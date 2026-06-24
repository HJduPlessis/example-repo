class Album:
    def __init__(self, album_name, number_of_songs, album_artist):
        self.album_name = album_name;
        self.number_of_songs = number_of_songs;
        self.album_artist = album_artist;
    def __str__(self):
        return f"({self.album_name}, {self.album_artist}, {self.number_of_songs})";

albums1 = [Album("The Dark Side of the Moon", 10, "Pink Floyd"), Album("Abbey Road", 17, "The Beatles"), Album("Thriller", 9, "Michael Jackson"), Album("Back in Black", 10, "AC/DC"), Album("Rumours", 11, "Fleetwood Mac")];

albums1.sort(key=lambda x: x.number_of_songs);
print("Albums1 sorted by number of songs:");
for album in albums1:
    print(album);

albums1[0], albums1[1] = albums1[1], albums1[0];
print("Albums1 after swapping first two albums:");
for album in albums1:
    print(album);

albums2 = [Album("Hotel California", 9, "Eagles"), Album("Led Zeppelin IV", 8, "Led Zeppelin"), Album("Nevermind", 12, "Nirvana"), Album("The Wall", 26, "Pink Floyd"), Album("Born to Run", 8, "Bruce Springsteen")];

print("Albums2:");
for album in albums2:
    print(album);


for album in albums1:
    albums2.append(album);

albums2.append(Album("Dark Side of the Moon", 9, "Pink Floyd"));
albums2.append(Album("Oops!... I Did It Again", 16, "Britney Spears"));

albums2.sort(key=lambda x: x.album_name);

print("Albums2 sorted by name:");
for album in albums2:
    print(album);

for album in albums2:
    if album.album_name == "Dark Side of the Moon":
        print(f"Album index: {albums2.index(album)}");
        break;