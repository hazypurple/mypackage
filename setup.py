from setuptools import setup, find_packages

setup(
    name='mypackage',
    version='0.1',
    packages=find_packages(exclude=['tests*']),
    licence='MIT',
    description='EDSA example python package',
    long_description=open('README.md').read(),
    install_requires=['numpy'],
    url='https://github.com/hazypurple/mypackage_tut',
    author='Shehaam Mahomed',
    author_email='shehaam@gmail.com'
)
