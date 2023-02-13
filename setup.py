from setuptools import find_packages, setup

setup(
    name='lyrics_hunter',
    packages=find_packages(),
    version='10.0.0',
    description='Python Lyrics Scrapper',
    author='Ayush Lakra',
    author_email="ayushlakra846@gmail.com",
    license='MIT',
    install_requires=['beautifulsoup4', 'requests'],
    test_requires=['beautifulsoup4', 'requests'],
    test_suite='tests',
)
