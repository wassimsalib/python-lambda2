#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys

from setuptools import find_packages
from setuptools import setup

with open('README.rst') as readme_file:
    readme = readme_file.read()

requirements = [
    'boto3',
    'click',
    'PyYAML',
]

# Only install futures package if using a Python version <= 2.7
if sys.version_info < (3, 0):
    requirements.append('futures')

test_requirements = [
    # TODO: put package test requirements here
]

setup(
    name='python-lambda2',
    version='3.3.1',
    description='The bare minimum for a Python app running on Amazon Lambda.',
    long_description=readme,
    long_description_content_type='text/x-rst',
    author='Wassim Salib',
    author_email='wassim87@gmail.com',
    url='https://github.com/wassimsalib/python-lambda2',
    packages=find_packages(),
    package_data={
        'aws_lambda': ['project_templates/*'],
        '': ['*.json'],
    },
    include_package_data=True,
    scripts=['scripts/lambda'],
    install_requires=requirements,
    license='ISCL',
    zip_safe=False,
    keywords='python-lambda2',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: ISC License (ISCL)',
        'Natural Language :: English',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    test_suite='tests',
    tests_require=test_requirements,
)
