
Changelog
=========
{% set datestring -%}
{% now 'utc', '%Y-%m-%d' %}
{%- endset %}
{{ cookiecutter.version }} ({{ datestring }})
{% for _ in cookiecutter.version %}-{% endfor %}--{{ '-' * (datestring|length) }}-

* First release on PyPI.
