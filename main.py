from pathlib import Path
from datetime import datetime, timezone

if __name__ == "__main__":
    contents = f"""
```
WIP
```

Last generated: {datetime.now(timezone.utc).isoformat(sep=" ", timespec="seconds")}
"""

    readme_path = Path("README.md")
    readme_path.write_text(contents)
