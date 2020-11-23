"""
Package setup information for dankag.
"""
from setuptools import setup, find_packages


install_requirements = [
    'numpy',
    'pandas',
    'scikit-learn',
    'xgboost',
    'tensorflow',
]


setup(
    name='dankag',
    version='0.1.1',
    description='utilities for kaggle competitions',
    author='Dan Suh',
    author_email='kaehops@gmail.com',
    python_requires='>=3.7',
    packages=find_packages(exclude=['docs', 'tests*']),
    install_requires=install_requirements,
    classifiers=[
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
)
