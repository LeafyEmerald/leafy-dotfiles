#!/usr/bin/env python3
import dbus

from gi.repository import GLib

#loop = GLib.MainLoop()
#loop.run()
bus = dbus.SessionBus()

mprisMediaPlayer = bus.get_object('org.mpris.MediaPlayer2.spotify', '/org/mpris/MediaPlayer2')
mpris = dbus.Interface(mprisMediaPlayer, 'org.mpris.MediaPlayer2.Player')

def playSong(self):
    mpris.Play()

def pauseSong(self):
    mpris.Pause()

def nextSong(self):
    mpris.Next()

def prevSong(self):
    mpris.Previous()

#mpris.Play()

def getSongArt():
    metadata = getSongMetadata()
    art = "https://i.scdn.co/image/"+metadata['mpris:artUrl'].split("/")[4]
    #print(art)
    return art

def getTitle():
    metadata = getSongMetadata()
    title = str(metadata['xesam:title'])
    return title

def getArtist():
    metadata = getSongMetadata()
    artist = str(metadata['xesam:artist'][0])
    return artist

def getLen():
    metadata = getSongMetadata()
    len = int(metadata['mpris:length'])
    return len

def getAlbum():
    metadata = getSongMetadata()
    album = str(metadata['xesam:album'])
    return album

def getSongMetadata():
    #for service in bus.list_names():
        #if service.startswith('org.mpris.MediaPlayer2.'):
            #player = dbus.SessionBus().get_object(, '/org/mpris/MediaPlayer2')

            #status=mpris.Get('org.mpris.MediaPlayer2.spotify', 'PlaybackStatus', dbus_interface='org.freedesktop.DBus.Properties')
            metadata = mpris.Get('org.mpris.MediaPlayer2.Player', 'Metadata', dbus_interface='org.freedesktop.DBus.Properties')
        
            #for key in metadata:
            #title = str(metadata['xesam:title'])
            #len = int(metadata['mpris:length'])
            #artist = str(metadata['xesam:artist'][0])
            #art = "https://i.scdn.co/image/"+metadata['mpris:artUrl'].split("/")[4]
            #album = str(metadata['xesam:album'])            
            return metadata

if __name__ == '__main__':
    #playSong()
    getSongMetadata()
    print(getArtist())