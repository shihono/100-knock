# -*- coding : utf-8 -*-
from setuptools import setup, find_packages

install_requires = [
    'cython',
    'numpy',
    'scipy',
    'scikit-learn',
    'matplotlib',
    'pandas',
    'pydot',
    'lxml',
    'natto-py',
    'redis',
    'pycountry',
    'tqdm',
    'gensim',
]


setup(
    name='100-knock',
    version='0.0.1',
    description='Language Processing 100 knock code',
    author='Hono Shirai',
    author_email='',
    install_requires=install_requires,
    url='https://github.com/shihono/100-knock',
    # license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)

