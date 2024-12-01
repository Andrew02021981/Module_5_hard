import time

class User:
    def __init__(self, nickname : str, password : int , age : int):
        self.nickname = nickname
        self.password = password
        self.age = age

    def __str__(self):
        return self.nickname

class Video:
    def __init__(self, title : str, duration : int, adult_mode: bool = False):
        self.title = title
        self.duration = duration
        self.time_now = 0
        self.adult_mode = adult_mode

class UrTube:
    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None

    def register(self, nickname : str, password : str, age : int):
        password = hash(password)
        for nick in self.users:
            if nick.nickname == nickname:
                print(f'Пользователь {nickname} уже существует')
                return
        new_user = User(nickname, password, age)
        self.users.append(new_user)
        self.current_user = new_user

    def log_out(self):
        self.current_user = None

    def log_in(self, nickname, password):
        for nick in self.users:
            if nick in self.users and password == nick.password:
                self.current_user = nick

    def add(self, *args):
        for video in args:
            if video not in self.videos:
                self.videos.append(video)

    def get_videos(self, search_word: str):
        list_video = []
        for video in self.videos:
            if search_word.upper() in video.title.upper():
                list_video.append(video.title)
        return  list_video

    def watch_video(self, video: str):
        if not self.current_user:
            print('Войдите в аккаунт, чтобы смотреть видео')
            return

        for search_ in self.videos:
            if search_.title == video:
                if search_.adult_mode is True and self.current_user.age < 18:
                    print('Вам нет 18 лет, пожалуйста, покиньте страницу')
                    return

                for j in range(1, 11):
                    time_now = 0
                    print(j, end=' ')
                    time.sleep(1)
                    time_now = time_now + 1
                print('Конец видео')

ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)
# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')
