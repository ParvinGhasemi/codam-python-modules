from abc import ABC, abstractmethod
from typing import Any


"""
In case the user does not validate the data before calling ingest,
and provides invalid data, an exception must be raised.
"""
class DataProcessor(ABC):

    def __init__(self) -> None:
        self._processed_data: list[tuple[int, str]] = []
        self._total_processed: int = 0

    @abstractmethod
    def validate(self, data: Any) -> bool:
        """
        will check whether the input data are appropriate
        for the current data processor
        """
        pass

    @abstractmethod
    def ingest(self, data: Any) -> None:
        """will process the input data."""
        pass

    def output(self) -> tuple[int, str]:
        """will output ingested data."""
        if not self._processed_data:
            raise IndexError("No processed data available")
        return self._processed_data.pop(0)


class NumericProcessor(DataProcessor):

    def validate(self, data: Any) -> bool:
        if isinstance(data, bool):
            return False

        if isinstance(data, (int, float)):
            return True

        if isinstance(data, list):
            return all(
                isinstance(item, (int, float))
                and not isinstance(item, bool)
                for item in data
            )
        return False

    def ingest(self, data: int | float | list[int | float]) -> None:
        """will process the input data."""
        if not self.validate(data):
            raise ValueError(f"Improper numeric data")

        items = data if isinstance(data, list) else [data]
        for item in items:
            self._processed_data.append((self._total_processed, str(item)))
            self._total_processed += 1


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
            raise ValueError(f"Improper text data")

        items = data if isinstance(data, list) else [data]
        for item in items:
            self._processed_data.append((self._total_processed, item))
            self._total_processed += 1

class LogProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        return True

    def ingest(self, data: dict[str, str]) -> None:
        """will process the input data."""
        pass


if __name__ == "__main__":

    numeric_processor: NumericProcessor = NumericProcessor()
    text_processor: TextProcessor = TextProcessor()
    # log_check: LogProcessor = LogProcessor()
    print("=== Code Nexus - Data Processor ===")
    print()

    print("Testing Numeric Processor...")

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

    try:
        numeric_processor.ingest("foo")
    except ValueError as error:
        print("Test invalid ingestion of string 'foo' without prior validation:")
        print(f"Got Exception: {error}")

    valid_numeric_list: list[int | float] = [1, 2.5, 3]
    numeric_processor.ingest(valid_numeric_list)
    print(f"Processing data: {valid_numeric_list}")
    print(f"Extracting {numeric_processor._total_processed} values...")
    for i, value in enumerate(numeric_processor._processed_data):
        print(f"Numeric value {i}: {value}")

    print()

    print("Testing Text Processor...")

    invalid_text: int = 42
    print(
        f"Trying to validate input '{invalid_text}': "
        f"{text_processor.validate(invalid_text)}"
    )

    valild_text_list: Any = ["Hello", "Nexus", "World"]
    print(
        f"Trying to validate input '{valild_text_list}': "
        f"{text_processor.validate(valild_text_list)}"
    )

    print(f"Extracting {text_processor._total_processed} value")

    print(f"T")

    print()

    print("Testing Log Processor...")
    print()

    # try:
    #     number.ingest([1, 0.5, 12.5, 1524])
    #     print(number._processed_data)
    #     print(number._total_processed)
    # except ValueError as error:
    #     print(f"Got Exception: \n{error}")
