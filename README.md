# Parser for twitch
With this parser you could get list of streams from all videos page.

Main function `list_of_streams()`:
- `nickname` - name of the streamer, on main page or in the url.
- `file_output` - in whitch file to write list of the streams.
- `separator` - which would separate: `nickname`, `game name`, `title of the video`, `link to the video`.
- `stdout` - flag for print result to stdout.
- `appending` - flag for appending result to the `file_output`.
- `rewrite` - flag for rewrite the `file_output` with the result.

Dependencies:
- `import argparse` - for making command tool arguments.
- `import sys` - this module used for making fast stdout, but you could just change `sys.stdout.write('\n'.join(streams_list))` to `print('\n'.join(streams_list))`.
- `import cchardet` - also performans module, that is not necessary in this type of task, this module improve "file read time".
- `import requests` - for getting html from site.
- `from bs4 import BeautifulSoup` - for parsing html from site.
- `from lxml import etree` - for parsing html from site with xpath, because bs4 don't have this feature.

List of parameters for command tool
- `-n | --nickname` - name of the streamer, on main page or in the url.
- `-o | --output` - in whitch file to write list of the streams.
- `-s | --separator`- which would separate: `nickname`, `game name`, `title of the video`, `link to the video`.
- `-S | --stdout` - flag for print result to stdout.
- `-A | --append` - flag for appending result to the `file_output`.
- `-R | --rewrite` - flag for rewrite the `file_output` with the result.

Examples from terminal:
```
twitch-parse.py -n streamer_nickname -o ~/list_of_streams -S
twitch-parse.py -n streamer_nickname -o ~/list_of_streams -A
twitch-parse.py -n streamer_nickname -o ~/list_of_streams -R
```
for this functuanality you need:
- change first line of the twitch-parse.py, to find which path to add run this command `which python`, if you don't have `which` command, to install on arch run `sudo pacman -S which`.
- to give permition to run this file -> `chmod u+x twitch-parse.py`.
- and if you would like to use it from any directory, you need to move in to the $PATH location, if you don't know where is your $PATH run `echo $PATH` or add `export PATH="path/that/you/want:$PATH"` to your .bashrc/.zshrc/etc.
- if you would like to use this command tool like `twitch-parse -n streamer_nickname -o ~/list_of_streams -S` simply rename the file.

For more extensibility:
- you can use it with mpv, youtube-dl and dmenu
    - `sudo pacman -S mpv` - media player
    - `sudo pacman -S youtube-dl` - extension for ability to watch youtube videos and twitch streams within mpv
    - `sudo pacman -S dmenu` - lightweght menu
- [example script](twitch-mpv.sh)
