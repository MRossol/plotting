from setuptools import setup, find_packages

install_requires = [
    "matplotlib",
    "seaborn",
]

setup(
    name='plotting',
    version='0.1.0',
    author='Michael Rossol',
    author_email='mrossol@gmail.com',
    long_description=open('README.md').read(),
    packages=find_packages(),
    install_requires=install_requires,
)
