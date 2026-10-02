import importlib


"""
python3 -m pip install -r requirements.txt
python3 loading.py

poetry install
poetry run python loading.py
"""


def check_dependencies() -> bool:
    dependencies: dict[str, str] = {
        "numpy": "Numerical computation ready",
        "pandas": "Data manipulation ready",
        "matplotlib": "Visualization ready",
    }
    all_deps_available: bool = True

    print("Checking dependencies:")

    for name, description in dependencies.items():
        try:
            package = importlib.import_module(name)
            version: str = str(package.__version__)
            print(f"[OK] {name} ({version}) - {description}")

        except ImportError:
            print(f"[ERROR]: MISSING OR UNAVAILABLE {name}")
            all_deps_available = False
    return all_deps_available


def compare_package_managers() -> None:
    """Explain the two supported dependency management approaches."""

    print()
    print()
    print("=================================================================")
    print("Dependency management:")
    print("** pip ** installs packages into your selected Python environment.")
    print("This project lists its pip dependencies in requirements.txt.")
    print("     python3 -m pip install -r requirements.txt")

    print()
    print("** Poetry ** manages project dependencies & virtual environments.")
    print(
        "It reads pyproject.toml and records resolved versions "
        "in poetry.lock."
    )
    print("     poetry install")
    print("     poetry run python loading.py")
    print("=================================================================")
    print()
    print()


def analyze_data() -> None:
    """Generate simulated Matrix data and save a visualization."""
    import numpy as np
    import pandas as pd
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    count: int = 88
    output_file: str = "matrix_analysis.png"
    rng = np.random.default_rng(seed=12)
    signal: list[float] = rng.normal(loc=50, scale=10, size=count)
    print(signal[:10])
    print()

    data = pd.DataFrame({
        "sample": np.arange(count),
        "signal": signal,
    })
    print(data.head())
    print()
    print()

    data["rolling_avg"] = (
        data["signal"].rolling(window=50, min_periods=1).mean()
    )
    print(data.head())
    print()
    print()

    average: float = float(data["signal"].mean())
    minimum: float = float(data["signal"].min())
    maximum: float = float(data["signal"].max())
    total: int = len(data)
    median: float = float(data["signal"].median())
    std_dev: float = float(data["signal"].std())

    print(f"Average signal:     {average:.2f}")
    print(f"Minimum signal:     {minimum:.2f}")
    print(f"Maximum signal:     {maximum:.2f}")
    print(f"Total measurements: {total}")
    print(f"Median signal:      {median:.2f}")
    print(f"Standard deviation: {std_dev:.2f}")
    print()

    print("\nSignal summary:")
    print(data["signal"].describe())

    print("\nGenerating visualization...")

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.plot(
        data["sample"],
        data["signal"],
        color="seagreen",
        linewidth=2.1,
        label="Simulated signal",
    )

    ax.set_title("Matrix Signal Analysis")
    ax.set_xlabel("Sample")
    ax.set_ylabel("Signal strength")
    ax.legend()
    ax.grid(alpha=0.3)

    fig.tight_layout()
    fig.savefig(output_file, dpi=150)
    plt.close(fig)

    print("Analysis complete!")
    print(f"Results saved to: {output_file}")


def main() -> None:
    """Check dependencies, explain installation, and run the analysis."""

    print("LOADING STATUS: Loading programs...\n")
    dependencies_ready: bool = check_dependencies()
    compare_package_managers()

    if not dependencies_ready:
        print("*****      What to do?    *****")
        print("From the ex1 directory, install the dependencies with:")
        print("python3 -m pip install -r requirements.txt")
        # print("Install the dependencies in your virtual environment with:")
        # print("python3 -m pip install numpy pandas matplotlib")
        return

    print()
    print("Ready to analyze Matrix data!")

    analyze_data()


# instead of normaldistribution we can:
# rng.normal(50, 10, size=1000)
# Bell-shaped data centered around 50	Noisy signal measurements
# -----------------
# rng.uniform(0, 100, size=1000)	# Values from 0 up to 100, with equal
# likelihood across equal-sized intervals
# Random signal levels without a preferred center
# -----------------
# rng.integers(0, 101, size=1000)
# Whole numbers from 0 through 100	Random scores
# -----------------
# rng.binomial(1, 0.8, size=1000)
# Either 0 or 1, with an 80% chance of 1
# Connection success or failure
# -----------------
# rng.poisson(5, size=1000)
# Event counts averaging 5 per interval
# Requests received each second
# -----------------
# rng.exponential(2, size=1000)
# Nonnegative waiting times averaging 2Time between events

if __name__ == "__main__":
    main()
