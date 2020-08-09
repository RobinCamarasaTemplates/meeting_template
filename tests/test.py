"""
**Author** : Robin Camarasa

**Institution** : ErasmusMC

**Position** : PhD student

**Contact** : r.camarasa@erasmusmc.nl

**Date** : 2020-08-08

**Project** : meeting

**Test meeting project **

"""
import sys
import os
from datetime import datetime
import pytest
import shutil
from pathlib import Path
from cookiecutter import main
import subprocess


ROOT = Path(__file__).parents[1]
TESTS_ROOT = ROOT / 'test_output'
EXTRA_CONTEXT = {
    "meeting_type": "Test meeting",
    "meeting_date": "{% now 'utc', '%Y-%m-%d' %}",
    "meeting_hour": "{% now 'utc', '%H:%M' %}",
    "meeting_place": "Virtual",

    "presents": "John, Doe",

    "repo_name": "{{ cookiecutter.meeting_date }}-{{ cookiecutter.meeting_type.lower().replace(' ', '_') }}",


    "author_names": "John Doe, Doe John",
    "author_institutions": "Lambda company, Omega company",

    "author_name": "John Doe",
    "author_mail": "john.doe@lambda.com",
    "author_github": "https://github.com/JohnDoe",
    "author_scholar": "https://google.scholar",
    "author_website": "https://johndoe.github.io"
}


def test_generate_project() -> None:
    """
    Test project generation

    :return: None
    """
    # Clean
    if TESTS_ROOT.exists():
        shutil.rmtree(TESTS_ROOT)
    TESTS_ROOT.mkdir()

    # Get path
    output_dir = TESTS_ROOT.resolve()

    # Launch project generation
    main.cookiecutter(
        str(ROOT),
        no_input=True,
        extra_context=EXTRA_CONTEXT,
        output_dir=output_dir
    )

    # Test project generation
    repo_name = '{}-{}'.format(
        datetime.now().strftime('%Y-%m-%d'),
        EXTRA_CONTEXT['meeting_type'].lower().replace(' ', '_')
    )
    assert (TESTS_ROOT / repo_name).exists()
    assert (TESTS_ROOT / repo_name / 'README.md').exists()
    assert (TESTS_ROOT / repo_name / '.gitignore').exists()
    files = [
        'commands.sty',
        'images',
        'presentation.tex',
        'theme.sty',
    ]
    for file_ in files:
        assert (
            TESTS_ROOT / repo_name / 'presentation' / file_
        ).exists()

    process = subprocess.Popen(
        ['pdflatex', 'presentation.tex'],
        cwd= (TESTS_ROOT / repo_name / 'presentation').resolve()
    )
    process.wait()
    assert process.returncode == 0

