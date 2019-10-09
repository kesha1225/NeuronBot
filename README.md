
<h1>Генерация текста на основе сообщений в беседе или лс бота с помощью цепей Маркова</h1>
<p align="center">Для корректной работы бота установите самую последнюю версию api.
  
### Установка:
```
$ git clone https://github.com/kesha1225/NeuronBot.git

$ pip3 install -r requirements.txt
```
### Настройка(конфиг .env):

###### Отправка случайных сообщений
```python
RANDOM_SEND = 1 
```
###### Размер предложения
```
words = generator.generate(count=random.randint(1, 10)) 
```

###### Токен и айди группы
```python
gid = 123123 #  Айди группы
token = "token" #  Токен
```




## Запуск
```
$ python3 bot.py
```


