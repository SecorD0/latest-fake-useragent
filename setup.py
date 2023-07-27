import os

from setuptools import setup, find_packages

with open(os.path.join(os.path.abspath(os.path.dirname(__file__)), 'README.md'), encoding='utf-8') as fh:
    long_description = '\n' + fh.read()

setup(
    name='latest-fake-useragent',
    version='1.0.1',
    license='Apache-2.0',
    author='SecorD',
    description='',
    long_description_content_type='text/markdown',
    long_description=long_description,
    packages=find_packages(),
    install_requires=['fake-useragent', 'requests'],
    keywords=[
        'useragent', 'user-agent',
        'fake-useragent', 'fake-user-agent', 'latest-fake-useragent', 'latest-fake-user-agent',
        'chrome', 'chrome-useragent', 'chrome-user-agent',
        'firefox', 'firefox-useragent', 'firefox-user-agent'
    ],
    classifiers=[
        'Programming Language :: Python :: 3.8'
    ]
)
