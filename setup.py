import io
import os
from setuptools import setup

__version__ = '0.3'
__author__ = 'Fernando de Assis Rodrigues'

description = 'Attini Automation Script - Client Side - Raspberry'
here = os.path.abspath(os.path.dirname(__file__))

# load requirements
with open("requirements.txt") as f:
    dependencies = f.read().splitlines()

# load README
with io.open(os.path.join(here, "README.md"), encoding="utf-8") as doc_file:
    documentation = '\n' + doc_file.read()



setup(
    name='attini',
    version=__version__,
    description=description,
    long_description=documentation,
    author=__author__,
    author_email='fernando@rodrigues.pro.br',
    maintainer="Fernando de Assis Rodrigues at dadosabertos.info",
    url='http://dadosabertos.info/projects/attini',
    download_url="unavaliable",
    project_urls={"GUI": "http://dadosabertos.info/projects/attini",
                  "How Tos": "unavaliable",
                  "Examples": "unavaliable"},
    packages=['attini'],
    py_modules='attini',
    license="GPLv3",
    keywords=["attini", "automation", "bot"],
    classifiers=["Development Status :: 5 - Production/Stable",
                 "Environment :: Console",
                 "Environment :: Web Environment",
                 "Intended Audience :: End Users/Desktop",
                 "Intended Audience :: Developers",
                 "License :: OSI Approved :: GNU General Public License v3",
                 "Operating System :: POSIX :: Linux",
                 "Operating System :: Unix",
                 "Programming Language :: PHP",
                 "Programming Language :: Python",
                 "Programming Language :: JavaScript",
                 "Programming Language :: SQL",
                 "Topic :: Internet :: Browsers",
                 "Topic :: Utilities",
                 "Natural Language :: Portuguese"],
    install_requires=dependencies,
    include_package_data=True,
    python_requires=">=3.5",
    platforms=[ "linux", "linux2"]
)
