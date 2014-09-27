from setuptools import setup, find_packages
import sys, os

version = '3'

setup(
    name='ckanext-obshtestvo_theme',
    version=version,
    description="Theme for data.obshtestvo.bg",
    long_description='''
    ''',
    classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
    keywords='',
    author='Obshtestvo.bg',
    author_email='info@obshtestvo.bg',
    url='https://data.obshtestvo.bg',
    license='MIT',
    packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
    namespace_packages=['ckanext', 'ckanext.obshtestvo_theme'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        # -*- Extra requirements: -*-
    ],
    entry_points='''
        [ckan.plugins]
        obshtestvo_theme=ckanext.obshtestvo_theme.plugin:ObshtestvoThemePlugin
    ''',
)
