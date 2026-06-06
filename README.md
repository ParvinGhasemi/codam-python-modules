# codam-python-modules
My solutions for Codam Python modules. Python learning modules completed at Codam, covering fundamentals, object-oriented programming(OOP), exceptions, collections, file handling, and polymorphic data pipelines.

## Structure

```text
module_00/
module_01/
module_02/
module_03/
module_04/
module_05/
module_06/
module_07/
module_08/
module_09/
module_10/
subjects/
```

Each `module_xx/` folder contains the exercises for that module.

The `subjects/` folder contains the assignment PDFs for reference only.

### Requirements
* Python 3.10+
* flake8
* mypy

### Code checks
Run these commands from the repository root:
```Bash
flake8 .
mypy .
mypy --strict .
```

For a single module:
```
cd module_01
flake8 .
mypy .
```

### Documentation
Some modules may include Sphinx documentation for my own learning purposes. (it is not required by the instructions from codam).

Currently, module_01 includes a basic Sphinx documentation setup to practice writing and generating project documentation.

### <ins>Build Module 01 documentation</ins>


From the repository root:
```
cd module_01/docs
make html
```
Then open the generated HTML file.

On macOS:
```
open build/html/index.html
```
On Linux:
```
xdg-open build/html/index.html
```
or if it didn't work, use a browser directly instead; try one of these on Linux:
```
google-chrome build/html/index.html
or
```
firefox build/html/index.html
```
or:
```
chromium build/html/index.html
```

if the `open` command didn't work, you can also try the below commands - copy & paste all 3 lines together to your terminal in one go:
```
cd ~/Documents/codam/python_modules/module_01/docs
~/.local/bin/sphinx-build -b html source build/html
open build/html/index.html
```

#### <ins>Documentation files</ins>

The documentation source files are stored in: `module_01/docs/source/`

The generated HTML files are created in: `module_01/docs/build/`

## License

My own solution code in this repository is licensed under the MIT License.

The PDF subject files and any school-provided materials are included only for reference/context and remain the property of their respective authors/owners. They are not covered by the MIT License.




