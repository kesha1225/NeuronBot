## Генерация текста на основе сообщений в беседе или лс бота с помощью цепей маркова

#### Установка
```
git clone https://github.com/kesha1225/NeuronBot.git

pip install mc.py
pip install https://github.com/prostomarkeloff/vk.py/archive/master.zip --upgrade
```
#### Настройка
```python
RANDOM_SEND = 1 #  Будут ли отправляться случайные сообщения
```

##### Токен и айди устанавливается в файле vk_interaction.py
```python
gid = 123123 #  Айди группы
token = "token" #  Токен
```

###### Версия api в группе должна стоять последняя

Размер сгенерированного предложения менять здесь (По умолчанию от 1 до 10 слов)
```
words = generator.generate(count=random.randint(1, 10)) 
```

#### Запуск
```
python3 bot.py
```