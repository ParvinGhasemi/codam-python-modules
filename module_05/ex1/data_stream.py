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

    @property
    def total_processed(self) -> int:
        """Return the total number of processed items."""
        return self._total_processed

    @property
    def remaining(self) -> int:
        """Return the number of items waiting for output."""
        return len(self._processed_data)

    @property
    def processor_name(self) -> str:
        """Return a readable version of the class name."""
        return type(self).__name__.replace("Processor", " Processor")


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


class DataStream:
    def __init__(self) -> None:
        self._processors: list[DataProcessor] = []

    def register_processor(self, proc: DataProcessor) -> None:
        """Register a processor for future stream elements."""
        self._processors.append(proc)

    def process_stream(self, stream: list[Any]) -> None:
        """Route every element to the first compatible processor."""
        for element in stream:
            for processor in self._processors:
                if processor.validate(element):
                    processor.ingest(element)
                    break
            else:
                print(
                    "DataStream error - Can't process element "
                    f"in stream: {element}"
                )

    def print_processors_stats(self) -> None:
        """Print statistics for every registered processor."""
        print("== DataStream statistics ==")

        if not self._processors:
            print("No processor found, no data")
            return

        for processor in self._processors:
            print(
                f"{processor.processor_name}: total "
                f"{processor.total_processed} items processed, "
                f"remaining {processor.remaining} on processor"
            )


def consume(processor: DataProcessor, amount: int) -> None:
    """Remove a given number of items from a processor."""
    for _ in range(amount):
        processor.output()


def main() -> None:
    print("=== Code Nexus - Data Stream ===")
    print()
    print("Initialize Data Stream...")

    data_stream = DataStream()
    numeric_processor = NumericProcessor()
    text_processor = TextProcessor()
    log_processor = LogProcessor()

    data_stream.print_processors_stats()

    print()
    print("Registering Numeric Processor")
    data_stream.register_processor(numeric_processor)

    first_batch: list[Any] = [
        "Hello world",
        [3.14, -1, 2.71],
        [
            {
                "log_level": "WARNING",
                "log_message": "Telnet access! Use ssh instead",
            },
            {
                "log_level": "INFO",
                "log_message": "User wil is connected",
            },
        ],
        42,
        ["Hi", "five"],
    ]

    print()
    print(f"Send first batch of data on stream: {first_batch}")
    data_stream.process_stream(first_batch)
    data_stream.print_processors_stats()

    print()
    print("Registering other data processors")
    data_stream.register_processor(text_processor)
    data_stream.register_processor(log_processor)

    print("Send the same batch again")
    data_stream.process_stream(first_batch)
    data_stream.print_processors_stats()

    print()
    print(
        "Consume some elements from the data processors: "
        "Numeric 3, Text 2, Log 1"
    )
    consume(numeric_processor, 3)
    consume(text_processor, 2)
    consume(log_processor, 1)

    data_stream.print_processors_stats()


if __name__ == "__main__":
    main()
