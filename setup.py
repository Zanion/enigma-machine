from setuptools import setup, find_packages

setup(
    name='enigma-machine',
    version='0.0.1',
    py_modules=['enigma_machine'],
    packages=find_packages(exclude=['test']),
    include_package_data=True,
    install_requires=[
        'click',
    ],
    entry_points='''
        [console_scripts]
        enigma-machine=enigma_machine.__main__:cli
    ''',
)
