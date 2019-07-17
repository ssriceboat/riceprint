import os
from setuptools import setup

cwd = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(cwd, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

# Install colorama if using Windows
if os.name == 'nt':
   dependencies = ['colorama']
else:
   dependencies = []

setup(
   name='riceprint',
   version='1.5.5',
   description='OS-agnostic colored & custom Python console print() functions.',
   long_description=long_description,
   author='Kevin Sacca',
   author_email='ssriceboat@gmail.com',
   url='https://github.com/ssriceboat/riceprint',
   project_url='Documentation, https://riceprint.readthedocs.io/en/latest/',
   license='MIT',
   classifiers=[
      'Development Status :: 4 - Beta',

      'Intended Audience :: Developers',
      'Topic :: Software Development :: Build Tools',

      'License :: OSI Approved :: MIT License',

      'Programming Language :: Python :: 3',
      'Programming Language :: Python :: 3.5',
      'Programming Language :: Python :: 3.6',
      'Programming Language :: Python :: 3.7',
   ],
   packages=['riceprint'],
   package_dir={'riceprint': 'src/riceprint'},
   install_requires=dependencies,
   keywords='print console terminal shell python pprint color progress bar'
)
