""" Commandline scripts """
import os
import sys
from base64 import b64encode

from jinja2 import Template
from pkg_resources import resource_string  # pylint: disable=E0611
from pypicloud.access import pwd_context


def make_config():
    """

    env = ['dev', test, prod]

    :param password:
    :param username:
    :param env:
    :param outfile:
    :return:
    """
    env = os.environ['ENV']
    username = os.environ['ADMIN_USERNAME']
    password = os.environ['ADMIN_PASSWORD']

    outfile = 'server.ini'

    data = {
        'env': env,
        'reload_templates': env == 'dev',
        'storage': 's3',
        'access_key': os.environ['AWS_ACCESS_KEY_ID'],
        'secret_key': os.environ['AWS_SECRET_ACCESS_KEY'],
        's3_bucket': os.environ['S3_BUCKET'],
        'encrypt_key': b64encode(os.urandom(32)),
        'validate_key': b64encode(os.urandom(32)),
        'admin': username,
        'password': pwd_context.encrypt(password),
        'session_secure': env == 'prod',
    }

    if env == 'dev' or env == 'test':
        data['wsgi'] = 'waitress'
    else:
        if hasattr(sys, 'real_prefix'):
            data['venv'] = sys.prefix
        data['wsgi'] = 'uwsgi'

    tmpl_str = resource_string('pypicloud', 'templates/config.ini.jinja2')
    template = Template(tmpl_str)

    config_file = template.render(**data)
    with open(outfile, 'w') as ofile:
        ofile.write(config_file)

    print "Config file written to '%s'" % outfile


if __name__ == '__main__':
    make_config()
