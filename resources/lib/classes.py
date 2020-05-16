import urllib
import utils
import config

class MenuItem(object):
    def __init__(self, **kwargs):
        self.playable = False # set to true if this is a video
        
        for key in kwargs:
            setattr(self, key, kwargs[key])

    def has(self, attr):
        return hasattr(self, attr) and getattr(self, attr)

    def get(self, attr):
        if not self.has(attr):
            return None

        val = getattr(self, attr)

        if isinstance(val, str) and val.startswith(('http://', 'https://')):
            return '{}|{}'.format(val, urllib.urlencode({'User-Agent': config.USER_AGENT, 'Range': ''}))

        return val

    def to_kodi_url(self):
        # Make sure encoding is correct for displaying in kodi menus
        for k in self.__dict__:
            val = getattr(self, k)
            
            if isinstance(val, unicode):
                setattr(self, k, val.encode('utf-8', 'ignore'))

        # If we clicked on a playable item, just include the url
        if self.playable and self.has('url'):
            return urllib.urlencode({'url': self.url})

        # Otherwise this is a listing item, include all properties
        return urllib.urlencode({k: v for k, v in vars(self).items() if v})

    def from_kodi_url(self, url):
        d = utils.uri_to_dict(url)

        for k in d:
            setattr(self, k, d[k])
