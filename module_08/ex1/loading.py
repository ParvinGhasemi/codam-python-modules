import importlib
import numpy as np
import pandas as pd


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


def analyze_data() -> None:
    count: int = 88
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


def main() -> None:
    print("LOADING STATUS: Loading programs...\n")
    dependencies_ready: bool = check_dependencies()
    if not dependencies_ready:
        print("From the ex1 directory, install the dependencies with:")
        print("python3 -m pip install -r requirements.txt")
        # print("Install the dependencies in your virtual environment with:")
        # print("python3 -m pip install numpy pandas matplotlib")
        return

    print()
    print("Ready to analyze Matrix data!")

    analyze_data()


# instead of normal, what other are available?

if __name__ == "__main__":
    main()
