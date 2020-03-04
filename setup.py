from __future__ import absolute_import
from __future__ import unicode_literals

import os

from setuptools import setup, find_packages

try:
    with open('README.md') as f:
        readme = f.read()
except IOError:
    readme = ''


def _requires_from_file(filename):
    return open(filename).read().splitlines()


setup(
    name="cuitools",
    version="1.0.0",
    url='https://github.com/kumitatepazuru/cuitools',
    author='kumitatepazuru',
    author_email='teltelboya18@gmail.com',
    maintainer='kumitatepazuru',
    maintainer_email='teltelboya18@gmail.com',
    description='Provides CUI drawing support libraries.',
    long_description=readme,
    packages=find_packages(),
    install_requires=_requires_from_file('requirements.txt'),
    license="MIT",
    classifiers=[
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'License :: OSI Approved :: MIT License',
    ],
    entry_points="""
      # -*- Entry points: -*-
      [console_scripts]
      pkgdep = pypipkg.scripts.command:main
    """,
)
