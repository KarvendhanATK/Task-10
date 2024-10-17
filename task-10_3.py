class Audio:
    def __init__(self, title, url):
        self.title = title
        self.url = url
        self.ratings = []

    def add_rating(self, rating):
        if 1 <= rating <= 5:
            self.ratings.append(rating)

    def average_rating(self):
        return sum(self.ratings) / len(self.ratings) if self.ratings else 0


class Playlist:
    def __init__(self, name):
        self.name = name
        self.audios = []

    def add_audio(self, audio):
        self.audios.append(audio)

    def average_rating(self):
        total_rating = sum(audio.average_rating() for audio in self.audios)
        return total_rating / len(self.audios) if self.audios else 0


class MusicPlayer:
    def __init__(self):
        self.playlists = []

    def create_playlist(self, name):
        playlist = Playlist(name)
        self.playlists.append(playlist)
        return playlist

    def search_audio(self, title):
        results = []
        for playlist in self.playlists:
            for audio in playlist.audios:
                if title.lower() in audio.title.lower():
                    results.append(audio)
        return results

    def search_playlist(self, name):
        for playlist in self.playlists:
            if name.lower() == playlist.name.lower():
                return playlist
        return None
