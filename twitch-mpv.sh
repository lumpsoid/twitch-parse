#!/bin/sh

# pass list from txt file to dmenu
chosen_nickname=$(cat ~/.local/share/qq/twitch-nicknames | dmenu -i -l 30)
# Exit if none chosen.
[ -z "${chosen_nickname}" ] && exit

# pass list of streams to dmenu
chosen_video=$(parser-twitch -n ${chosen_nickname} -S | dmenu -i -l 30 | cut -d '|' -f4)
[ -z "${chosen_video}" ] && exit


chosen_format=$(youtube-dl --list-formats ${chosen_video} | awk 'NR>=7 {print $1}' | dmenu -i -l 7)
[ -z "${chosen_format}" ] && exit

# you can customize cash buffer (`--demuxer-max-bytes`) you can use `M` for megabytes and `K` for kilobytes
mpv --pause --save-position-on-quit --demuxer-max-bytes=30M --ytdl-format="${chosen_format}" ${chosen_video}
