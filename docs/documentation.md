# Documentation

Documentation for all projects under MARSH-Sim.

All sources for these pages are in a [GitHub repository](https://github.com/marsh-sim/marsh-sim.github.io). It is set up to automatically build the documentation on every commit on GitHub servers. The public version at [marsh-sim.github.io](https://marsh-sim.github.io/) is updated every time the `main` branch is changed, the actual files served are from `gh-pages`.

## Local installation

The pages can be built into HTML and other formats using Python. A virtual environment is recommended to avoid mixing this documentation with system packages.

The following commands can be used for Linux:

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

For users on Windows, only the line to activate the virtual environment changes to:

```ps1
./venv/Scripts/activate
```

## Usage

Once a local installation is complete, the pages can be re-built live with:

```bash
mkdocs serve
```

## Contributing

Content is written in Markdown and built to HTML with [MkDocs](https://www.mkdocs.org/). Markdown files should preferably be formatted with [markdownlint extension for VS Code](https://marketplace.visualstudio.com/items?itemName=DavidAnson.vscode-markdownlint).

### MAVLink

The pages in the "MAVLink Definitions" section contain an initial part written normally, which is followed by automatically generated tables.
The tables are (re-)generated with the `update_mavlink_tables.py` Python script, which should do the complete process of getting the definitions, running the original generator used for MAVLink documentation, and then replacing a relevant part of the pages.
This script will be run when publicly deploying updates of the `main` branch.
The generated content of the files in this repository should be commited when there are significant changes in the dialect, for convenience of offline development and reference.

### Bibliography

The first paragraph under headings that match citation keys are replaced by citation generated using [Pybtex](https://pybtex.org/) in `update_bibliography.py` Python script.
They can be linked to from other documents [like this](./bibliography.md#padfieldhelicopterflightdynamics2018): `[like this](./bibliography.md#padfieldhelicopterflightdynamics2018)`.
Note that the key after `#` is all lowercase.

Subsequent paragraphs can be used for commentary how the document is relevant.

The preferred tool for formatting BibTeX source is [Zotero](https://www.zotero.org/) with the [Better BibTeX plugin](https://retorque.re/zotero-better-bibtex/).
After selecting the desired items in Zotero, right click and choose "Better BibTeX" -> "Copy BibTeX to clipboard".
Then paste them into [bibliography.bib](./bibliography.bib).

### Recommended resources

- [Make a Readme](https://www.makeareadme.com/)
- [Readme Driven Development](https://tom.preston-werner.com/2010/08/23/readme-driven-development.html)
- [More Software Projects need Defenses of Design](https://buttondown.email/hillelwayne/archive/more-software-projects-need-defenses-of-design/)

### Defense of Design

The goal for this setup of the documentation was to make it simple to update to users who come from aerospace engineering background and may not be familiar with the web technologies at large. A single documentation for all related projects was chosen to simplify navigation, allow easier cross linking between different concepts, and make it easier to search.

The web pages are generated with MkDocs, because it uses Python which most colleagues already know. The alternatives used by related projects like GitBook (for MAVLink Dev Guide) are not free anymore, and VuePress (for PX4) requires NodeJS. Initially the more popular Sphinx was chosen, but didn't play nicely with Markdown files. This was deemed more important, since we already use it for a README.md file in every repository, is much more popular than reStructured Text, and has simpler syntax.

Hosting the page through GitHub Pages and building through GitHub Actions mean there are no dedicated servers needed to be maintained by users. A fully open-source solution independent of a specific for-profit company would be preferred, but at least this can serve as introduction to contributing to other software outside of the University.

An early goal for documentation of the dialect was to provide a user experience very close to using the standard messages. The files for MAVLink definitions are re-generated every time the page is published, but can also be updated in the repository. This was chosen to keep the repository simple (no submodules), and always up to date with the newest definitions in the fork. The generated content isn't ignored by git, so the results are the same when working with the repository offline.

## License

Content in this documentation is licensed under [Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/)
