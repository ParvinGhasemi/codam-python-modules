import importlib


"""
python3 -m pip install -r requirements.txt
python3 loading.py

poetry install
poetry run python loading.py
"""


def check_dependencies() -> bool:
    print("Checking dependencies:")

    try:
        package = importlib.import_module("numpy")
        version: str = str(package.__version__)
        print(f"[OK] numpy ({version})")
        return True

    except ImportError:
        print("[ERROR]: MISSING OR UNAVAILABLE numpy")
        return False




def main() -> None:
    print("LOADING STATUS: Loading programs...\n")
    dependencies_ready: bool = check_dependencies()
    if not dependencies_ready:
        if not dependencies_ready:
            print("Install NumPy in your virtual environment with:")
            print("python3 -m pip install numpy")
            return

    print()
    print("Ready to analyze Matrix data!")


if __name__ == "__main__":
    main()
