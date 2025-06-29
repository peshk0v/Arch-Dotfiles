#!/bin/bash

if [ $# -lt 2 ]; then
  echo "Usage: $0 <transition_type> <delay_seconds>"
  echo "Available transitions: fade, outer, wave, random"
  exit 1
fi

swww img $(find ~/Pictures/Wallpapers/ -type f | shuf -n 1) --transition-fps 255 --transition-type fade --transition-duration 0.8

sleep "$2"

while true; do
  if [ "$1" == "fade" ]; then
    swww img $(find ~/Pictures/Wallpapers/ -type f | shuf -n 1) --transition-type fade
  elif [ "$1" == "outer" ]; then
    swww img $(find ~/Pictures/Wallpapers/ -type f | shuf -n 1) --transition-type outer --transition-pos "$(hyprctl cursorpos)"
  elif [ "$1" == "wave" ]; then
    swww img $(find ~/Pictures/Wallpapers/ -type f | shuf -n 1) --transition-type wave --transition-angle 30 --transition-step 120
  elif [ "$1" == "random" ]; then
    swww img $(find ~/Pictures/Wallpapers/ -type f | shuf -n 1) --transition-type any --transition-angle 45 --transition-step 80
  else
    echo "Unknown transition type: $1"
    exit 1
  fi
  sleep "$2"
done
