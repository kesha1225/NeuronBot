<h1>Генерация теста на основе сообщений в беседе или лс бота с помощью цепей Маркова</h1>

### Установка:
```
$ git clone https://github.com/kesha1225/NeuronBot.git

$ pip3 install -r requirements.txt
```
### Настройка:

###### Отправка случайных сообщений
```python
RANDOM_SEND = 1 
```
###### Размер предложения
```python
words = generator.generate(count=random.randint(1, 10)) 
```

###### Токен и айди группы
```python
gid = 123123 #  Айди группы
token = "token" #  Токен
```
*Для корректной работы бота установите самую последнюю версию api.*



## Запуск
```
$ python3 bot.py
```
