import os
from setuptools import find_packages, setup

with open(os.path.join(os.path.dirname(__file__), 'README.md')) as readme:
    README = readme.read()

# To allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='djangocms-tacc-remote-content',
    version='0.1.0',
    packages=find_packages(),
    include_package_data=True,
    license='BSD License',
    description='A DjangoCMS plugin (for TACC Core CMS) to fetch and display content from remote TACC URLs.',
    long_description=README,
    url='https://github.com/TACC/Core-CMS-Plugin-Remote-Content/',
    author='TACC ACI WMA, TACC COA CMD',
    author_email='wma-portals@tacc.utexas.edu, coa-cmd@tacc.utexas.edu',
    # SEE: https://packaging.python.org/discussions/install-requires-vs-requirements/
    install_requires=[
        'Django>=3.2',
        'django-cms>=3.7.4,<4',
        'beautifulsoup4>=4.9.3',
        'requests>=2.25.1',
    ],
    # SEE: https://pypi.org/classifiers/
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 2.2.16',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
)
