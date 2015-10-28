#!/usr/bin/env python

import setuptools
import os
import sys

dependencies = ['requests >= 2.0.0']
if sys.version_info < (3, 4):
    dependencies.append('enum34')

setuptools.setup(
    name='freelancersdk',
    author='Freelancer.com',
    url='https://github.com/freelancer/freelancer-sdk-python',
    author_email='sdk@freelancer.com',
    version='0.1.2',
    description='Freelancer.com SDK',
    long_description='Freelancer.com SDK',
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Software Development",
        "License :: OSI Approved :: BSD License",
        'Operating System :: OS Independent',
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: Implementation :: CPython",
    ],
    packages=setuptools.find_packages(),
    install_requires=dependencies,
)
