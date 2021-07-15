from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in beneficiary_sys/__init__.py
from beneficiary_sys import __version__ as version

setup(
	name='beneficiary_sys',
	version=version,
	description='beneficiary system',
	author='s97',
	author_email='s97@gmail.com',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
