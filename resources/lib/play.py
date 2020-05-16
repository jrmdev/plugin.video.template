import config
import sys
import utils
import xbmcgui
import xbmcplugin

_url = sys.argv[0]
_handle = int(sys.argv[1])

def play_video(params):
    try:
        params['url'] += '|User-Agent=%s' % config.USER_AGENT
        play_item = xbmcgui.ListItem(path=params['url'])
        xbmcplugin.setResolvedUrl(_handle, True, play_item)
    except Exception:
        utils.handle_error('Unable to play video')
