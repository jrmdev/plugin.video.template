import xbmc
import xbmcaddon
import xbmcgui

from urllib import quote_plus
from urlparse import parse_qsl

def get_addon():
    return xbmcaddon.Addon()

def get_addon_id():
    """Helper function for returning the version of the running add-on"""
    return get_addon().getAddonInfo('id')

def get_addon_name():
    """Helper function for returning the version of the running add-on"""
    return get_addon().getAddonInfo('name')

def get_addon_version():
    """Helper function for returning the version of the running add-on"""
    return get_addon().getAddonInfo('version')

def log(s):
    xbmc.log("[%s v%s] %s" % (get_addon_name(), get_addon_version(), s.encode('utf-8')), level=xbmc.LOGNOTICE)

def handle_error(message):
    if isinstance(message, str):
        message = message.split('\n')

    message = ["%s v%s" % (get_addon_name(), get_addon_version())] + message

    xbmcgui.Dialog().ok(*message)

def uri_to_dict(s):
    return {k: v for k, v in parse_qsl(s.lstrip('?'))}
