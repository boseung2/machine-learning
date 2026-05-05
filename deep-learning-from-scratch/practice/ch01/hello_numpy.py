import sys
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main() -> None:
    root = Path(__file__).resolve().parents[2]
    output_dir = root / "outputs"
    output_dir.mkdir(exist_ok=True)

    x = np.arange(5)
    y = x ** 2

    print(f"Python: {sys.version.split()[0]}")
    print(f"NumPy: {np.__version__}")
    print(f"Matplotlib: {matplotlib.__version__}")
    print(f"x = {x}")
    print(f"y = {y}")

    plt.figure()
    plt.plot(x, y, marker="o")
    plt.title("y = x^2")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.grid(True)

    output_path = output_dir / "ch01_square.png"
    plt.savefig(output_path, dpi=150, bbox_inches="tight")
    print(f"saved: {output_path.relative_to(root)}")


if __name__ == "__main__":
    main()
