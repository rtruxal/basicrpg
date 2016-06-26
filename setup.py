from setuptools import setup

def readme():
    with open('README.rst') as f:
        return f.read()

setup(name='basicrpg',
      version='0.1',
      description="Just a simple rpg to make sure I'm pythoning correctly.",
      url='https://github.com/rtruxal/basicrpg',
      author='rtruxal',
      author_email='rtruxal@gmail.com',
      license='MIT',
      keywords='rpg beginner inheretence classmethods',
      requires=[
          'numpy',
          'matplotlib'
      ]
      )