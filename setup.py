#!/usr/bin/env python

from setuptools import setup

import vector

setup(
    name="vector",
    version=vector.__version__,
    url="https://github.com/ryanleland/Vector.py",
    packages = [
        'vector'
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
