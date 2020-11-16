from setuptools import setup

setup(
    name='PingProvider',
    version='1.0',
    py_modules=['pingprovider'],
    install_requires=[
        'Click',
        'pythonping'
    ],
    entry_points='''
        [console_scripts]
        pingprovider=pingprovider:cli
    ''',
)