from setuptools import setup, find_packages
import sys, os
import subprocess
import glob

version_py = os.path.join(os.path.dirname(__file__), 'version.py')
with open(version_py, 'r') as fh:
    version = open(version_py).read().strip().split('=')[-1].replace('"','')

try:
    with open("requirements.txt", "r") as f:
        install_requires = [x.strip() for x in f.readlines()]
except IOError:
        install_requires = [
          "flask",
          "pytest"]


setup(name='Gaffophone',
      version=version,
      description="Reddit bot to post stuff to /r/france",
      classifiers=[
	"Development Status :: 4 - Beta",
	"Environment :: Web Environment",
    "License :: OSI Approved :: MIT License",
	"Operating System :: POSIX :: Linux",
	"Programming Language :: Python"
	],
      keywords='reddit /r/france',
      author='Denis Moreno',
      author_email='milui.galithil@gmail.com',
      maintainer='Denis Moreno',
      maintainer_email='denis.moreno@scilifelab.se',
      url='https://github.com/Galithil/Gaffophone',
      license='MIT',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      scripts=glob.glob("scripts/*.py"),
      include_package_data=True,
      zip_safe=False,
      install_requires=install_requires,
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
