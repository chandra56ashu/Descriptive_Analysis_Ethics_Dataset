import json
from pathlib import Path

NOTEBOOK = Path("Descriptive_Analysis_Ethics_Dataset.ipynb")
OUTPUT = Path("NOTEBOOK_EXTRACT.md")
FOCUSED_OUTPUT = Path("NOTEBOOK_FOCUSED.md")

KEYWORDS = [
    "shape", "missing", "null", "imput", "univariate", "bivariate", "multivariate",
    "ethical culture", "culture index", "eci", "rule tolerance", "rti",
    "future ethical concern", "feci", "ethical acceptability", "eai",
    "q04", "q06", "q07", "q08", "q14", "q15", "age", "gender",
    "employment", "full-time", "part-time", "pressure", "retaliation",
    "speak", "raising", "awareness", "aware", "satisfaction", "younger", "older",
]


def clean_text(value):
    if isinstance(value, list):
        value = "".join(str(item) for item in value)
    return str(value).replace("\x1b", "")


def text_outputs(cell):
    outputs = []
    for output in cell.get("outputs", []):
        output_type = output.get("output_type")
        if output_type == "stream":
            outputs.append(clean_text(output.get("text", "")))
        elif output_type in {"execute_result", "display_data"}:
            data = output.get("data", {})
            if "text/plain" in data:
                outputs.append(clean_text(data["text/plain"]))
        elif output_type == "error":
            outputs.append("\n".join(output.get("traceback", [])))
    return outputs


with NOTEBOOK.open("r", encoding="utf-8") as file:
    notebook = json.load(file)

cells = notebook.get("cells", [])
markdown_cells = sum(cell.get("cell_type") == "markdown" for cell in cells)
code_cells = sum(cell.get("cell_type") == "code" for cell in cells)

lines = [
    "# Notebook extraction",
    "",
    f"- Total cells: {len(cells)}",
    f"- Markdown cells: {markdown_cells}",
    f"- Code cells: {code_cells}",
    "",
]

focused = [
    "# Focused notebook extraction",
    "",
    f"- Total cells: {len(cells)}",
    f"- Markdown cells: {markdown_cells}",
    f"- Code cells: {code_cells}",
    "",
]

for index, cell in enumerate(cells, start=1):
    cell_type = cell.get("cell_type", "unknown")
    source = clean_text(cell.get("source", []))
    outputs = text_outputs(cell)

    lines.append(f"## Cell {index} — {cell_type}")
    lines.append("")

    if cell_type == "markdown":
        lines.append(source.strip() or "_Empty markdown cell._")
        lines.append("")
    elif cell_type == "code":
        lines.extend(["```python", source.rstrip(), "```", ""])
        if outputs:
            lines.extend(["**Text output:**", ""])
            for output_text in outputs:
                output_text = output_text.strip()
                if len(output_text) > 5000:
                    output_text = output_text[:5000] + "\n... [output truncated]"
                lines.extend(["```text", output_text, "```", ""])

    haystack = (source + "\n" + "\n".join(outputs)).lower()
    if any(keyword in haystack for keyword in KEYWORDS):
        focused.extend([f"## Cell {index} — {cell_type}", ""])
        if cell_type == "markdown":
            focused.extend([source.strip() or "_Empty markdown cell._", ""])
        else:
            focused.extend(["```python", source.rstrip(), "```", ""])
            if outputs:
                focused.extend(["**Text output:**", ""])
                for output_text in outputs:
                    output_text = output_text.strip()
                    if len(output_text) > 3000:
                        output_text = output_text[:3000] + "\n... [output truncated]"
                    focused.extend(["```text", output_text, "```", ""])

OUTPUT.write_text("\n".join(lines), encoding="utf-8")
FOCUSED_OUTPUT.write_text("\n".join(focused), encoding="utf-8")
print(f"Wrote {OUTPUT} ({OUTPUT.stat().st_size} bytes)")
print(f"Wrote {FOCUSED_OUTPUT} ({FOCUSED_OUTPUT.stat().st_size} bytes)")
