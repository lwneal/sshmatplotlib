#!/usr/bin/env python

from setuptools import setup

setup(name='sshmatplotlib',
    version='0.1.0',
    description='Automatically sets matplotlib backend based on $DISPLAY',
    author='Larry Neal',
    author_email='nealla@lwneal.com',
    url='https://github.com/lwneal/sshmatplotlib',
    packages=[
        'sshmatplotlib',
    ],
    install_requires=[
        "matplotlib",
    ],
)
