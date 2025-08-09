import subprocess
import re
from pathlib import Path

README = Path("README.md")

# Get current tree output
tree_cmd = [
    "tree",
    "-I", "__pycache__|*.pyc|*.pyo|.git|env|venv|.idea|node_modules",
]
tree_output = subprocess.check_output(tree_cmd).decode("utf-8")

# Read README
content = README.read_text(encoding="utf-8")

# Pattern to replace
pattern = r"(## 📂 Project Structure\n```bash\n)(.*?)(\n```)"
new_content = re.sub(pattern, r"\1" + tree_output + r"\3", content, flags=re.S)

# Write updated README
README.write_text(new_content, encoding="utf-8")
print("✅ README updated with latest project tree.")
