from setuptools import setup, find_packages

setup(
    name='tada0-toddler-neural-network',
    version='1.1.1',
    url='https://github.com/Tada0/Toddler-Neural-Network',
    description='Little neural network library',
    author='Tomasz Hołda',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'tnn=toddlernetwork.__main__:main'
            ]
        },
)