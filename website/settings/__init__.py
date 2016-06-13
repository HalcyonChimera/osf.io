# -*- coding: utf-8 -*-
'''Consolidates settings from defaults.py and local.py.

::
    >>> from website import settings
    >>> settings.MAIL_SERVER
    'smtp.sendgrid.net'
'''
import yaml


try:
    from .local import *  # noqa
except ImportError as error:
    raise ImportError("No local.py settings file found. Did you remember to "
                        "copy local-dist.py to local.py?")


discourse_settings = yaml.load(open('./website/settings/discourse_settings.yml', 'r'))

from .defaults import *  # noqa
if not DEV_MODE:
    from . import local
    from . import defaults
    
    for setting in ('WATERBUTLER_JWE_SECRET', 'WATERBUTLER_JWE_SALT', 'WATERBUTLER_JWT_SECRET', 'JWT_SECRET', 'DB_PASS', 'DEFAULT_HMAC_SECRET', 'POPULAR_LINKS_NODE', 'NEW_AND_NOTEWORTHY_LINKS_NODE'):
        assert getattr(local, setting, None) and getattr(local, setting, None) != getattr(defaults, setting, None), '{} must be specified in local.py when DEV_MODE is False'.format(setting)

