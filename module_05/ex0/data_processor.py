from abc import ABC, abstractmethod
from typing import Any


class DataProcessor(ABC):

    def __init__(self) -> None:
        self._processed_data: list[tuple[int, str]] = []
        self._total_processed: int = 0

    @abstractmethod
    def validate(self, data: Any) -> bool:
        """Return whether this processor accepts the supplied data."""
        raise NotImplementedError

    @abstractmethod
    def ingest(self, data: Any) -> None:
        """Validate, transform, and store the supplied data."""
        raise NotImplementedError

    def output(self) -> tuple[int, str]:
        """Remove and return the oldest processed item."""
        if not self._processed_data:
            raise IndexError("No processed data available")
        return self._processed_data.pop(0)

    def _store(self, value: str) -> None:
        """Store the value with its processing rank."""
        rank: int = self._total_processed
        self._processed_data.append((rank, value))
        self._total_processed += 1


class NumericProcessor(DataProcessor):

    @staticmethod
    def _is_numeric(value: Any) -> bool:
        return (
            isinstance(value, (int, float))
            and not isinstance(value, bool)
        )

    def validate(self, data: Any) -> bool:
        if self._is_numeric(data):
            return True

        if isinstance(data, list):
            return all(self._is_numeric(item) for item in data)
        return False

    def ingest(
            self,
            data: int | float | list[int] | list[float] | list[int | float],
    ) -> None:
        """will process the input data."""
        if not self.validate(data):
            raise ValueError("Improper numeric data")

        items = data if isinstance(data, list) else [data]
        for item in items:
            self._store(str(item))


class TextProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if isinstance(data, (str)):
            return True
        if isinstance(data, list):
            return all(isinstance(item, str) for item in data)
        return False

    def ingest(self, data: str | list[str]) -> None:
        """will process the input data."""
        if not self.validate(data):
            raise ValueError("Improper text data")

        items = data if isinstance(data, list) else [data]
        for item in items:
            self._store(item)


class LogProcessor(DataProcessor):
    def _is_log_entry(self, data: Any) -> bool:
        if not isinstance(data, dict):
            return False

        if "log_level" not in data or "log_message" not in data:
            return False

        return all(
            isinstance(key, str) and isinstance(value, str)
            for key, value in data.items()
        )

    def validate(self, data: Any) -> bool:
        if self._is_log_entry(data):
            return True
        if isinstance(data, list):
            return all(self._is_log_entry(item) for item in data)
        return False

    def ingest(self, data: dict[str, str] | list[dict[str, str]]) -> None:
        """will process the input data."""
        if not self.validate(data):
            raise ValueError("Improper log data")

        logs: list[dict[str, str]] = data if isinstance(data, list) else [data]
        for entry in logs:
            log_level: str = entry["log_level"]
            log_message: str = entry["log_message"]
            self._store(f"{log_level}: {log_message}")


def print_outputs(
        processor: DataProcessor,
        amount: int,
        label: str,
) -> None:
    for _ in range(amount):
        rank, value = processor.output()
        print(f"{label} {rank}: {value}")


def test_numeric_processor() -> None:
    print("Testing Numeric Processor...")
    numeric_processor: NumericProcessor = NumericProcessor()

    valid_numeric_data: int = 42
    print(
        f"Trying to validate input '{valid_numeric_data}': "
        f"{numeric_processor.validate(valid_numeric_data)}"
    )

    invalid_numeric_data: str = "Hello"
    print(
            f"Trying to validate input '{invalid_numeric_data}': "
            f"{numeric_processor.validate(invalid_numeric_data)}"
    )

    print("Test invalid ingestion of string 'foo' without prior validation:")
    try:
        numeric_processor.ingest("foo")
    except ValueError as error:
        print(f"Got Exception: {error}")

    numeric_data: list[int | float] = [1, 2, 3, 4, 5]
    print(f"Processing data: {numeric_data}")
    numeric_processor.ingest(numeric_data)

    print("Extracting 3 values...")
    print_outputs(numeric_processor, 3, "Numeric value")

    print()


def test_text_processor() -> None:
    text_processor = TextProcessor()

    print("Testing Text Processor...")
    print(
        "Trying to validate input '42': "
        f"{text_processor.validate(42)}"
    )

    text_data = ["Hello", "Nexus", "World"]
    print(f"Processing data: {text_data}")
    text_processor.ingest(text_data)

    print("Extracting 1 value...")
    print_outputs(text_processor, 1, "Text value")


def test_log_processor() -> None:
    log_processor = LogProcessor()

    print("Testing Log Processor...")
    print(
        "Trying to validate input 'Hello': "
        f"{log_processor.validate('Hello')}"
    )

    log_data = [
        {
            "log_level": "NOTICE",
            "log_message": "Connection to server",
        },
        {
            "log_level": "ERROR",
            "log_message": "Unauthorized access!!",
        },
    ]

    print(f"Processing data: {log_data}")
    log_processor.ingest(log_data)

    print("Extracting 2 values...")
    print_outputs(log_processor, 2, "Log entry")


if __name__ == "__main__":
    print("=== Code Nexus - Data Processor ===")
    test_numeric_processor()
    print()
    test_text_processor()
    print()
    test_log_processor()
