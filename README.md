<img src="images/ICCS_logo.png"  width="355" align="left">

<br><br><br><br><br><br><br>

# Green Software Engineering Practices

![GitHub](https://img.shields.io/github/license/Cambridge-ICCS/green-se-summer-school-2026)

*This course is currently under development for the
[2026 Summer School](https://iccs.cam.ac.uk/events/institute-computing-climate-science-annual-summer-school-2026)
of the
[Institute of Computing for Climate Science (ICCS)](https://iccs.cam.ac.uk) by
[Joe Wallwork](https://joewallwork.com),
[Surbhi Goel](https://github.com/surbhigoel77), and
[David Kamm](https://github.com/vopikamm)*

## Setup

The course will involve some Python examples. To manage the dependencies, first
create a Python virtual environment and then activate it. For example:
```sh
python3 -m venv green-se
source green-se/bin/activate
```
Having done so, install the Python dependencies in the
[requirements.txt](requirements.txt) file with
```sh
pip install -r requirements.txt
```
This will install [CodeCarbon](https://codecarbon.io/), the
[Carbon Aware Task Scheduler (CATS)](https://cats.readthedocs.io), and
additional packages to support plotting with CATS.
