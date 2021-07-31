#!/usr/bin/env python3

# import the needed stuff

from os import WIFCONTINUED
import kivy


from kivy.config import Config

# Window config
# we want it centered, my screen res is 2560x1440

vert_height = 150
horiz_height= 350

window_left_pos = int(2560/2-(horiz_height/2))

# my polybar height (for now is 27 px)

window_top = int(1440)

# Hides title bar for configs where titlebar is enabled
Config.set('graphics', 'fullscreen', 'fake')


# Disables resizing
Config.set('graphics', 'resizable', False)
Config.set('graphics', 'position', 'custom')
Config.set('graphics', 'left', window_left_pos)
Config.set('graphics', 'top',  50)

#sets window size

Config.set('graphics', 'width', str(horiz_height))
Config.set('graphics', 'height', str(vert_height))

#Window.size = (window_vert_size, window_horiz_size)

from kivy.app import App
from kivy.core import window
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
from kivy.clock import Clock

import player_ctl_script



class MouseLeavesWindow(Label):
    def __init__(self, **kwargs):
        super(MouseLeavesWindow, self).__init__(**kwargs)
        Window.bind(on_cursor_leave=self.cursor_leave)

    def cursor_leave(self, window):
        print("lmao")


class MainContainer (BoxLayout):
    def __init__(self, *args):
        super().__init__()
        self.playing = True

        # FORWARD AND REWIND CHARACTER
        self.ids.np.text = chr(63622) + " Playing"
        self.ids.pl.text= chr(63715)
        self.ids.rw.text = chr(63838)
        self.ids.ff.text = chr(63248)


        self.metadata_list = player_ctl_script.getSongMetadata()
        Clock.schedule_interval(self.update, 1)

    def update(self, val):
        #self.ids.img.source = player_ctl_script.getSongArt()
        self.ids.title.text = player_ctl_script.getTitle()
        self.ids.artist.text = player_ctl_script.getArtist()

    def playingFunc(self, val):
        if self.playing == True:
            print (self.playing)
            player_ctl_script.pauseSong(self)
            self.ids.pl.text= chr(63753)
            self.playing = not self.playing
        
        elif self.playing == False:
            player_ctl_script.playSong(self)
            self.ids.pl.text = chr(63715)
            self.playing = not self.playing

class MyApp(App):
    def __init__(self, *args):
        super().__init__()

    def build(self):
        return MainContainer()

def main(*args):
    MouseLeavesWindow()
    MyApp().run()

if __name__ == '__main__':
    main()