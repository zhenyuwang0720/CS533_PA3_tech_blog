#!/usr/bin/env python3
"""Generate Jekyll notebook catalog from notebooks/*.ipynb without executing code."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
items = []
for path in sorted((ROOT / "notebooks").rglob("*.ipynb")):
    if ".ipynb_checkpoints" in path.parts:
        continue
    try:
        notebook = json.loads(path.read_text(encoding="utf-8"))
        if notebook.get("nbformat") not in (4,):
            print(f"Skipping unsupported file: {path}")
            continue
        markdown = ""
        for cell in notebook.get("cells", []):
            if cell.get("cell_type") == "markdown":
                source = cell.get("source", [])
                markdown = "".join(source) if isinstance(source, list) else str(source)
                if markdown.strip():
                    break
        lines = [line.strip() for line in markdown.splitlines() if line.strip()]
        title = next((line.lstrip("# ").strip() for line in lines if line.startswith("#")), path.stem.replace("_", " ").title())
        description = next((line for line in lines if not line.startswith("#") and not line.startswith("!") and not line.startswith("[")), "Open the interactive analysis notebook.")
        items.append({"title": title[:120], "description": description[:240], "path": path.relative_to(ROOT).as_posix()})
    except (OSError, ValueError, UnicodeError) as error:
        print(f"Skipping unreadable notebook {path}: {error}")
output = ROOT / "_data" / "notebooks.json"
output.parent.mkdir(parents=True, exist_ok=True)
output.write_text(json.dumps(items, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
print(f"Indexed {len(items)} notebooks")
