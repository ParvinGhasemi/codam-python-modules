PYTHON = python
FLAKE8 = python -m flake8

FILES = $(wildcard ex*/*.py)

prepare:
	@cp $(FILES) .

run: prepare
	$(PYTHON) main.py

lint:
	$(FLAKE8) $(FILES)

check: lint run

clean:
	rm -rf __pycache__ ex*/__pycache__
	rm -f ft_*.py

re: clean check

.PHONY: prepare run lint check clean re
