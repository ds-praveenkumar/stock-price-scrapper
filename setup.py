# github link: https://github.com/ds-praveenkumar/kaggle
# Author: ds-praveenkumar
# file: personal-project/setup.py/
# Created by ds-praveenkumar at 09-06-2020 22 42
# feature:

from setuptools import setup,find_packages

setup(
    name = 'personal-project-env',
    version='0.1.0',
    licence='MIT',
    description='project for personal interest',
    packages=find_packages('bulls-run.src','bulls-run'),
    install_requires=[
        'requests',
        'beautifulsoup4',
    ],
)