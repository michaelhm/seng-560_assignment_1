from setuptools import find_packages, setup

setup (
    name='math_lib',
    packages=find_packages(include='[math_lib]'),
    version='0.1.0',
    description='Reusable math library for SENG-560',
    author='Michael McLinden',
    license='GNU General Public License',
    install_requires=[],
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
    test_suite='test',
)