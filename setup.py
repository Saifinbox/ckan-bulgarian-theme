from setuptools import setup, find_packages
import sys, os

version = '3'

setup(
    name='ckanext-bulgarian_theme',
    version=version,
    description="Theme for the Bulgarian opendata portal",
    long_description="Theme for the Bulgarian opendata portal - opendata.government.bg",
    classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
    keywords='',
    author='Obshtestvo.bg',
    author_email='info@obshtestvo.bg',
    url='https://opendata.government.bg',
    license='MIT',
    packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
    namespace_packages=['ckanext', 'ckanext.bulgarian_theme'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        # -*- Extra requirements: -*-
    ],
    entry_points='''
        [ckan.plugins]
        bulgarian_theme=ckanext.bulgarian_theme.plugin:BulgarianThemePlugin
    ''',
)
