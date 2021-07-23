#!/bin/bash
if pgrep -f music_player_gui.py
then
	pkill -f music_player_gui.py
else
	python ~/.config/polybar/music_player_gui.py
fi
