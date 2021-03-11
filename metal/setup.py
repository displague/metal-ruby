# coding: utf-8

import sys
from setuptools import setup, find_packages

NAME = "metal"
VERSION = "1.0.0"

# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = [
    "connexion>=2.0.2",
    "swagger-ui-bundle>=0.0.2",
    "python_dateutil>=2.6.0"
]

setup(
    name=NAME,
    version=VERSION,
    description="Metal API",
    author_email="support@equinixmetal.com",
    url="",
    keywords=["OpenAPI", "Metal API"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['openapi/openapi.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['metal=metal.__main__:main']},
    long_description="""\
    This is the API for Equinix Metal Product. Interact with your devices, user account, and projects.
    """
)

