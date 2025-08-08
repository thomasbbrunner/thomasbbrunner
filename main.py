import numpy as np
from pathlib import Path
from datetime import datetime, timezone

# ASCII characters in increasing level of brightness.
ASCII_CHARS =  r" .:-=+*#%@"
IMAGE_SIZE = (16, 16)
GRID_SIZE = (4, 4)

if __name__ == "__main__":

    rng = np.random.default_rng()

    image = np.zeros(shape=IMAGE_SIZE)
    displacement = rng.uniform(-1, 1, size=GRID_SIZE)
    gradients = rng.uniform(-1, 1, size=(*GRID_SIZE, 2))

    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            x0 = i % GRID_SIZE[0]
            y0 = j % GRID_SIZE[1]
            x1 = x0+1
            y1 = y0+1
            print(f"{i=},{j=}")
            print(f"{x0=},{y0=},{x1=},{y1=}")
            breakpoint()

    breakpoint()

    # TODO contents could be perlin noise or a random walk that keeps being updated.
    contents = f"""
```
WIP
```

Last generated: {datetime.now(timezone.utc).isoformat(sep=" ", timespec="seconds")}
"""

    readme_path = Path("README.md")
    readme_path.write_text(contents)
