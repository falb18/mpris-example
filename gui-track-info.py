import dbus
import tempfile
import os

from tkinter import *
from mpris2.mpris2 import utils, player, interfaces
from urllib.parse import urlparse
from urllib.request import urlretrieve, urlcleanup
from PIL import Image, ImageTk

# Get Spotify's interface
#------------------------------------------------------------------------------

# Metadata fields keys
track_title_tag = 'xesam:title'
track_album_tag = 'xesam:album'
track_artist_tag = 'xesam:artist'
track_artUrl_tag = 'mpris:artUrl'

print(f"MPRIS2 bus name: {interfaces.Interfaces.MEDIA_PLAYER}")
print(f"MPRIS2 object path: {interfaces.Interfaces.OBJECT_PATH}")

uri = interfaces.Interfaces.MEDIA_PLAYER + ".spotify"
print(f"Spotify bus name: {uri}")

spotify_player = player.Player(dbus_interface_info={'dbus_uri': uri})

# Create temporary directory where album covers will be downloaded.
# Keep in mind that after program ends all the thumbnails are going to be deleted.
albums_dir = tempfile.TemporaryDirectory(prefix='albums_')

def get_spotify_artAlbum(url_album_cover) -> str:
    # For more information:
    # https://stackoverflow.com/a/18727481
    # https://stackoverflow.com/a/50336597
    file_name,_ = urlretrieve(url_album_cover)
    image = Image.open(file_name)
    album_cover_path = albums_dir.name + '/' + os.path.basename(file_name) + '.png'
    image.save(album_cover_path)

    return album_cover_path

# GUI helper functions
#------------------------------------------------------------------------------

def get_album_cover(artAlbum_url) -> ImageTk.PhotoImage:
    image_artAlbum = Image.open(artAlbum_url)
    image_artAlbum = image_artAlbum.resize([100, 100])
    return ImageTk.PhotoImage(image_artAlbum)

# Build GUI
#------------------------------------------------------------------------------

window = Tk()
window.title("Metadata information")
window.geometry("450x120")
# window.resizable(0, 0)

def get_text_justification(str_metadata, str_length) -> str:
    print(len(str_metadata))
    if len(str_metadata) >= str_length:
        return 'left'
    else:
        return 'center'

def create_labels():
    y_window_margin = 10
    y_lbl_margin = 2
    lbl_height_px = 21
    lbls_width = 27
    lbl_bg_color = 'white'
    text_justify = ""

    text_justify = get_text_justification(spotify_player.Metadata[track_title_tag], lbls_width)
    lbl_song_title = Label(
                        window,
                        text=f"Title: {spotify_player.Metadata[track_title_tag]}",
                        justify=text_justify,
                        background=lbl_bg_color)
    lbl_song_title.place(x=120, y=y_window_margin)

    text_justify = get_text_justification(spotify_player.Metadata[track_album_tag], lbls_width)
    lbl_album = Label(
                    window,
                    text=f"Album: {spotify_player.Metadata[track_album_tag]}",
                    justify=text_justify,
                    background=lbl_bg_color)
    lbl_album.place (x=120, y=y_window_margin + (lbl_height_px + y_lbl_margin)*1)

    text_justify = get_text_justification(spotify_player.Metadata[track_artist_tag], lbls_width)
    lbl_artist = Label(
                    window,
                    text=f"Artist: {spotify_player.Metadata[track_artist_tag][0]}",
                    justify=text_justify,
                    background=lbl_bg_color)
    lbl_artist.place (x=120, y=y_window_margin + (lbl_height_px + y_lbl_margin)*2)

    window.update()

def create_album_thumbnail():
    lbl_bg_color = 'white'
    artAlbum_url = get_spotify_artAlbum(spotify_player.Metadata[track_artUrl_tag])
    thumbnail = get_album_cover(artAlbum_url)
    lbl_thumbnail = Label(window, image=thumbnail, background=lbl_bg_color)
    lbl_thumbnail.place(x=10, y=10)

    # Keep the image after the function returns: https://ccia.ugr.es/mgsilvente/tkinterbook/photoimage.htm
    lbl_thumbnail.image = thumbnail
    window.update()

def build_gui():
    create_labels()
    create_album_thumbnail()

# Main
#------------------------------------------------------------------------------

build_gui()
window.mainloop()

# Delete all album covers downloaded
urlcleanup()