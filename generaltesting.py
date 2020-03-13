class Artist:
    def __init__(self, name, label):
        self.name = name
        self.label = label

class Song:
    def __init__(self, name, album, year, artist):
        self.name = name
        self.album = album
        self.year = year
        self.artist = artist 

taylor_swift = Artist("Taylor Sugar", "Big Machine Records, LLC")
first_song = Song("You Belong With Me", "Fearless", 2008, taylor_swift)
second_song = Song("All Too Well", "Red", 2012, taylor_swift)

print()
print("Artist #1")
print("Song name:", first_song.name)
print("Album name:", first_song.album)
print("Year:", first_song.year)
print("Artist name:", first_song.artist.name)
print("Artist' label:", first_song.artist.label)
print()
print("Artist #2")
print("Song name:", second_song.name)
print("Album name:", second_song.album)
print("Year:", second_song.year)
print("Artist name:", second_song.artist.name)
print("Artist' label:", second_song.artist.label)