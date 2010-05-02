import os
from setuptools import setup, find_packages

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "python-bidi",
    version = "0.1",
    url = 'http://github.com/mksoft/python-bidi',
    license = 'LGPL',
    description = "BIDI related functions",
    long_description = read('README.rst') + read('CHANGELOG.rst'),

    author = 'Meir Kriheli',
    author_email = 'meir@mksoft.co.il',

    packages = find_packages('src'),
    package_dir = {'': 'src'},
    include_package_data = True,

    install_requires = ['setuptools'],

    classifiers = [
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: GNU Library or Lesser General Public License (LGPL)',
        'Programming Language :: Python',
        'Topic :: Text Processing',
    ]
)