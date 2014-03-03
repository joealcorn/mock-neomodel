from setuptools import setup, find_packages

setup(
    name='mock-neomodel',
    version='0.4',
    url='https://github.com/buttscicles/mock-neomodel',
    description='Basic mocking of neomodel objects',
    license='MIT',
    packages=find_packages(),
    install_requires=['neomodel>=0.4', 'fudge>=1.0'],
    classifiers=['License :: OSI Approved :: MIT License']
)
