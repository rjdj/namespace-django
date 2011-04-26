import os
import imp
from django.conf import settings
from django.core.management import execute_manager as execute_django

def find_ns_management_module(app_name):
    parts = app_name.split('.')
    parts.append('management')
    parts.reverse()
    part = parts.pop()
    path = None

    if settings.DEBUG:
        print "Searching for managment module in %s ..." % app_name

    try:
        module = app_name.split(".")
        module.append("management")
        paths = __import__(".".join(module)).__path__
    except ImportError,e:
        raise e

    res = []
    for path in paths:
        p = parts[:]
        while p:
            part = p.pop()
            try:
                f, path, descr = imp.find_module(part, path and [path] or None)
                res.append(path)
            except Exception,e:
                pass

    management_module = res and res.pop() or ''
    if settings.DEBUG:
        print "Found in %s" % management_module
    return management_module


def execute_manager(settings_mod, argv=None):
    """Execute Django"""
    import django.core.management
    # Patch Django's find_management_module method.
    django.core.management.find_management_module = find_ns_management_module
    execute_django(settings_mod, argv=argv)
