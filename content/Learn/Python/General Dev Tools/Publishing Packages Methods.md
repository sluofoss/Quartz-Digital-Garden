---
title: Publishing Packages Methods
created: 2024-10-16T00:00
updated: 2024-10-16T00:26
---

# Publish Location
- PyPi
- anaconda

# Publishing procedure
- prior to publishing the project should undergo code linting and compilation. Of course all this can be done locally. but it's best to automate it using github workflow.
- some GitHub workflow actions that's worth looking include:
	- https://github.com/astral-sh/setup-uv
	- https://github.com/eifinger/setup-rye?tab=readme-ov-file
	- https://github.com/marketplace/actions/python-setup-rye
	- https://github.com/marketplace/actions/pypi-publish
The Official Github Actions has a workflow for Publishing Python Package. It uses the action `pypi-publish`. Inside which contains a reference to the following document
- https://docs.github.com/en/actions/use-cases-and-examples/building-and-testing/building-and-testing-python#publishing-to-package-registries
