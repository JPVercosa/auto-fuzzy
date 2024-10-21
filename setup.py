
from setuptools import setup, find_packages


def readme():
    with open('README.md') as f:
        return f.read()

setup(name='autofis',
      version = '0.1.1',
      description = 'Automatic Synthesis of Fuzzy Inference Systems Toolkit',
      long_description = readme(),
      url = 'https://github.com/lucasthim/auto-fuzzy',
      license = 'MIT',
      author = 'Lucas Thimoteo',
      packages = find_packages(exclude=['tests','ensemble']),
    #   entry_points = {
    #       'console_scripts': [
    #           'autofis=autofis.console:main',
    #       ],
    #   },
      install_requires = [
          'pandas',
          'numpy',
          'scikit-learn',
          'scipy'
      ],
      zip_safe=False)
