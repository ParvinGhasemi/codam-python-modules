# Files to Submit: oracle.py, .env.example, .gitignore
# Authorized: os, sys, python-dotenv modules, file operations

# •MATRIX_MODE - "development" or "production"
# •DATABASE_URL - Connection string for data storage
# •API_KEY - Secret key for external services
# •LOG_LEVEL - Logging verbosity
# •ZION_ENDPOINT - URL for the resistance network

import os
import sys

try:
    from dotenv import load_dotenv
except ImportError:
    print("[ERROR]: python-dotenv is unavailable")
    print("Install it in your virtual environment:")
    print("     python -m pip install python-dotenv")
    sys.exit(1)


def main() -> None:

    load_dotenv(override=False)

    print("ORACLE STATUS: Reading the Matrix...")
    print()

    mode: str = os.getenv('MATRIX_MODE', "development")
    # mode_second: str = os.environ.get("MATRIX_MODE", "development")
    # print(f"Mode with environ: {mode_second}")
    # third: str = os.environ["MATRIX_MODE"]
    # print(f"Mode with environ: {third}")

    if mode not in ("production", "development"):
        print("[ERROR]: MATRIX_MODE must be 'production' or 'development'.")
        sys.exit(1)

    default_level: str = "DEBUG" if mode == "development" else "INFO"
    log_level: str = os.getenv("LOG_LEVEL", default_level).upper()

    allowed_levels: tuple[str, ...] = (
        "DEBUG",
        "INFO",
        "WARNING",
        "ERROR",
        "CRITICAL",
    )

    if log_level not in allowed_levels:
        print(
            "[ERROR]: LOG_LEVEL must be "
            "DEBUG, INFO, WARNING, ERROR, CRITICAL"
        )
        sys.exit(1)

    required_settings: tuple[str, ...] = (
        "DATABASE_URL",
        "API_KEY",
        "ZION_ENDPOINT"
    )
    all_configs_present: bool = True

    for config in required_settings:
        value = os.getenv(config, "")

        if not value.strip():
            print(f"[ERROR]: Missing required setting: {config}")
            all_configs_present = False

    if not all_configs_present:
        sys.exit(1)

    print(f"Mode: {mode}")
    print(f"Log level: {log_level}")
    if log_level == "DEBUG":
        print("[DEBUG] All required settings contain nonempty values.")
        print("[DEBUG] No database or API connection has been attempted.")

    if log_level in ("DEBUG", "INFO"):
        print(f"[INFO] Database: [OK] - Configured")
        print(f"[INFO] API key: [OK] - Configured (hidden)")
        print(f"[INFO] Zion endpoint: [OK] - Configured")


if __name__ == "__main__":
    main()
