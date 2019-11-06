========
Overview
========
{% if cookiecutter.repo_hosting_domain == "github.com" %}
.. start-badges

.. end-badges
{% endif %}
{{ cookiecutter.project_short_description|wordwrap(119) }}
Installation
============

::

    pip install {{ cookiecutter.distribution_name }}

You can also install the in-development version with::
{% if cookiecutter.repo_hosting_domain == "github.com" %}
    pip install https://github.com/{{ cookiecutter.repo_username }}/{{ cookiecutter.repo_name }}/archive/master.zip
{% elif cookiecutter.repo_hosting_domain == "gitlab.com" %}
    pip install https://gitlab.com/{{ cookiecutter.repo_username }}/{{ cookiecutter.repo_name }}/-/archive/master/{{ cookiecutter.repo_name }}-master.zip
{% else %}
    pip install git+ssh://git@{{ cookiecutter.repo_hosting_domain }}/{{ cookiecutter.repo_username }}/{{ cookiecutter.repo_name }}.git@master
{%- endif %}

Development
===========

To run the all tests run::

    tox

Note, to combine the coverage data from all the tox environments run:

.. list-table::
    :widths: 10 90
    :stub-columns: 1

    - - Windows
      - ::

            set PYTEST_ADDOPTS=--cov-append
            tox

    - - Other
      - ::

            PYTEST_ADDOPTS=--cov-append tox
