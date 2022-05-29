import requests
import os
import pathlib


PATH = os.getcwd()
path = os.path.join(PATH)


TOKEN = "" # Yandex токен


class Yandexloader:

    token = TOKEN

    def __init__(self, file_path):
        self.file_path = file_path

    def upload_files(self):
        url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        headers = {"Content-Type": "application/json",
                   "Authorization": "OAuth {}".format(self.token)}
        params = {"path": "disk:/Learning/" + self.file_path.name,
                  "overwrite": "true"}
        upload_link = requests.get(url, headers=headers, params=params).json()["href"]
        res = requests.put(upload_link, data=open(self.file_path, "rb"))
        res.raise_for_status()
        if res.status_code == 201:
            return "Файл успешно выгружен на Яндекс диск"
        return "Файл не выгружен, ошибка!"


if __name__ == "__main__":
    uploader = Yandexloader(pathlib.Path(path, "file.txt"))
    print(uploader.upload_files())