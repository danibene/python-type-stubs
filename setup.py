"""Package setup"""
from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="scikit-learn-stubs",
    version="0.1.0",
    url="https://github.com/microsoft/python-type-stubs",
    author="microsoft",
    description="A set of type stubs for popular Python packages.",
    license="MIT License",
    long_description=long_description,
    long_description_content_type="text/markdown",
    package_data={
        "stubs/sklearn": ["*.pyi", "**/*.pyi", "**/**/*.pyi", "**/**/**/*.pyi"],
    },
    packages=[
        "stubs/sklearn",
    ],
    python_requires=">=3.8",
    zip_safe=False,
)