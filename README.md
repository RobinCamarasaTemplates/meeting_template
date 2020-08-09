# Meeting template

Cookiecutter project to generate meeting notes and latex presentation for the meeting.

## Requirements
 - Python 2.7 or 3.5
 - [Cookiecutter Python package](http://cookiecutter.readthedocs.org/en/latest/installation.html) >= 1.4.0: This can be installed with pip by or conda depending on how you manage your Python packages:

``` bash
$ pip install cookiecutter
```

or

``` bash
$ conda config --add channels conda-forge
$ conda install cookiecutter
```


## To start a new meeting, run
``` bash
$ cookiecutter https://github.com/RobinCamarasaTemplates/meeting_template
```

## To contribute
- Clone the repository
``` bash
$ cookiecutter https://github.com/RobinCamarasaTemplates/meeting_template
```
- Install the requirement
```bash
$ pip install -r requirements.txt
```
- Modify the project
- Make sure that your modification works
```bash
$ pytest tests/test.py
```

## Authors
The following authors contributed :
- [Robin Camarasa](https://github.com/RobinCamarasa)
