class User:
    def __init__(self, nickname : str, password : int , age : int):
        self.nickname = nickname
        self.password = hash(password)
        self.age = int(age)

class Video:
    # time_now = 0
    # adult_mode = False
    def __init__(self, title : str, duration : int, **kwargs):
        self.title = title
        self.duration = duration
        self.time_now = 0
        self.adult_mode = False

class UrTube:
    def __init__(self, *args):
        self.args = args
        self.users = []
        self.videos = []
        self.current_user = User

    def add(self, *args):
        for video in args:
            if video not in self.videos:
                self.videos.append(video)

    def get_videos(self, search_word: str):
        for i in range (len(self.videos)):
            if search_word.lower() in str(self.videos[i]).lower():
                return self.videos[i]
                # print(self.videos[i])

    def __repr__(self):
        return str(self.videos)

ur = UrTube()

v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode = True)
ur.add(v1, v2)

print(ur)

# Проверка поиска

print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))