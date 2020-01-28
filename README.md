# Jobtimize
`Jobtimize` is a python package which collects, standardizes and completes information about job offers published on job search platforms.
The package is mainly based on scraping and text classification to fill in missing data.


|Release|Usage|Development|
|---	|---  |---	      |
|[![GitHub version](https://img.shields.io/badge/Version-Planning-orange?style=for-the-badge)](https://travis-ci.com/Lrakotoson/Jobtimize)|[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](https://opensource.org/licenses/MIT)|[![Build Status](https://img.shields.io/travis/com/Lrakotoson/Jobtimize/master.svg?style=for-the-badge&logo=Travis-CI&logoColor=white)](https://travis-ci.com/Lrakotoson/Jobtimize)|
|   	|[![Python version](https://img.shields.io/badge/Python-3-blue?style=for-the-badge&logo=python&logoColor=yellow)](https://www.python.org/)|[![Codecov](https://img.shields.io/codecov/c/gh/Lrakotoson/Jobtimize?logo=Codecov&style=for-the-badge)](https://codecov.io/gh/Lrakotoson/Jobtimize/)|
|   	|   	|[![Python](https://img.shields.io/badge/Made%20with-Python-blue?style=for-the-badge&logo=python&labelColor=yellow)](https://www.python.org/)|

# Dependencies

```
beautifulsoup4
jsonschema
lxml
numpy
pandas
```

# Installation
## Pypi
The safest way to install `Jobtimize` is to go through pip
```bash
pip install Jobtimize
```

## Git
The installation with git allows to have the latest version. However it can have some bugs.
```bash
pip install git+https://github.com/Lrakotoson/Jobtimize.git
```

# How to use ?
Since `Jobtimize` is a package, in python you just have to import it.
The main function (*for now*) is `Jobtimize.jobscrap`.
```python
from Jobtimize import jobscrap

df = jobscrap(["Data Scientist", "Data Analyst"],
              ["UK", "FR"]
    )

df.head()
```
The `df` object is a dataframe pandas, so it inherits all its methods.