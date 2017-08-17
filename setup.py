from setuptools import setup, find_packages

setup(
    name='earthdata_download',
    version='0.2',
    description='NASA EarthData download interface',
    author='Jonas Solvsteen',
    author_email='josl@dhi-gras.com',
    url='https://www.dhi-gras.com',
    packages=find_packages(),
    install_requires=[
        'wget_provider'],
    dependency_links=[
        'https://github.com/DHI-GRAS/wget_provider/archive/v0.2.tar.gz#egg=wget_provider-0.2'])