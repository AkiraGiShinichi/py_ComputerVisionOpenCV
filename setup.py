from setuptools import setup, find_packages

requirements = [
    'pep8',
    'autopep8',
    'opencv-python', 
    'tesseract',
    'tesseract-python',
    'tensorflow',
    'tensorflow-hub',
    'tflearn',
    'keras'
]

setup(
    name='py_ComputerVisionOpenCV',
    version='1.0.0',
    description='Study from Book',
    url='https://github.com/akiragishinichi/py_ComputerVisionOpenCV.git',
    packages=find_packages(),
    install_requires=requirements,
    classifiers=['Programming Language :: Python :: 3.7']
)