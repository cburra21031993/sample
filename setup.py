from setuptools import setup

setup(
    name='my_package',
    version='1.0.0',
    author='John Doe',
    author_email='john.doe@example.com',
    description='A sample Python package',
    packages=['my_package'],
    install_requires=[
        'numpy>=1.19.0',
        'pandas>=1.0.0',
    ],
)
