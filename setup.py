#!/usr/bin/env python

import setuptools
import sys

dependencies = [
    'requests >= 2.0.0',
    'guzzle_sphinx_theme',
]

if sys.version_info < (3, 4):
    dependencies.append('enum34')

with open('PYPI_DESCRIPTION.rst') as file:
    long_description = file.read()

setuptools.setup(
    name='freelancersdk',
    author='Freelancer.com',
    url='https://github.com/freelancer/freelancer-sdk-python',
    author_email='api-support@freelancer.com',
    version='0.1.13',
    description='Offical Freelancer.com SDK',
    long_description=long_description,
    classifiers=[
        "Development Status :: 4 - Beta",
        "Topic :: Software Development",
        "License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)",
        'Operating System :: OS Independent',
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: Implementation :: CPython",
    ],
    packages=setuptools.find_packages(),
    install_requires=dependencies,
)
