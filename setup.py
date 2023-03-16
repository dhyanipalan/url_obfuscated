import os
from setuptools import setup, find_packages

with open(os.path.join(os.path.dirname(__file__), 'README.md')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))
VERSION = '0.0.1'
NAME = 'Dhyanikumar Palan'
EMAIL = 'dhyanipalan@gmail.com'
setup(
    name='url-obfuscated',
    version=VERSION,
    packages=find_packages(),

    # Dependencies
    install_requires=['Django>=2.2', 'pycrypto==2.6.1'],

    # Metadata for PyPI
    author=NAME,
    author_email=EMAIL,
    maintainer=NAME,
    maintainer_email=EMAIL,
    description='Easy and Simple method to obfuscate and deobfuscate your Django URLs.',
    long_description=README,
    long_description_content_type='text/markdown',
    license='Apache License',
    url='https://github.com/dhyanipalan/url_obfuscated',
    keywords=['django', 'Python', 'url' 'obfuscate', 'encrypt'],
    download_url='https://github.com/dhyanipalan/url_obfuscated',
    bugtrack_url='https://github.com/dhyanipalan/url_obfuscated/issues',
    classifiers=[
        'License :: OSI Approved :: Academic Free License (AFL)',
        'Natural Language :: English',
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
        'Framework :: Django',
    ]
)
