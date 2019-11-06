{%- if cookiecutter.c_extension_support != 'no' %}
from {{cookiecutter.package_namespace}}.{{ cookiecutter.package_name }} import {{ cookiecutter.c_extension_function }}
{%- endif %}
{%- if cookiecutter.test_matrix_configurator == 'yes' %}
from {{cookiecutter.package_namespace}}.{{ cookiecutter.package_name }} import main
{%- endif %}


def test_main():
{%- if cookiecutter.test_matrix_configurator == 'yes' and cookiecutter.test_matrix_configurator == 'no' %}
    assert 'site-packages' in {{cookiecutter.package_namespace}}.{{ cookiecutter.package_name }}.__file__
{%- endif %}
{%- if cookiecutter.c_extension_support != 'no' %}


def test_{{ cookiecutter.c_extension_function }}():
    assert {{ cookiecutter.c_extension_function }}([b'a', b'bc', b'abc']) == b'abc'
{%- endif %}
