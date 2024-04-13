#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
    'flask',
]

test_requirements = ['pytest>=3', ]

setup(
    author="Austyn Herman",
    author_email='austynherman112994@gmail.com',
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
    description="Scheduling and orchestration management framework.",
    install_requires=requirements,
    license="Apache Software License 2.0",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='majic',
    name='majic',
    packages=find_packages(include=['majic', 'majic.*']),
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/austynherman112994/majic',
    version='0.0.0',
    zip_safe=False,
)
