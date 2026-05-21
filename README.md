<img src="./images/UCAM_ICCS_Logo.png"  width="600">

#  Green Software Engineering Practices

This repository contains documentation, resources, and code for the 'Green Software
Engineering Practices' session designed and delivered by Joe Wallwork
(@joewallwork), Surbhi Goel (@surbhigoel) and David Kamm (@vopikamm) of
[ICCS](https://github.com/Cambridge-ICCS).
All materials, including slides and videos, are available such that individuals
can cover the course in their own time.


## Contents

- [Learning Objectives](#learning-objectives)
- [Teaching material](#teaching-material)
- [Preparation and prerequisites](#preparation-and-prerequisites)
- [Installation and setup](#installation-and-setup)
- [License information](#license)
- [Contribution Guidelines and Support](#contribution-guidelines-and-support)


## Learning Objectives

The key learning objective from this workshop is to equip participants with
awareness and practical skills to measure, interpret, and reduce the carbon
footprint of research software.

Research software engineering activities inherently involve use of computational
resources. That is, programs run on computers, servers and other pieces of
hardware, which may be hosted on a machine in your office, in a HPC centre, or
in the cloud. Computational resource usage can be measured in terms of the
corresponding energy consumption and - with some additional data on electricity
generation - it’s possible to estimate the associated carbon emissions. Green
Computing is focused on measuring such computational resource usage and finding
ways to reduce it to lower the carbon footprint of your work. We will explain
and demonstrate several useful approaches and tools for good green software
engineering practices, including those related to

  -  Green computing for testing and debugging.
  -  Measuring the carbon emissions associated with HPC jobs.
  -  Green use of AI.

## Teaching Material

### Slides
TODO (right now google docs)

The slides for this workshop can be viewed here:
[Slides](https://docs.google.com/presentation/d/1msHjFMiHlV20jqhZVixFkhG3L0sDddPFQagMCMDyaII/edit?slide=id.p#slide=id.p)

### Exercises
The exercises for the course can be found in the [demos](demos/) directory.
These take the form of erroneous Python scripts for unit testing, designed to
demonstrate the practical use of `pytest --last-failed`.

### Worked Solutions
Worked solutions for all of the exercises can be found in the
[TODO](worked-solutions/) directory.
These are for recapping after the course in case you missed anything, and
contain example solutions.


## Preparation and prerequisites

### Prerequisites

To get the most out of the session we assume a basic understanding in a few
areas and for you to do some preparation in advance.
This expected knowledge is outlined below, along with resources for reading if
you are unfamiliar with any areas.

#### Python

The course uses some basic elements of Python and assumes some basic knowledge
of the ecosystem. This includes:

- use of a
  [python virtual environment](https://www.datasciencebase.com/fundamentals/python/environment-setup/)
- installation of dependencies
- running python scripts from the command line
- basic unit testing using
  [pytest](https://docs.pytest.org/en/stable/)

#### HPC
TODO?

### Preparation

In preparation for the course please ensure that your computer contains the
following:

- A text editor - e.g. vim/[neovim](https://neovim.io/),
  [gedit](https://gedit.en.softonic.com/),
  [vscode](https://code.visualstudio.com/),
  [sublimetext](https://www.sublimetext.com/) etc. to open and edit code files
- A terminal emulator - e.g.
  [GNOME Terminal](https://help.gnome.org/users/gnome-terminal/stable/),
  [wezterm](https://wezfurlong.org/wezterm/index.html),
  [Windows Terminal (windows only)](https://learn.microsoft.com/en-us/windows/terminal/),
  [iTerm (mac only)](https://iterm2.com/)
- A Python 3 installation

If you require assistance or further information with any of these please reach
out to us before the session.


## Installation and setup


### 1. Clone or fork the repository
Navigate to the location you want to install this repository on your system and
clone via https by running:
```
git clone https://github.com/Cambridge-ICCS/green-se-summer-school-2026.git
```
This will create a directory `green-se-summer-school-2026/` with the contents of this repository.

Please note that if you have a GitHub account and want to preserve any work you
do we suggest you first
[fork the repository](https://github.com/Cambridge-ICCS/green-se-summer-school-2026/fork)
and then clone your fork.
This will allow you to push your changes and progress from the workshop back up
to your fork for future reference.

### 2. Create a virtual environment
TODO

Before installing any Python packages it is important to first create a Python
virtual environment.
This provides an insulated environment inside which we can install Python
packages without polluting the operating system's Python environment.
```
python3 -m venv .venv
```
This will create a directory called `.venv/` containing software for the
virtual environment.
To activate the environment run:
```
source .venv/bin/activate
```
You can now work on python from within this isolated environment, installing
packages as you wish without disturbing your base system environment.

When you have finished working on this project run:
```
deactivate
```
to deactivate the venv and return to the system python environment.

You can always boot back into the venv as you left it by running the activate command again.

### 3. Install dependencies
TODO

It is now time to install the dependencies for our code, for example `pytest`.
The project has been packaged with a [`pyproject.toml`](pyproject.toml) so can
be installed in one go.
From within the root directory in a active virtual environment run:
```
pip install .
```
This will download the relevant dependencies into the venv as well as setting
up the datasets that we will be using in the course.

## License

The code materials in this project are licensed under the [MIT License](LICENSE).

The teaching materials are licensed under a
[Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License][cc-by-nc-sa].

[cc-by-nc-sa]: http://creativecommons.org/licenses/by-nc-sa/4.0/
[cc-by-nc-sa-image]: https://licensebuttons.net/l/by-nc-sa/4.0/88x31.png
[cc-by-nc-sa-shield]: https://img.shields.io/badge/License-CC%20BY--NC--SA%204.0-lightgrey.svg

[![CC BY-NC-SA 4.0][cc-by-nc-sa-image]][cc-by-nc-sa]

## Contribution Guidelines and Support

If you spot an issue with the materials please let us know by
[opening an issue](https://github.com/Cambridge-ICCS/green-se-summer-school-2026/issues/new)
here on GitHub clearly describing the problem.

If you are able to fix an issue that you spot, or an
[existing open issue](https://github.com/Cambridge-ICCS/green-se-summer-school-2026/issues),
please get in touch by commenting on the issue thread.

Contributions from the community are welcome.
To contribute back to the repository please first
[fork it](https://github.com/Cambridge-ICCS/green-se-summer-school-2026/fork),
make the necessary changes to fix the problem, and then open a pull request
back to this repository clearly describing the changes you have made.
We will then preform a review and merge once ready.

If you would like support using these materials, adapting them to your needs,
or delivering them please get in touch either via GitHub or via
[ICCS](https://github.com/Cambridge-ICCS).