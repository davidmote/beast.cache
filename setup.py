from setuptools import setup, find_packages
import os

version = '0.1.2'

setup(name='beast.cache',
      version=version,
      description="",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from
      # http://pypi.python.org/pypi?:action=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        ],
      keywords='',
      author='',
      author_email='',
      url='http://svn.plone.org/svn/collective/',
      license='GPL',
      packages=find_packages('src', exclude=['ez_setup']),
      package_dir={'':'src'},
      namespace_packages=['beast'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'python-memcached',
          # -*- Extra requirements: -*-
      ],
      
    extras_require=dict(
        test=['plone.app.testing'],
        ),
      entry_points="""
      # -*- Entry points: -*-

      [z3c.autoinclude.plugin]
      target = plone
      """,
      )
