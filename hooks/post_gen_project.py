from __future__ import print_function

import datetime
import os
import shutil
import subprocess
import sys
from os.path import join

try:
    from click.termui import secho
except ImportError:
    warn = note = print
else:
    def warn(text):
        for line in text.splitlines():
            secho(line, fg="white", bg="red", bold=True)

    def note(text):
        for line in text.splitlines():
            secho(line, fg="yellow", bold=True)


def unlink_if_exists(path):
    if os.path.exists(path):
        os.unlink(path)

if __name__ == "__main__":
{%- if cookiecutter.repo_hosting == 'no' %}
    os.unlink('CONTRIBUTING.rst')
{% endif %}

#    print("""
#################################################################################
#
#    Generating CI configuration ...
#""")
#    try:
#        subprocess.check_call(['tox', '-e', 'bootstrap'])
#    except Exception:
#        try:
#            subprocess.check_call([sys.executable, '-mtox', '-e', 'bootstrap'])
#        except Exception:
#            subprocess.check_call([sys.executable, join('ci', 'bootstrap.py')])

    print("""
################################################################################
################################################################################

    You have successfully created `{{ cookiecutter.repo_name }}`.

################################################################################

    You've used these cookiecutter parameters:
{% for key, value in cookiecutter.items()|sort %}
        {{ "{0:26}".format(key + ":") }} {{ "{0!r}".format(value).strip("u") }}
{%- endfor %}

    See .cookiecutterrc for instructions on regenerating the project.

################################################################################

    To get started run these:

        cd {{ cookiecutter.repo_name }}
        git init
        git add --all
        git commit -m "Add initial project skeleton."
        git remote add origin git@{{ cookiecutter.repo_hosting_domain }}:{{ cookiecutter.repo_username }}/{{ cookiecutter.repo_name }}.git
        git push -u origin master
""")
