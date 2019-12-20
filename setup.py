from setuptools import setup, find_packages

setup(
    name='enigma-machine',
    version='0.0.1',
    py_modules=['enigma_machine'],
    package_dir={'': 'src'},
    packages=find_packages(where='src', exclude=['test']),
    include_package_data=True,
    install_requires=[
        'click',
    ],
    entry_points={
        'console_scripts': {
            'enigma-machine=__main__:cli'
        }
    },
)
