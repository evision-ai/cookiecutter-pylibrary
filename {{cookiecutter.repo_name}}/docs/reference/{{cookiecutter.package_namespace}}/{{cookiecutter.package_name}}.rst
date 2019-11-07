{{cookiecutter.package_namespace}}.{{ cookiecutter.package_name }}
{{ "=" * cookiecutter.package_namespace|length }}={{ "=" * cookiecutter.package_name|length }}

.. testsetup::

    from {{cookiecutter.package_namespace}}.{{ cookiecutter.package_name }} import *

.. automodule:: {{cookiecutter.package_namespace}}.{{ cookiecutter.package_name }}
    :members:
