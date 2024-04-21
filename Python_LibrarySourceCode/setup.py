from setuptools import setup
import setuptools

setup(
    name="ConsoleColor",
    author="RiritoNinigaya",
    author_email="riritoninigaya@hotmail.com",
    version="1.0",
    license='LGPL-2.1',
    description="My First Library for Colorizing Text Color in Console Window!!!",
    packages=setuptools.find_packages(),
    package_data={
        '': ['resource\\*.dll'],
    }
)
