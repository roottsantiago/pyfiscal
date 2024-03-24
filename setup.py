from pathlib import Path
from setuptools import setup

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()


VERSION = '2.1'
DESCRIPTION = 'Pyfiscal calculation of tax data.'
PACKAGE_NAME = 'pyfiscal'
AUTHOR = 'Tomás Santiago'
EMAIL = 'thom.sgonzalez@gmail.com'
GITHUB_URL = 'https://github.com/roottsantiago/pyfiscal'


setup(
    name = PACKAGE_NAME,
    packages = [PACKAGE_NAME],
    version = VERSION,
    license='MIT',
    description = DESCRIPTION,
    long_description_content_type = "text/markdown",
    long_description = long_description,
    author = AUTHOR,
    author_email = EMAIL,
    url = GITHUB_URL,
    keywords = [
        'RFC',
        'CURP',
        'NSS',
        'fiscal',
        'tax',
        'SAT'
    ],
    classifiers = [
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
)
