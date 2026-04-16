import requests
from urllib.parse import quote

class ImgAPI:
    def download_image(self, prompt):
        # Создаём функцию download_image.
        # Она принимает один параметр: prompt.
        # prompt - это текстовое описание картинки, которую нужно сгенерировать.

        url = f"https://image.pollinations.ai/image/{prompt}"
        # Создаём адрес запроса.
        # Внутрь URL подставляется значение переменной prompt.
        # Именно по этому адресу мы обращаемся к сервису генерации изображений.

        response = requests.get(url)
        # Отправляем GET-запрос на сервер.
        # В ответ сервер должен вернуть данные изображения.

        with open('generated_image.jpg', 'wb') as file:
            # Открываем файл generated_image.jpg в режиме записи байтов.
            # Режим wb нужен, потому что изображение - это бинарные данные, а не обычный текст.

            file.write(response.content)
            # Записываем в файл содержимое ответа сервера.
            # response.content содержит байты изображения.

        print('Image downloaded!')
        # Выводим сообщение в консоль, чтобы пользователь понял, что программа завершила работу.
        return "generated_image.jpg"
