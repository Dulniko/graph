from setuptools import setup, find_packages

NAME = "Flatland"

CONFIG = {
    "name": NAME,
    "version": "0.1",
    "packages": find_packages(),
}

setup(**CONFIG)
