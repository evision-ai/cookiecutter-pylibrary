#!/usr/bin/env python
# -*- encoding: utf-8 -*-
from __future__ import absolute_import
from __future__ import print_function

import io
{% if cookiecutter.repo_hosting_domain == "no" -%}
import os.path
{% endif -%}
import re
from glob import glob
from os.path import basename
from os.path import dirname
from os.path import join
from os.path import splitext

from setuptools import find_namespace_packages
from setuptools import setup


def read(*names, **kwargs):
    with io.open(
        join(dirname(__file__), *names),
        encoding=kwargs.get('encoding', 'utf8')
    ) as fh:
        return fh.read()


setup(
    name='{{ cookiecutter.distribution_name }}',
    version='{{ cookiecutter.version }}',
    description={{ '{0!r}'.format(cookiecutter.project_short_description).lstrip('ub') }},
    long_description='%s\n%s' % (
        re.compile('^.. start-badges.*^.. end-badges', re.M | re.S).sub('', read('README.rst')),
        re.sub(':[a-z]+:`~?(.*?)`', r'``\1``', read('CHANGELOG.rst'))
    ),
    author='eVision.AI',
    author_email='dev@evision.ai',
{%- if cookiecutter.repo_hosting_domain == "no" %}
    url='file://' + os.path.abspath(dirname(__file__)),
{%- else %}
    url='https://{{ cookiecutter.repo_hosting_domain }}/{{ cookiecutter.repo_username }}/{{ cookiecutter.repo_name }}',
{%- endif %}
    packages=find_namespace_packages('src', include=['{{ cookiecutter.package_namespace }}.*']),
    package_dir={'': 'src'},
    py_modules=[splitext(basename(path))[0] for path in glob('src/*.py')],
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        # complete classifier list: http://pypi.python.org/pypi?%3Aaction=list_classifiers
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Operating System :: Unix',
        'Operating System :: POSIX',
        'Operating System :: Microsoft :: Windows',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        # uncomment if you test on these interpreters:
        # 'Programming Language :: Python :: Implementation :: IronPython',
        # 'Programming Language :: Python :: Implementation :: Jython',
        # 'Programming Language :: Python :: Implementation :: Stackless',
        'Topic :: Utilities',
        'Private :: Do Not Upload'
    ],
{%- if cookiecutter.repo_hosting_domain != "no" %}
    project_urls={
        'Changelog': 'https://{{ cookiecutter.repo_hosting_domain }}/{{ cookiecutter.repo_username }}/{{ cookiecutter.repo_name }}/blob/master/CHANGELOG.rst',
        'Issue Tracker': 'https://{{ cookiecutter.repo_hosting_domain }}/{{ cookiecutter.repo_username }}/{{ cookiecutter.repo_name }}/issues',
    },
{%- endif %}
    keywords=[
        # eg: 'keyword1', 'keyword2', 'keyword3',
    ],
    python_requires='!=2.*, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*, !=3.4.*',
    install_requires=[
        # eg: 'aspectlib==1.1.1', 'six>=1.7',
    ],
    extras_require={
        # eg:
        #   'rst': ['docutils>=0.11'],
        #   ':python_version=="2.6"': ['argparse'],
    },
{%- set setup_requires_interior %}
        'pytest-runner',
{%- endset %}
)
