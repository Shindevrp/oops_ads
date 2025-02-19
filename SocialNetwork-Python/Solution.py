class Person:
    def __init__(self,name,games) -> None:
        self.name = name
        self.games = games
        # self.FavoriteGame=[]

    def add_game(self,game):
        if game not in self.games:
            self.games.append(game)
    def remove_game(self,game):
        if game in self.games:
            self.games.remove(game)
    def get_favorite_games(self):
        return self.games
    def get_name(self):
        return self.name
    def __str__(self):
        return "Person(name=" + self.name + ", games=" + str(self.games) + ")"
class SocialNetwork:
    def __init__(self):
        self.person = None
        self.users = []
    
    def add_user(self,person):
        for user in self.users:
            if user.get_name()==person.get_name():
                print(f"User with name {person.get_name()} already exists.")
                return
        self.users.append(person)


        
    def remove_user(self, name):
        for user in self.users:
            if user.get_name() == name:
                self.users.remove(user)
                if self.person==user:
                    self.person=None
                return
        print(f"User with name {name} not found.")

    def get_user(self, name):
        for user in self.users:
            if user.get_name() == name:
                return user
        return None

    def update_person(self, person):
        for i in self.users:
            if i.get_name() == person.get_name():
                self.person  = i
                return
        print(f"User {person.name} is not in the network.")

    def get_users_who_like(self,game):
        userswholike = []
        for user in self.users:
            if game in user.get_favorite_games():
                userswholike.append(user.get_name())
        return userswholike
    
    # def __str__(self):
    #     user_names = []
    #     for user in self.users:
    #         user_names.append(user.get_name())
    #     return f"SocialNetwork(current person={self.person}, users=[Person(name={user.get_name()}, games={user.get_favorite_games()})])"

    def __str__(self):
        users_str = ""
        for user in self.users:
            users_str += str(user) + ", "
        users_str = users_str.rstrip(", ")
        return f"SocialNetwork(current person={self.person}, users=[{users_str}])"