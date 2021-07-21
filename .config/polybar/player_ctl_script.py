#!/usr/bin/env python3
import dbus

from gi.repository import GLib

#loop = GLib.MainLoop()
#loop.run()
bus = dbus.SessionBus()




def getSongMetadata():
    for service in bus.list_names():
        if service.startswith('org.mpris.MediaPlayer2.'):
            player = dbus.SessionBus().get_object(service, '/org/mpris/MediaPlayer2')

            status=player.Get('org.mpris.MediaPlayer2.Player', 'PlaybackStatus', dbus_interface='org.freedesktop.DBus.Properties')
            metadata = player.Get('org.mpris.MediaPlayer2.Player', 'Metadata', dbus_interface='org.freedesktop.DBus.Properties')
        
            #for key in metadata:
            title = str(metadata['xesam:title'])
            len = int(metadata['mpris:length'])
            artist = str(metadata['xesam:artist'][0])
            art = "https://i.scdn.co/image/"+metadata['mpris:artUrl'].split("/")[4]
            album = str(metadata['xesam:album'])

            metadata_list = title, art, len, artist, album
            # print(metadata_list)
            
            return metadata_list

if __name__ == '__main__':
    getSongMetadata()