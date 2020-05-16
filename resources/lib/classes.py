import urllib
import utils

class MenuItem(object):
    def __init__(self, **kwargs):
        self.playable = False # set to true if this is a video
        
        for key in kwargs:
            setattr(self, key, kwargs[key])

    def has(self, attr):
        return hasattr(self, attr) and getattr(self, attr)

    def get(self, attr):
        return getattr(self, attr) if self.has(attr) else None

    def to_kodi_url(self):
        # Make sure encoding is correct for displaying in kodi menus
        for k in self.__dict__:
            var = getattr(self, k)
            
            if isinstance(var, unicode):
                setattr(self, k, var.encode('utf-8', 'ignore'))

        # If we clicked on a playable item, just include the url
        if self.playable and self.has('url'):
            return urllib.urlencode({'url': self.url})

        # Otherwise this is a listing item, include all properties
        return urllib.urlencode({k: v for k, v in vars(self).items() if v})

    def from_kodi_url(self, url):
        d = utils.uri_to_dict(url)

        for k in d:
            setattr(self, k, d[k])
