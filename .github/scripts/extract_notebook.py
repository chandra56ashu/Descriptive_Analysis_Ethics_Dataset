import json
from pathlib import Path

NOTEBOOK = Path("Descriptive_Analysis_Ethics_Dataset.ipynb")
OUTPUT = Path("NOTEBOOK_EXTRACT.md")


def clean_text(value):
    if isinstance(value, list):
        value = "".join(str(item) for item in value)
    return str(value).replace("\x1b", "")


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

for index, cell in enumerate(cells, start=1):
    cell_type = cell.get("cell_type", "unknown")
    source = clean_text(cell.get("source", []))

    lines.append(f"## Cell {index} — {cell_type}")
    lines.append("")

    if cell_type == "markdown":
        lines.append(source.strip() or "_Empty markdown cell._")
        lines.append("")
        continue

    if cell_type == "code":
        lines.append("```python")
        lines.append(source.rstrip())
        lines.append("```")
        lines.append("")

        text_outputs = []
        for output in cell.get("outputs", []):
            output_type = output.get("output_type")
            if output_type == "stream":
                text_outputs.append(clean_text(output.get("text", "")))
            elif output_type in {"execute_result", "display_data"}:
                data = output.get("data", {})
                if "text/plain" in data:
                    text_outputs.append(clean_text(data["text/plain"]))
            elif output_type == "error":
                text_outputs.append("\n".join(output.get("traceback", [])))

        if text_outputs:
            lines.append("**Text output:**")
            lines.append("")
            for output_text in text_outputs:
                output_text = output_text.strip()
                if len(output_text) > 5000:
                    output_text = output_text[:5000] + "\n... [output truncated]"
                lines.append("```text")
                lines.append(output_text)
                lines.append("```")
                lines.append("")

OUTPUT.write_text("\n".join(lines), encoding="utf-8")
print(f"Wrote {OUTPUT} ({OUTPUT.stat().st_size} bytes)")
