# MRPIS projects

These are a collection of examples or programs that interact or use the D-bus MPRIS (Meia Player Remote Interfacing
Specification).

## Run environment

Run the environment before executing any of the projects:
```bash
source mpris-venv/bin/activate
```

The reason is that some of them use libraries that are not installed by default on the operating system.

## Install the libraries in the environment

This is the list of the libraries used in these projects:
- dbus-python
- [mpris2](https://github.com/hugosenari/mpris2/tree/67356f29d68e29c7f3f0ddda5aaad6f68899b2bd)

To install dbus-python:
```bash
pip3 install dbus-python
```
For mpris2 download the source code from the link provided above. The source code comes with other files but for this
project we get rid of most of them and only left the mpris2 folder with the python scripts.

## Useful links

The following links are repositories that were used as inspiration for these projects:
- https://github.com/marcinn/letsplay
- https://github.com/hugosenari/mpris2
- https://github.com/dylanlobo/mpris-dbus-apps
- https://github.com/inopia/gnome-media-mpris
- https://github.com/RangHo/mprisctl
- https://github.com/patrickziegler/spotify-recorder
- https://specifications.freedesktop.org/mpris-spec/latest/
- https://dbus.freedesktop.org/doc/dbus-python/dbus.html
- https://stackoverflow.com/questions/70737550/how-to-connect-to-mediaplayer2-player-playbackstatus-signal-using-pygtk