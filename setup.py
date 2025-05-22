from setuptools import setup

setup(
    name="calculator",
    version="0.1",
    py_modules=["calculator"],
    description="Prosty kalkulator CLI",
    author="Łukasz",
    install_requires=[],
    entry_points={
        'console_scripts': [
            'calculator=calculator:main',
        ],
    },
)
