import dbus
from mpris2.mpris2 import utils, player, interfaces

# Metadata fields keys
track_title = 'xesam:title'
track_album = 'xesam:album'

print()
print(f"MPRIS2 bus name: {interfaces.Interfaces.MEDIA_PLAYER}")
print(f"MPRIS2 object path: {interfaces.Interfaces.OBJECT_PATH}")

uri = interfaces.Interfaces.MEDIA_PLAYER + ".spotify"
print(f"Spotify bus name: {uri}")

spotify_player = player.Player(dbus_interface_info={'dbus_uri': uri})
print(f"Spotify playback status: {spotify_player.PlaybackStatus}")

if spotify_player.PlaybackStatus == "Playing" or spotify_player.PlaybackStatus == "Paused":
    print("\nCurrent track information:")
    print("\tTitle: " + spotify_player.Metadata[track_title])
    print("\tAlbum: " + spotify_player.Metadata[track_album])
    print()