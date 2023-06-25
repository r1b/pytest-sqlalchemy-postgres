#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup


setup(
    name="pytest-sqlalchemy-postgres",
    version="1.0.0",
    author="Robert Jensen",
    author_email="robert.cole.jensen@gmail.com",
    license="BSD-3",
    url="https://github.com/r1b/pytest-sqlalchemy-postgres",
    description="Pytest plugin for testing Postgres with a SQLAlchemy session. Uses savepoints to isolate tests.",
    py_modules=["pytest_sqlalchemy_postgres"],
    python_requires=">=3.8",
    install_requires=["pytest", "sqlalchemy"],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Framework :: Pytest",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Testing",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: Implementation :: CPython",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: BSD License",
    ],
    entry_points={
        "pytest11": [
            "pytest-sqlalchemy-postgres = pytest_sqlalchemy_postgres",
        ],
    },
)
