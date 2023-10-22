from setuptools import setup, find_packages

setup(
   name='HivePy',
   version='0.1.0',
   description='Small wrapper for HexWay Hive API',
   author='@Cur1iosity',
   author_email='Ilyakovalevk@gmail.com',
   packages=find_packages(),
   install_requires=['requests>=2.31.0', 'pydantic>=2.4.0'],
)
