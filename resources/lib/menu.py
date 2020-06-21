import sys
import xbmcgui
import xbmcplugin
import comm
import utils
import config

from classes import MenuItem

_url = sys.argv[0]
_handle = int(sys.argv[1])

def make_menu(objects, next='', sort=False):
    try:
        listing = []

        for item in objects:

            li = xbmcgui.ListItem(label=item.get('title'), iconImage=item.get('icon'), thumbnailImage=item.get('thumb'))
            url = '{0}?action={1}&{2}'.format(_url, next, item.to_kodi_url())
            
            if item.playable:
                li.setProperty('IsPlayable', 'true')

            if item.has('description'):
                li.setInfo('video', {'plot': item.description, 'plotoutline': item.description})

            if item.has('duration'):
                li.setInfo('video', {'duration': item.duration})

            if item.has('date'):
                li.setInfo('video', {'date': item.date, 'aired': item.date})

            if item.has('mpaa'):
                li.setInfo('video', {'mpaa': item.mpaa})

            if item.has('season'):
                li.setInfo('video', {'season': item.season})

            if item.has('episode'):
                li.setInfo('video', {'episode': item.episode})

            if item.has('genre'):
                li.setInfo('video', {'genre': item.genre})

            if item.has('fanart'):
                li.setArt({'fanart': item.fanart})

            if item.has('banner'):
                li.setArt({'banner': item.banner})

            listing.append((url, li, not item.playable))

        if len(objects) == config.PAGE_SIZE:
            pager = MenuItem()
            pager.from_kodi_url(sys.argv[2])
            pager.page = int(pager.page) + 1 if hasattr(pager, 'page') else 1

            url = '{0}?action={1}&{2}'.format(_url, next, pager.to_kodi_url())
            li = xbmcgui.ListItem('Next page')
            listing.append((url, li, True))

        if len(objects) and objects[0].has('content'):
            xmbcplugin.setContent(_handle, objects[0].content)

        if sort:
            xbmcplugin.addSortMethod(_handle, xbmcplugin.SORT_METHOD_LABEL_IGNORE_THE)

        xbmcplugin.addDirectoryItems(_handle, listing, len(listing))
        xbmcplugin.endOfDirectory(_handle)

    except Exception:
        utils.handle_error("Unable to make menu")
