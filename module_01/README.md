### Install documentation tools

Sphinx is only needed if you want to build the documentation locally.

On macOS with Homebrew:

```bash
brew install sphinx-doc
```
Alternatively using pipx:
```
pipx install sphinx
pipx inject sphinx sphinx-rtd-theme
```

If the Read the Docs theme is used, make sure sphinx-rtd-theme is installed.
But don’t overdo it. You do **not** need to explain what Sphinx is, how `conf.py` works, themes, autodoc, etc. That belongs in your learning notes, not the root README.

Cleaner final wording:

```markdown
## Documentation

Some modules may include Sphinx documentation for learning purposes.

To build the documentation locally, install Sphinx first:

```bash
brew install sphinx-doc
```

If using Read The Docs theme:
```
pipx install sphinx
pipx inject sphinx sphinx-rtd-theme
```

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
And you can see the documentation in a new window.

