class User:
    def __init__(self, nickname : str, password : int , age : int):
        self.nickname = nickname
        self.password = hash(password)
        self.age = int(age)

class Video:
       def __init__(self, *args, **kwargs):
        self.title = str
        self.duration = int
        self.time_now = 0
        self.adult_mode = False

class UrTube:
    def __init__(self, *args):
        self.args = args
        self.users = []
        self.videos = []
        self.current_user = User

    def add(self, *args):
        self.args = args
        if self.args not in self.videos:
            self.videos.append(args)

    def __repr__(self):
        """Формальное строковое представление."""
        return f'{self.videos}'

ur = UrTube()

v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

ur.add(v1, v2)

print(ur)
