import pickle
import zlib
import io

class Cache:
    def __init__(self):
        '''Создает хранилище'''
        self.assets = {}

    def add(self, path):
        '''Загружает файл'''
        with open(path, 'rb') as file:
            asset = file.read()
            self.assets[path] = asset

    def get(self, name):
        '''Возвращает файл'''
        asset = self.assets[name]
        return io.BytesIO(asset)

    def save(self, path):
        '''Сохраняет хранилище'''
        with open(path, 'wb') as file:
            data = pickle.dumps(self.assets)
            data = zlib.compress(data)

            file.write(data)

    def load(self, path):
        '''Загружает хранилище'''
        with open(path, 'rb') as file:
            data = file.read()

            data = zlib.decompress(data)
            self.assets = pickle.loads(data)