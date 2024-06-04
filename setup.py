from setuptools import setup, find_packages

setup(
   name='hw-hivepy',
   version='0.3',
   description='Small wrapper for HexWay Hive API',
   long_description=open('README.md').read(),
   long_description_content_type='text/markdown',
   include_package_data=True,
   author='@Cur1iosity',
   author_email='Cur1iosity@protonmail.com',
   url='https://github.com/Cur1iosity/hivepy',
   packages=find_packages(),
   install_requires=['requests>=2.31.0', 'pydantic>=2.4.0'],
   extras_require={
      'dev': [
         'pytest',
      ],
   },
   classifiers=[
      'Programming Language :: Python :: 3',
      'License :: OSI Approved :: MIT License',
      'Operating System :: OS Independent',
   ],
   python_requires='>=3.12',
)
