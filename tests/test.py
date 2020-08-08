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
    "repo_name": "repo",
    "description": "Description",

    "author_name": "John Doe",
    "author_position": "Intern",
    "author_github": "https://github.com/JohnDoe"
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
    project_name = EXTRA_CONTEXT['repo_name']
    assert (TESTS_ROOT / project_name).exists()
