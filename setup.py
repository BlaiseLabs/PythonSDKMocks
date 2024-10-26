from setuptools import setup, find_packages

setup(
    name='sdk_mocks',
    version='0.1.0',
    author='BlaiseLabs',
    author_email='blaiselabs@gmail.com',
    description='A library of pre-built mocks for popular Python SDKs.',
    packages=find_packages(),
    python_requires='>=3.6',  # Adjust as needed
)
