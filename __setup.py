from setuptools import setup, find_packages

setup(
    name="cubiomespi",
    version="1.0",
    packages=find_packages(),
    package_data={'cubimespi': ['lib/lib.dll', 'lib/compile.txt', 'lib/newlib.c']},
    install_requires=[],  # List your library's dependencies here
    author="Languste",
    author_email="maximilian.afemann@gmail.com",
    description="This library is a python interface for cubiomes",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url="https://github.com/Languste27/cpi",
)