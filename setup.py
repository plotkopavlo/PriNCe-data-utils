# -*- coding: utf-8 -*-
import sys
from distutils.core import setup
from os.path import abspath, dirname, join

import setuptools

def get_version():
    version = {}
    with open("prince_analysis_tools/version.py") as fp:
        exec (fp.read(), version)
    return version['__version__']

__version__ = get_version()

this_directory = abspath(dirname(__file__))
if sys.version_info.major == 3:
    with open(join(this_directory, 'README.md'), encoding='utf-8') as f:
        long_description = f.read()
else:
    with open(join(this_directory, 'README.md')) as f:
        long_description = f.read()

skip_marker = "# PriNCe-data-utils"
long_description = long_description[long_description.index(skip_marker) :].lstrip()

setup(
    name='prince_data_utils',
    version=__version__,
    author='Jonas Heinze, Anatoli Fedynitch',
    author_email='jonas.heinze@gmail.com',
    description='Data tables and utilities to construct the database file for PriNCe',
    long_description=long_description,
    long_description_content_type='text/markdown',
    license='BSD 3-Clause License',
    url='https://github.com/joheinze/PriNCe-data-utils',
    packages=[
        'prince_data_utils'
    ],
    install_requires=[
        # 'six',
        'iminuit',
        'scipy',
        'numpy',
        'tqdm',
        'requests',
        'pandas',
        'h5py'
        'six',
        'particletools',
    ],
    tests_require=['pytest','matplotlib'],
    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Topic :: Scientific/Engineering :: Physics',
        'Intended Audience :: Science/Research',
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: BSD License'
    ]
)
