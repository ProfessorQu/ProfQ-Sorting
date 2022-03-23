# sourcery skip: path-read
from setuptools import setup, find_packages

VERSION = '0.0.1'
DESCRIPTION = 'A library for sorting algorithms.'

with open("README.md") as f:
    LONG_DESCRIPTION = f.read()

# Setting up
setup(
    name="profq-sorting",
    version=VERSION,
    author="ProfessorQu",
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    keywords=['python', 'sorting', 'algorithms'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Microsoft :: Windows",
    ]
)