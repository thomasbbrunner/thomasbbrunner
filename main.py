import numpy as np
from pathlib import Path
from datetime import datetime, timezone
import math

# ASCII characters in increasing level of brightness.
ASCII_CHARS = r" .:-=+*#%@"
IMAGE_SIZE = (24, 160)
GRID_SIZE_CHOICES = range(4, 8)

if __name__ == "__main__":
    rng = np.random.default_rng()

    grid_size = rng.choice(GRID_SIZE_CHOICES, size=2, replace=True)

    image = np.zeros(shape=IMAGE_SIZE)
    image_heights = np.zeros(shape=IMAGE_SIZE)
    # heights = rng.normal(-1, 1, size=grid_size)
    heights = rng.uniform(-1, 1, size=grid_size)

    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            # Image to grid coordinates.
            xi = i / (IMAGE_SIZE[0] / grid_size[0])
            yi = j / (IMAGE_SIZE[1] / grid_size[1])

            # Grid corners.
            x0 = math.floor(xi)
            y0 = math.floor(yi)
            # Includes wrap around.
            x1 = x0 + 1 if x0 + 1 < grid_size[0] else 0
            y1 = y0 + 1 if y0 + 1 < grid_size[1] else 0

            # Interpolation of grid heights.
            xd = np.array([[x1 - xi, xi - x0]])
            yd = np.array([[y1 - yi], [yi - y0]])
            h = np.array(
                [[heights[x0, y0], heights[x0, y1]], [heights[x1, y0], heights[x1, y1]]]
            )
            hd = 1 / ((x1 - x0) * (y1 - y0)) * (xd @ h @ yd)

            image_heights[i, j] = hd

    bin_edges = np.histogram_bin_edges(image_heights, len(ASCII_CHARS) - 1)
    image_heights_categories = np.digitize(image_heights, bin_edges) - 1

    ascii_chars = np.array([c for c in ASCII_CHARS])
    image = ascii_chars[image_heights_categories]

    contents = f"""
```
{"\n".join(["".join(line) for line in image])}
```

This is procedurally generated (last generated: {datetime.now(timezone.utc).isoformat(sep=" ", timespec="seconds")})
"""
    print(contents)
    readme_path = Path("README.md")
    readme_path.write_text(contents)
