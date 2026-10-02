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


if __name__ == "__main__":
    main()
