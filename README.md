<p>
<img src="https://img.shields.io/badge/License-MIT-yellow.svg">
<img src="https://img.shields.io/badge/python-3.6%2B-%23FFD242">
<img src="https://img.shields.io/badge/code--style-black-%23000000">
</p>

<h1>Генерация текста на основе сообщений в беседе Вконтакте с помощью цепей Маркова</h1>

> Вдохновлен [Witless](https://vk.com/witless)

<p align="center">Для корректной работы бота установите самую последнюю версию api.
  
### Установка:
```sh
git clone https://github.com/kesha1225/NeuronBot.git

cd NeuronBot

pip install -r requirements.txt
```
### Настройка(конфиг .env):

>Если PRODUCTION=False, то можно оставить пустыми все настройки кроме
RANDOM_RULE, TOKEN и GROUP_ID.
```sh
PRODUCTION=False  # Основная настройка запуска  
RANDOM_RULE=True  # Будут ли отправляться случайные сообщения
USUAL_SYNTAX=False # Подгонять ли сообщения под нормальный синтаксис с точками и заглавными буквами
TOKEN=TOKEN  # Токен группы
RABBITMQ_QUEUE=some_queue  # Название очереди rabbitmq
RABBITMQ_URL=amqp://guest:guest@127.0.0.1/  # url локальной очереди
VK_SECRET_KEY=SOME_SECRET_KEY  # Секретный ключ от cb-api
VK_CONF_CODE=123ABCDF789  # Код подтверждения cb-api
```

### Запуск

#### Бот имеет два способа запуска:

**Для выбора первого установите в конфиге .env ```PRODUCTION=True```, а 
для второго ```PRODUCTION=False```.**

1) Отладочный или просто расчитанный на небольшую нагрузку,
 работающий на longpoll.

```sh
python bot.py
```

2) Полноценный запуск в работу с cb-api receiver и очередью сообщений RabbitMQ.
Для него вам понадобится установить дополнительные библиотеки:
```
pip install starlette uvicorn aio_pika
```
> Необходимо устнановить rabbitmq-server
    
```sh
python receiver.py
    
python bot.py
```