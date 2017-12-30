from setuptools import setup, find_packages

setup(
    name='mara-acl',
    version='1.2.0',

    description='Default ACL implementation for Mara',

    install_requires=[
        'mara-db>=2.0.0',
        'mara-page>=1.2.0'
    ],

    dependency_links=[
        'https://github.com/mara/mara-page.git@1.2.0#egg=mara-page'
    ],

    packages=find_packages(),

    author='Mara contributors',
    license='MIT',

    entry_points={},
)

