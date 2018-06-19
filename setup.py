# -*- coding: utf-8 -*-
import sys
from os.path import join, dirname
from setuptools import setup, find_packages

VERSION = (6, 0, 0, 'dev')
__version__ = VERSION
__versionstr__ = '.'.join(map(str, VERSION))

f = open(join(dirname(__file__), 'README.md'))
long_description = f.read().strip()
f.close()

install_requires = [
    'elasticsearch-async>=5.0.0,<6.2.0',
    'elasticsearch-dsl>=5.0.0,<6.2.0',
]

if sys.version_info[:2] < (3, 4):
    install_requires.append('asyncio')

setup(
    name="elasticsearch-dsl-async",
    description="Async search for elasticsearch-dsl",
    license="Apache License, Version 2.0",
    url="https://github.com/VladimirKuzmin/elasticsearch-dsl-py-async",
    long_description=long_description,
    version=__versionstr__,
    author="Vladimir Kuzmin",
    author_email="Vladimir.A.Kuzmin@gmail.com",
    packages=find_packages(
        where='.',
    ),
    classifiers=[
        "License :: OSI Approved :: Apache Software License",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: Implementation :: CPython",
    ],
    install_requires=install_requires,
)
