# Module 00

This module contains the solutions for the Python fundamentals exercises.

## Structure

```text
module_00/
├── ex0/
├── ex1/
├── ex2/
├── ex3/
├── ex4/
├── ex5/
├── ex6/
├── ex7/
├── main.py
└── Makefile
```
The original solution files are kept inside the ex*/ folders.

## Using the Makefile

The provided `main.py` helper expects the exercise files to be available in the `module_00/` root directory.
To avoid copying them manually, the `Makefile` can copy the files from the exercise folders before running the tests. I have explained the rules in the Makefile in the **commands** section with other usefule commands.

### Commands

```make prepare```: Copies all Python files from the exercise folders to `module_00/` directory.

```make run```: Runs make prepare, then executes:```python main.py```<br>

```make lint```: Runs flake8 on the Python files inside the exercise folders.

```make check```: Runs both linting and testing.

```make clean```: Removes Python cache folders and copied root-level exercise files.

```make re```: Runs a clean check from scratch.

#### Important

If you want to play around and/or modify the files, do it inside the `ex*/` folders only. The copied files in the `module_00/` root are temporary and may be deleted by make clean.

