from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='gum',
    version='1.0.0',
    packages=find_packages(exclude=[]),
    install_requires=[],

    entry_points={
        'console_scripts': [
            'upc2color=gum.tools.upc2color:main',
        ],
    },

    description='Mini product library for chewing gum related demo',
    long_description=long_description,
    url='https://github.com/jonemo/gum',
    author='Jonas Neubert',
    author_email='jn@jonasneubert.com',
    license='MIT',

    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',
    ],
)
