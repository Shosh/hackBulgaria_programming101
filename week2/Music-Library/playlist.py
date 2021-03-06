import json
from song import Song


class Playlist():

    def __init__(self, name):
        self.name = name
        self.songs = []

    def __str__(self):
        result = ''
        for song in self.songs:
            time = str(round(song.length / 60, 2))
            time = time.replace('.', ':')
            tmp = ' '.join(['\n', song.artist, song.title, '-', time])
            result += tmp
        return result

    def add_song(self, song):
        self.songs.append(song)

    def remove_song(self, song_name):
        for song in self.songs:
            if song.title == song_name:
                self.songs.remove(song)

    def total_length(self):
        length = 0
        for song in self.songs:
            length += song.length
        return length

    def remove_disrated(self, rating):
        for song in self.songs:
            if song.rating < rating:
                self.remove_song(song.title)

    def remove_bad_quality(self):
        for song in self.songs:
            if song.bitrate <= 96:
                self.remove_song(song.title)

    def show_artists(self):
        result = []
        for song in self.songs:
            if song.artist not in result:
                result.append(song.artist)
        return result

    def save(self, file_name):
        playlist = {"name": self.name, "songs": []}
        for song in self.songs:
            song = song.__dict__
            playlist["songs"].append(song)
        playlist_file = open("{}.json".format(file_name), 'a+')
        playlist_file.write(json.dumps(playlist))
        playlist_file.close()


def load(file_name):
    playlist_file = open(file_name, 'r')
    content = playlist_file.read()
    content = json.loads(content)
    playlist_file.close()
    loaded_playlist = Playlist(content['name'])
    for song in content['songs']:
        loaded_playlist.songs.append(
            Song(
                song['title'],
                song['artist'],
                song['album'],
                song['rating'],
                song['length'],
                song['bitrate'])
        )
        print(loaded_playlist.songs)
    return loaded_playlist
