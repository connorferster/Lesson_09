from setuptools import setup

setup(
   name='my_package',
   version='0.0.1',
   description='A useful module',
   author='Connor Ferster',
   author_email='cferster@rjc.ca',
   packages=['my_package'],  #same as name
   install_requires=[], #external packages as dependencies
)