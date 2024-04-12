import dbus
import sys
from dbus.exceptions import DBusException
from mpris2.mpris2 import player, interfaces
from mpris2.mpris2.types import Metadata_Map

print()
print(f"MPRIS2 bus name: {interfaces.Interfaces.MEDIA_PLAYER}")
print(f"MPRIS2 object path: {interfaces.Interfaces.OBJECT_PATH}")

uri = interfaces.Interfaces.MEDIA_PLAYER + ".spotify"
print(f"Spotify bus name: {uri}")

try:
    spotify_player = player.Player(dbus_interface_info={'dbus_uri': uri})
except DBusException as dbus_exception:
    # Catch the exception when the Spotify player is not running
    print(f"DBusException: {str(dbus_exception)}")
    sys.exit(1)
else:
    print(f"Spotify playback status: {spotify_player.PlaybackStatus}")

    if spotify_player.PlaybackStatus == "Playing" or spotify_player.PlaybackStatus == "Paused":
        print("\nCurrent track information:")
        print("\tTitle: " + spotify_player.Metadata[Metadata_Map.TITLE])
        print("\tAlbum: " + spotify_player.Metadata[Metadata_Map.ALBUM])
        print()