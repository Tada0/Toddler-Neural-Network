from setuptools import setup

setup(
    name='tada0-toddler-neural-network',
    version='1.0.4',
    author ='Tomasz Hołda',
    packages=['toddlerneuron'],
    scripts=['neural_network.py', 'nn_exceptions.py'],
    install_requires=[
    "numpy",
    "csv",
    "time",],
)
