![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)
![code-style](https://img.shields.io/badge/code--style-black-%23000000)

<h1>Генерация текста на основе сообщений в беседе Вконтакте с помощью цепей Маркова</h1>

> Вдохновлен [Witless](https://vk.com/witless)

<p align="center">Для корректной работы бота установите самую последнюю версию api.
  
### Установка:
```sh
git clone https://github.com/kesha1225/NeuronBot.git

pip3 install -r requirements.txt
```
### Настройка(конфиг .env):

>Если PRODUCTION=False, то можно оставить пустыми все настройки кроме
RANDOM_RULE, TOKEN и GROUP_ID.
```sh
PRODUCTION=False  # Основная настройка запуска  
RANDOM_RULE=True  # Будут ли отправляться случайные сообщения
TOKEN=TOKEN  # Токен группы
GROUP_ID=123123  # Айди группы
RABBITMQ_QUEUE=some_queue  # Название очереди rabbitmq
RABBITMQ_URL=amqp://guest:guest@127.0.0.1/  # url локальной очереди
VK_SECRET_KEY="SOME_SECRET_KEY"  # Секретный ключ от cb-api
VK_CONF_CODE="123ABCDF789"  # Код подтверждения cb-api
```

### Запуск

#### Бот имеет два способа запуска:

**Для выбора первого установите в конфиге .env ```PRODUCTION=True```, а 
для второго ```PRODUCTION=False```.**

1) Полноценный запуск в работу с [cb-api
receiver](https://github.com/prostomarkeloff/cbapi-receiver) и 
очередью сообщений RabbitMQ.
    > Необходимо устнановить rabbitmq-server
    
    ```python3
    uvicorn receiver:app
    
    python3 bot.py
    ```
2) Отладочный или просто расчитанный на небольшую нагрузку,
 работающий на longpoll.
    ```python3
    python3 bot.py
    ```
### Дополнительные настройки

Размер предложений, по умолчанию от 1 до 10 слов.
```
words = generator.generate(count=random.randint(1, 10)) 
```