#!/usr/bin/env python

from setuptools import setup

import linear

setup(
    name="linear",
    version=linear.__version__,
    url="https://github.com/ryanleland/Vector.py",
    packages = [
        'linear'
    ],
    package_data={'': ['LICENSE']},
    include_package_data=True,
    license=open("LICENSE").read(),
    classifiers=(
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
    )
)
