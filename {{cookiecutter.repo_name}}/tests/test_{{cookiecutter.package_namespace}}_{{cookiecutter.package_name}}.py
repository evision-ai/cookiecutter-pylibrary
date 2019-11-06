{%- if cookiecutter.c_extension_support != 'no' %}
from {{cookiecutter.package_namespace}}.{{ cookiecutter.package_name }} import {{ cookiecutter.c_extension_function }}
{%- endif %}

def test_main():
{%- if cookiecutter.c_extension_support != 'no' %}


def test_{{ cookiecutter.c_extension_function }}():
    assert {{ cookiecutter.c_extension_function }}([b'a', b'bc', b'abc']) == b'abc'
{%- endif %}
