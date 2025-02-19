class Song:
    def __init__(self,title,artist,album,genre,duration) -> None:
        self.title = title
        self.artist = artist
        self.album = album
        self.genre = genre
        self.duration = duration
    def display_details(self):
        return f"Title: {self.title}, Artist: {self.artist}, Album: {self.album}, Genre: {self.genre}, Duration: {self.duration}" 
    
#2nd class
class Playlist:
    def __init__(self,name):
        self.name = name
        self.songs =[]

    def add_song(self,Song):
        self.songs.append(Song)

    def remove_song(self,title):
        for song in self.songs:
            if song.title == title:
                self.songs.remove(song)
                return True
        return False
        

    def get_songs(self):
        return self.songs

    def filter_songs(self,Critera, value):
        out=[]
        if Critera=="artist":
            for song in self.songs:
                if song.artist ==value:
                    out.append(song)
        else:
            if Critera =="genre":
                for song in self.songs:
                    if song.genre ==value:
                        out.append (song)
            
           
        return out

        
    def search_songs(self,keyword):
        keyword = keyword.lower()
        searched_tasks = []
        for task in self.songs:
            if keyword in  task.title.lower() or keyword in task.artist.lower() or keyword in task.album.lower() or keyword in task.genre.lower():
                searched_tasks.append(task)
        return searched_tasks

#3rd class
class PlaylistManager:
    def __init__(self) -> None:
        self.playlists=[]
    def create_playlist(self,name):
        self.playlists.append(Playlist(name))

    def delete_playlist(self,name):
        for i in self.playlists:
            if i.name ==name:
                self.playlists.remove(i)
                return True
        return False
    def get_playlist(self,name):
        for i in self.playlists:
            if i.name == name:
                return i
        return None
    def list_playlists(self):
        return self.playlists
    def cross_playlist_search(self,keyword):
        keyword = keyword.lower()
        searched_tasks = []
        for task in self.playlists:
            # if keyword in task.name.lower():#or keyword in task.details.lower()
            #     searched_tasks.append(task)
            searched_tasks.extend(task. search_songs(keyword))
        return searched_tasks