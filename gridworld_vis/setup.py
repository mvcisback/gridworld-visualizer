from setuptools import find_packages, setup

DESC = 'Gridworld visualization library..'

setup(
    name='gridworld-viz',
    version='0.0.0',
    description=DESC,
    url='http://github.com/mvcisback/gridworld-viz',
    author='Marcell Vazquez-Chanlatte',
    author_email='marcell.vc@eecs.berkeley.edu',
    license='MIT',
    install_requires=[
        'svgwrite'
    ],
    packages=find_packages(),
)
