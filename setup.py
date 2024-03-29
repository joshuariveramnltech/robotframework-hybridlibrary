import re
from os.path import abspath, dirname, join
from setuptools import setup, find_packages


CURDIR = dirname(abspath(__file__))

CLASSIFIERS = '''
Development Status :: 5 - Production/Stable
License :: OSI Approved :: Apache Software License
Operating System :: OS Independent
Programming Language :: Python
Programming Language :: Python :: 3
Topic :: Software Development :: Testing
Framework :: Robot Framework
Framework :: Robot Framework :: Library
'''.strip().splitlines()
with open(join(CURDIR, 'src', 'HybridLibrary', '__init__.py')) as f:
    VERSION = re.search("\n__version__ = '(.*)'", f.read()).group(1)
with open(join(CURDIR, 'README.rst')) as f:
    DESCRIPTION = f.read()
with open(join(CURDIR, 'requirements.txt')) as f:
    REQUIREMENTS = f.read().splitlines()
with open(join(CURDIR, 'LICENSE')) as f:
    LICENSE = f.read()

setup(
    name             = 'robotframework-hybridlibrary',
    version          = VERSION,
    description      = 'Robot Framework Libray for automating using appium API',
    long_description = DESCRIPTION,
    author           = 'Joshua Kim Rivera',
    author_email     = 'joshuakimrivera@gmail.com',
    url              = 'https://github.com/robotframework/SeleniumLibrary',
    license          = LICENSE,
    keywords         = 'robotframework testing testautomation selenium webdriver web',
    platforms        = 'any',
    classifiers      = CLASSIFIERS,
    python_requires  = '>=2.7.*, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*, !=3.4.*, <4',
    install_requires = REQUIREMENTS,
    package_dir      = {'': 'src'},
    packages         = find_packages('src')
)