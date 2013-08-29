from setuptools import setup, find_packages

setup(
    name='mock-neomodel',
    version='0.1',
    packages=find_packages(),
    install_requires=['neomodel>=0.3', 'fudge>=1.0'],
)
