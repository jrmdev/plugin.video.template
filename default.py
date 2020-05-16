import sys
import xbmc

from resources.lib import utils, menu, play, comm

def router(paramstring):
    params = utils.uri_to_dict(paramstring)
    
    if 'action' in params:

        # Implement more menu levels here as needed

        if params['action'] == 'get_videos':
            menu.make_menu(comm.get_videos(params), next='play')

        elif params['action'] == 'play':
            play.play_video(params)
    
    else:
        menu.make_menu(comm.get_categories(), next='get_videos', sort=True) # First level

if __name__ == '__main__':
    router(sys.argv[2][1:])
