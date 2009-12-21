from setuptools import setup, find_packages
import sys, os

version = '0.0.1'

setup(name='chicanery',
      version=version,
      description="duplicity wrapper",
      long_description="""""",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='duplicity backup sysadmin',
      author='Rob Weir',
      author_email='rweir@ertius.org',
      url='http://ertius.org/code/chicanery/',
      license='GNU GPL v2',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=True,
      install_requires=[
        'argparse',
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
