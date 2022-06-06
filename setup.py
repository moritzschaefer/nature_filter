#!/usr/bin/env python

"""The setup script."""

from setuptools import find_packages, setup

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = ['Click>=7.0', 'feedparser>=6.0.0', 'Flask>=2.0.0', 'requests>=2.0.0', 'feedgen>=0.9.0']

test_requirements = [ ]

setup(
    author="Moritz Schaefer",
    author_email='mail@moritzs.de',
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="Filtering nature RSS feed for scientific articles",
    entry_points={
        'console_scripts': [
            'nature_filter=nature_filter.cli:main',
        ],
    },
    install_requires=requirements,
    license="MIT license",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='nature_filter',
    name='nature_filter',
    packages=find_packages(include=['nature_filter', 'nature_filter.*']),
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/moritzschaefer/nature_filter',
    version='0.1.1',
    zip_safe=False,
)
