"""A setuptools based setup module.
See:
https://packaging.python.org/en/latest/distributing.html
https://github.com/pypa/sampleproject
"""

from setuptools import setup, find_packages
# To use a consistent encoding
from codecs import open


def read_requirements():
    with open("requirements.txt", "r") as f:
        lines = f.readlines()
        lines = [line.strip("\n") for line in lines]
        return lines


setup(
    name="oshe",

    version="0.0.1.dev1",

    description="A sample Python web crawler",

    # The project"s main homepage.
    url="https://github.com/imhuwq/oshe",

    # Author details
    author="imhuwq",
    author_email="imhuwq@gmail.com",

    # Choose your license
    license="MIT",

    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",

        "Environment :: Console"

        "Intended Audience :: Developers",

        "Topic :: Web :: Crawler",

        "License :: OSI Approved :: MIT License",

        "Programming Language :: Python :: 3.5",
    ],

    # What does your project relate to?
    keywords="web crawler",

    # You can just specify the packages manually here if your project is
    # simple. Or you can use find_packages().
    packages=find_packages(),

    install_requires=read_requirements(),

    # To provide executable scripts, use entry points in preference to the
    # "scripts" keyword. Entry points provide cross-platform support and allow
    # pip to create the appropriate form of executable for the target platform.
    entry_points={
        "console_scripts": [
            "oshe=oshe.oshe:oshe",
        ],
    },
)
