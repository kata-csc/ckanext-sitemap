from setuptools import setup, find_packages
import sys, os

version = '0.1.3'

setup(
	name='ckanext-sitemap',
	version=version,
	description="Sitemap extension for CKAN",
	long_description="""\
	""",
	classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
	keywords='',
	author='CSC - IT Center for Science Ltd.',
	author_email='kata-project@postit.csc.fi',
	url='https://github.com/kata-csc/ckanext-sitemap',
	license='AGPL',
	packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
	namespace_packages=['ckanext', 'ckanext.sitemap'],
	include_package_data=True,
	zip_safe=False,
	setup_requires=[
		'nose'
	],
	entry_points=\
	"""
        [ckan.plugins]
	# Add plugins here, eg
	sitemap=ckanext.sitemap.plugin:SitemapPlugin
	""",
)
