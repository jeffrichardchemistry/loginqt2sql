# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open("README.md", 'r') as fr:
	description = fr.read()

setup(
    name='loginqt2sql',
    version='1.0.0',
    url='https://github.com/jeffrichardchemistry/loginqt2sql',
    license='GNU General Public License v3.0',
    author='Jefferson Richard',
    author_email='jrichardquimica@gmail.com',
    keywords='Login Register Qt Python',
    description='Simples sistema de login/registro integrado ao banco de dados SQLite3',
	long_description = description,
	long_description_content_type = "text/markdown",
	include_package_data = True,
	scripts=['scripts/loginqt2sql'],
    packages=['loginqt2sql'],
    install_requires=['PyQt5'],
	classifiers = [
		'Environment :: X11 Applications :: Qt',
		'Intended Audience :: Developers',
		'Intended Audience :: End Users/Desktop',
		'Intended Audience :: Science/Research',
		'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
		'Natural Language :: English',
		'Operating System :: POSIX :: Linux',
		'Operating System :: Microsoft :: Windows',
		'Operating System :: MacOS',
		'Programming Language :: Python',
		'Programming Language :: Python :: 3',
		'Programming Language :: Python :: 3.6',
		'Programming Language :: Python :: 3.7',
		'Programming Language :: Python :: 3.8']
)
