# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

try:
    long_description = open("README.rst").read()
except IOError:
    long_description = ""

setup(
    name="pip+AZON",
    version="0.1.0",
    description="Nikita Stepanenko pip package",
    author="Nikita Stepanenko",
    author_email='241379@student.pwr.edu.pl',
    packages=find_packages(),
    install_requires=['requests', 'json'],
    long_description=long_description,
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.8",
    ]
)
