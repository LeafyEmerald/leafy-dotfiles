#!/bin/bash

# Terminate the already running bar instances
killall -q polybar

# Wait untill the processes have been shut down
while pgrep -u $UID -x polybar >/dev/null; do sleep 1; done

# Launch polybar, using the default config location
polybar example &

echo "Polybar launched..."
