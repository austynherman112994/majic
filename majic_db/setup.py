#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
    'psycopg2-binary'
]

test_requirements = ['pytest>=3', ]

setup(
    author="Austyn Herman",
    author_email='austynherman112994@gmail.coom',
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="Python Boilerplate contains all the boilerplate you need to create a Python package.",
    install_requires=requirements,
    license="Apache Software License 2.0",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='majic_db',
    name='majic_db',
    packages=find_packages(include=['majic_db', 'majic_db.*']),
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/austynherman112994/majic_db',
    version='0.0.0',
    zip_safe=False,
)
