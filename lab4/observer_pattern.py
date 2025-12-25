from abc import ABC, abstractmethod

class Observer(ABC):
    @abstractmethod
    def update(self, message):
        pass

class Subject(ABC):
    def __init__(self):
        self._observers = []

    def attach(self, observer):
        if observer not in self._observers:
            self._observers.append(observer)

    def detach(self, observer):
        if observer in self._observers:
            self._observers.remove(observer)

    def notify(self, message):
        for observer in self._observers:
            observer.update(message)

class NewsAgency(Subject):
    def __init__(self):
        super().__init__()
        self._latest_news = None

    def publish_news(self, news):
        self._latest_news = news
        self.notify(f"Новая новость: {news}")

    def get_latest_news(self):
        return self._latest_news

class NewsSubscriber(Observer):
    def __init__(self, name):
        self.name = name
        self.received_news = []

    def update(self, message):
        self.received_news.append(message)
        return f"{self.name} получил: {message}"
