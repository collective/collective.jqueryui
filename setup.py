from setuptools import setup, find_packages
import os

version = '1.8.20'

setup(name='collective.jqueryui',
      version=version,
      description="jQuery UI integration for Plone",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from http://www.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
      keywords='plone jquery jqueryui',
      author='Rok Garbas and contributors',
      author_email='rok.garbas@gmail.com',
      url='http://pypi.python.org/pypi/collective.jqueryui',
      license='MIT',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['collective'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'plone.app.jquery>1.7'
      ],
      entry_points="""
          [z3c.autoinclude.plugin]
          target = plone
      """,
      )
