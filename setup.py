from setuptools import setup, find_packages
from os import path

from io import open

here = path.abspath(path.dirname(__file__))

with open(path.join(here, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="mkdocs-user-defined-values",
    version="0.0.3",
    description="Enable user defined values for MkDocs",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/rahult/mkdocs-user-defined-values",
    author="Rahul Trikha",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Build Tools",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
    ],
    keywords="mkdocs plugin user defined value",
    packages=find_packages(exclude=["contrib", "docs", "tests"]),
    python_requires=">=3, <4",
    install_requires=[
        "mkdocs>=1.0.4"
    ],
    extras_require={"dev": []},
    dependency_links=[],
    entry_points={
        "mkdocs.plugins": ["user-defined-values = plugin.plugin:UserDefinedValues",]
    },
    project_urls={
        "Bug Reports": "https://github.com/rahult/mkdocs-user-defined-values/issues",
        "Source": "https://github.com/rahult/mkdocs-user-defined-values/",
    },
)
