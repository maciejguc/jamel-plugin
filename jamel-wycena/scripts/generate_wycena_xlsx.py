"""Standalone template-based XLSX generator for ELA-style estimates ("Wycena").

Ported from ELA's ``apps/estimates/xlsx_generator.py`` (render layer, kept
byte-identical for pixel-identical output) and ``apps/estimates/services.py``
(data layer: ordering + rate resolution + totals), with all Django
dependencies removed. Input is a plain JSON payload; output is an .xlsx file
assembled from the bundled ``assets/estimate_template.xlsx``.

The render functions below (``load_template`` … ``generate_xlsx``) are a verbatim
port: the entire visual style — fonts, colors, borders, column widths, merges,
logo — comes from the template, never hardcoded.

CLI:
    python generate_wycena_xlsx.py input.json -o wycena.xlsx
"""
from __future__ import annotations

import argparse
import json
import math
import re
import sys
import zipfile
from collections import defaultdict
from copy import copy
from dataclasses import dataclass, field
from datetime import date
from decimal import Decimal
from io import BytesIO
from pathlib import Path
from typing import TYPE_CHECKING, Any

import openpyxl
from openpyxl import Workbook
from openpyxl.drawing.image import Image as XLImage
from openpyxl.utils import get_column_letter

if TYPE_CHECKING:
    from openpyxl.worksheet.worksheet import Worksheet

TEMPLATE_PATH = Path(__file__).resolve().parent.parent / "assets" / "estimate_template.xlsx"
LOGO_ZIP_PATH = "xl/media/image1.png"
LOGO_WIDTH_PX = 74
LOGO_HEIGHT_PX = 119
NUM_COLS = 9  # A through I

# ---------------------------------------------------------------------------
# Hardcoded role -> hourly rate fallback (PLN netto). Ported verbatim from
# ELA services.py ROLE_RATES. Used only when neither a per-item rate nor a
# payload ``role_rates`` entry resolves the role.
# ---------------------------------------------------------------------------
ROLE_RATES: dict[str, Decimal] = {
    "Project Manager": Decimal("225"),
    "Web Designer": Decimal("225"),
    "Front-end Developer": Decimal("250"),
    "Back-end Developer": Decimal("250"),
    "Tester": Decimal("180"),
    "Redaktor": Decimal("180"),
    "Programista": Decimal("250"),
}


# ===========================================================================
# Data layer (port of services.py::_create_line_items)
# ===========================================================================
@dataclass
class Role:
    """Minimal stand-in for ELA's Role model — only ``name`` is read by render."""

    name: str


@dataclass
class LineItem:
    """Resolved estimate line item.

    Mirrors the attribute surface that the render layer reads from ELA's
    ``EstimateLineItem`` model: ``stage``, ``stage_order``, ``item_order``,
    ``display_number``, ``title``, ``description``, ``role.name``, ``hours``,
    ``hourly_rate``, ``total``.
    """

    stage: str
    title: str
    description: str
    hours: Decimal
    hourly_rate: Decimal
    stage_order: int = 0
    item_order: int = 0
    display_number: str = ""
    total: Decimal = Decimal("0")
    role: Role | None = None


def _as_decimal(value: Any) -> Decimal:
    return Decimal(str(value))


def assemble_line_items(payload: dict) -> tuple[list[LineItem], dict]:
    """Resolve raw payload line items into ordered, rated :class:`LineItem`s.

    Ports ELA ``_create_line_items``: groups by stage in order of first
    appearance (-> ``stage_order``), assigns per-stage ``item_order``, sets
    ``display_number = "{stage_order}.{item_order}"``, resolves the hourly rate
    (per-item ``hourly_rate`` > payload ``role_rates`` > ``ROLE_RATES`` >
    ``default_hourly_rate``) and computes ``total = hours * rate``.

    Args:
        payload: Parsed estimate payload (see ``reference/line-item-schema.json``).

    Returns:
        A ``(line_items, meta)`` tuple. ``meta`` is the payload's ``meta`` block.
    """
    meta = payload.get("meta", {})
    fallback_rate = _as_decimal(meta.get("default_hourly_rate") or 200)

    # Build resolved rate map: payload role_rates override ROLE_RATES fallback.
    rate_map: dict[str, Decimal] = dict(ROLE_RATES)
    for role_name, rate in (payload.get("role_rates") or {}).items():
        rate_map[role_name] = _as_decimal(rate)

    # Group items by stage to assign stage_order + item_order, preserving the
    # order in which each stage first appears (insertion order of dict keys).
    stage_items: dict[str, list[dict]] = defaultdict(list)
    for item in payload.get("line_items", []):
        if isinstance(item, dict):
            stage_items[item.get("stage", "development")].append(item)

    result: list[LineItem] = []
    stage_order_counter = 1
    for stage_name, items in stage_items.items():
        for item_order, item in enumerate(items, start=1):
            hours = _as_decimal(item.get("hours", 0))
            role_name = str(item.get("role", ""))
            if item.get("hourly_rate") is not None:
                rate = _as_decimal(item["hourly_rate"])
            else:
                rate = rate_map.get(role_name, fallback_rate)
            result.append(
                LineItem(
                    stage=stage_name,
                    title=item.get("title") or item.get("category", "General"),
                    description=item.get("description", ""),
                    stage_order=stage_order_counter,
                    item_order=item_order,
                    display_number=f"{stage_order_counter}.{item_order}",
                    role=Role(role_name) if role_name else None,
                    hours=hours,
                    hourly_rate=rate,
                    total=hours * rate,
                )
            )
        stage_order_counter += 1

    return result, meta


# ===========================================================================
# Render layer (verbatim port of xlsx_generator.py — keeps pixel identity)
# ===========================================================================
def load_template() -> openpyxl.Workbook:
    """Load the estimate template workbook with all building-block sheets."""
    return openpyxl.load_workbook(TEMPLATE_PATH)


def extract_logo_bytes() -> bytes:
    """Extract the logo PNG from the template XLSX ZIP archive."""
    with zipfile.ZipFile(TEMPLATE_PATH) as zf:
        return zf.read(LOGO_ZIP_PATH)


_STAGE_PREFIX_RE = re.compile(r"^Etap\s+\d+:\s*", re.IGNORECASE)


def _strip_stage_prefix(name: str) -> str:
    """Strip AI-generated 'Etap N: ' prefix from stage names."""
    return _STAGE_PREFIX_RE.sub("", name)


def _apply_column_widths(source_ws: "Worksheet", target_ws: "Worksheet") -> None:
    """Copy column widths from source sheet to target sheet, with B +20%."""
    for letter, dim in source_ws.column_dimensions.items():
        if dim.width:
            width = dim.width * 1.2 if letter == "B" else dim.width
            target_ws.column_dimensions[letter].width = width


def _auto_row_height(ws: "Worksheet", row: int, description: str, col_b_width: float) -> None:
    """Estimate and set row height based on description length."""
    if not description:
        return
    chars_per_line = max(10, int(col_b_width * 1.3))
    lines = sum(
        max(1, math.ceil(len(part) / chars_per_line))
        for part in description.split("\n")
    )
    if lines > 1:
        current = ws.row_dimensions[row].height or 15
        ws.row_dimensions[row].height = max(current, lines * 13)


def _replace_variables(value: Any, var_map: dict[str, Any]) -> Any:
    """Replace all {{key}} placeholders in a string value."""
    if not isinstance(value, str):
        return value
    for key, replacement in var_map.items():
        value = value.replace(f"{{{{{key}}}}}", str(replacement))
    return value


def _copy_row(
    source_ws: "Worksheet",
    source_row: int,
    target_ws: "Worksheet",
    target_row: int,
    var_map: dict[str, Any] | None = None,
) -> None:
    """Copy one row from source_ws to target_ws, substituting variables and styles."""
    if var_map is None:
        var_map = {}

    # --- Copy cell values and styles ---
    for col in range(1, NUM_COLS + 1):
        src_cell = source_ws.cell(row=source_row, column=col)
        dst_cell = target_ws.cell(row=target_row, column=col)

        raw = src_cell.value

        # Skip broken formula references from template (e.g. =SUM(#REF!,...))
        if isinstance(raw, str) and "#REF!" in raw:
            dst_cell.value = None
        else:
            dst_cell.value = _replace_variables(raw, var_map)

        # Copy styles (each must be a fresh copy, not a reference)
        if src_cell.has_style:
            dst_cell.font      = copy(src_cell.font)
            dst_cell.fill      = copy(src_cell.fill)
            dst_cell.border    = copy(src_cell.border)
            dst_cell.alignment = copy(src_cell.alignment)
            dst_cell.number_format = src_cell.number_format

    # --- Copy row height ---
    src_height = source_ws.row_dimensions[source_row].height
    if src_height:
        target_ws.row_dimensions[target_row].height = src_height

    # --- Copy merged cells, offset to target_row ---
    row_delta = target_row - source_row
    existing_ranges = {str(r) for r in target_ws.merged_cells.ranges}
    for merged_range in source_ws.merged_cells.ranges:
        if merged_range.min_row <= source_row <= merged_range.max_row:
            new_min_row = merged_range.min_row + row_delta
            new_max_row = merged_range.max_row + row_delta
            min_col_letter = get_column_letter(merged_range.min_col)
            max_col_letter = get_column_letter(merged_range.max_col)
            target_range = f"{min_col_letter}{new_min_row}:{max_col_letter}{new_max_row}"
            if target_range not in existing_ranges:
                target_ws.merge_cells(target_range)
                existing_ranges.add(target_range)


# Sheet name constants for line item variants
VARIANT_SINGLE = "line-item-single"
VARIANT_FIRST  = "line-item-first"
VARIANT_MIDDLE = "line-item-middle"
VARIANT_LAST   = "line-item-last"


def _group_by_stage(
    line_items: list[Any],
) -> list[tuple[int, str, list[Any], list[str]]]:
    """Group line items by stage, assign template variant names per item."""
    stage_map: dict[int, tuple[str, list[Any]]] = {}
    for item in line_items:
        so = item.stage_order
        if so not in stage_map:
            stage_map[so] = (item.stage, [])
        stage_map[so][1].append(item)

    groups: list[tuple[int, str, list[Any], list[str]]] = []
    for stage_order, (stage_name, items) in sorted(stage_map.items()):
        # Sort items within stage by item_order
        items.sort(key=lambda li: li.item_order)

        n = len(items)
        if n == 1:
            variants = [VARIANT_SINGLE]
        else:
            variants = (
                [VARIANT_FIRST]
                + [VARIANT_MIDDLE] * (n - 2)
                + [VARIANT_LAST]
            )
        groups.append((stage_order, stage_name, items, variants))

    return groups


def _reapply_h_style(src_cell: Any, dst_cell: Any) -> None:
    """Re-apply H-column cell styles after a formula write clears them."""
    if src_cell.has_style:
        dst_cell.font         = copy(src_cell.font)
        dst_cell.fill         = copy(src_cell.fill)
        dst_cell.border       = copy(src_cell.border)
        dst_cell.alignment    = copy(src_cell.alignment)
        dst_cell.number_format = src_cell.number_format


def generate_xlsx(line_items: list[LineItem], meta: dict) -> bytes:
    """Generate an XLSX file from resolved line items + meta, using the template.

    Assembles the output by copying rows from named template sheets:
      1. estimate-header (5 rows) — title, date, author, spacer, column headers
      2. For each stage: etap-header + line items (first/middle/last/single)
      3. sum — SUMA row with =SUM(...) of all H cells
      4. last-row — closing spacer

    Args:
        line_items: Resolved :class:`LineItem`s (see :func:`assemble_line_items`).
        meta: Estimate meta block (``title``, ``client_name``, ``author``).

    Returns:
        Raw XLSX bytes.
    """
    template = load_template()
    wb = Workbook()
    ws = wb.active
    ws.title = "Wycena"

    # Apply column widths from template header sheet
    _apply_column_widths(template["estimate-header"], ws)

    current_row = 1
    h_cells: list[str] = []  # collect all H column addresses for SUM

    # ------------------------------------------------------------------
    # 1. Header block (rows 1-5 from estimate-header sheet)
    # ------------------------------------------------------------------
    author = meta.get("author") or {}
    first_name = author.get("first_name", "")
    last_name = author.get("last_name", "")

    title = meta.get("title", "")
    header_var_map = {
        "estimate-title": title,
        "client": meta.get("client_name") or title,
        "today": date.today().strftime("%d.%m.%Y"),
        "user-firstname": first_name,
        "user-lastname": last_name,
    }

    header_ws = template["estimate-header"]
    for src_row in range(1, header_ws.max_row + 1):
        _copy_row(header_ws, src_row, ws, current_row, header_var_map)
        current_row += 1

    # Embed logo at B1
    try:
        logo_bytes = extract_logo_bytes()
        img = XLImage(BytesIO(logo_bytes))
        img.width = LOGO_WIDTH_PX
        img.height = LOGO_HEIGHT_PX
        img.anchor = "B1"
        ws.add_image(img)
    except Exception:
        pass  # logo is non-critical — generate without it on any error

    # ------------------------------------------------------------------
    # 2. Stages + line items
    # ------------------------------------------------------------------
    groups = _group_by_stage(list(line_items))

    col_b_width = ws.column_dimensions["B"].width if ws.column_dimensions["B"].width else 40

    for stage_order, stage_name, items, variants in groups:
        clean_stage_name = _strip_stage_prefix(stage_name)
        # --- etap-header ---
        _copy_row(
            template["etap-header"], 1, ws, current_row,
            var_map={"stage-name": f"{stage_order}. {clean_stage_name}"},
        )
        current_row += 1

        # --- line items ---
        for item, variant in zip(items, variants):
            role_name = item.role.name if item.role else ""
            var_map = {
                "line-item-number": item.display_number,
                "line-item-title": item.title,
                "line-item-description": item.description,
                "role": role_name,
                "hours": float(item.hours),
                "rate": float(item.hourly_rate),
            }
            _copy_row(template[variant], 1, ws, current_row, var_map)

            # Write hours x rate formula directly (template has =F1*G1 for row 1;
            # we replace it with the correct target row number)
            h_addr = f"H{current_row}"
            ws[h_addr] = f"=F{current_row}*G{current_row}"
            # Re-apply H cell style from template (formula write clears it)
            _reapply_h_style(template[variant].cell(row=1, column=8), ws.cell(row=current_row, column=8))

            # Auto-adjust row height for long descriptions
            _auto_row_height(ws, current_row, item.description or "", col_b_width)

            h_cells.append(h_addr)
            current_row += 1

    # ------------------------------------------------------------------
    # 3. SUMA row
    # ------------------------------------------------------------------
    _copy_row(template["sum"], 1, ws, current_row)
    if h_cells:
        sum_formula = f"=SUM({','.join(h_cells)})"
        ws[f"H{current_row}"] = sum_formula
        # Re-apply H cell style from sum template sheet
        _reapply_h_style(template["sum"].cell(row=1, column=8), ws.cell(row=current_row, column=8))
    current_row += 1

    # ------------------------------------------------------------------
    # 4. Last row (closing spacer)
    # ------------------------------------------------------------------
    _copy_row(template["last-row"], 1, ws, current_row)

    # ------------------------------------------------------------------
    # Serialize
    # ------------------------------------------------------------------
    buffer = BytesIO()
    wb.save(buffer)
    return buffer.getvalue()


def generate_from_payload(payload: dict) -> bytes:
    """Convenience: resolve a raw payload and render it to XLSX bytes."""
    line_items, meta = assemble_line_items(payload)
    return generate_xlsx(line_items, meta)


# ===========================================================================
# CLI
# ===========================================================================
def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Generate an ELA-style estimate .xlsx from a JSON payload.")
    parser.add_argument("input", help="Path to the input JSON payload.")
    parser.add_argument("-o", "--output", default="wycena.xlsx", help="Output .xlsx path (default: wycena.xlsx).")
    args = parser.parse_args(argv)

    payload = json.loads(Path(args.input).read_text(encoding="utf-8"))
    data = generate_from_payload(payload)
    Path(args.output).write_bytes(data)
    print(f"Wrote {args.output} ({len(data)} bytes)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
