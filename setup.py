from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in montego_app/__init__.py
from montego_app import __version__ as version

setup(
	name="montego_app",
	version=version,
	description="It a developing app",
	author="Montego-arch",
	author_email="mmanuelmiles@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
