class Warrior(): # Создаем класс и пишем название с БОЛЬШОЙ буквы

    def __init__(self, name, power, endurance, hair_color) # init(конструктор) - это метод создания нашего объекта класса
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