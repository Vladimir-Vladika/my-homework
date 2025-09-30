class Warrior(): # Создаем класс и пишем название с БОЛЬШОЙ буквы

    def __init__(self, name, power, endurance, hair_color): # init(конструктор) - это метод создания нашего объекта класса
# self (это обязательный атрибут), он указывает то что мы создаем функцию конкретно для класса Warrior
#name, power, endurance, hair_color - это переменные
        self.name = name #Создаем характеристику и приравниваем ее к переменной
        self.power = power# Мы введем power оно сохраниться в self.power
        self.endurance = endurance # Теперь эти характеристики будут использоваться при создании объекта
        self.hair_color = hair_color

    def sleep(self): #Прописываем методы
        print(f'{self.name} лег спать') #Выводит что человек с именем name сейчас спит
        self.endurance += 2 # добавляет 2 очка к выносливости

    def eat(self):
        print(f'{self.name} сейчас кушает')
        self.power += 1 # добавляет 2 очка к силе

    def hit(self):
        print(f'{self.name} сейчас дерется в бою')
        self.endurance -= 3

    def walk(self):
        print(f'{self.name} находится на прогулке')

    def info(self): # Функция которая выводит всю информацию
        print(f'Имя война - {self.name}')
        print(f'Сила война - {self.power}')
        print(f'Выносливость война - {self.endurance}')
        print(f'Цвет волос война - {self.hair_color}')

war1 = Warrior('Сергей', 85, 70, 'Брюнет') # Создаем переменную которая будет хранить объект, данного класса
#Указываем имя класса затем в скобках прописываем аргументы для метода
war2 = Warrior('Алекс', 90, 75, 'Блондин') # Создаем новый объект класса
# МЫ МОЖЕМ СОЗДАВАТЬ СКОЛЬКО УГОДНО ОБЬЕКТОВ КЛАССА

print(war2.name)  #прописываем переменную, в которой храниться класс и через точку выводим характеристики

print(war2.power)
print(war2.endurance)

war2.eat()
war2.sleep() #Выводит метод(функцию) из класса

print(war2.power)
print(war2.endurance)

war1.info()  #Выводит всю информацию записанную в методе
war1.info()