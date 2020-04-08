'''
Реализовать следующие элементы:
Вода, Воздух, Огонь, Земля, Шторм, Пар, Грязь, Молния, Пыль, Лава.
Каждый элемент организовать как отдельный класс.
Таблица преобразований:
Вода + Воздух = Шторм
Вода + Огонь = Пар
Вода + Земля = Грязь
Воздух + Огонь = Молния
Воздух + Земля = Пыль
Огонь + Земля = Лава
Сложение элементов реализовывать через __add__
Если результат не определен - то возвращать None
Вывод элемента на консоль реализовывать через __str__
Примеры преобразований:
print(Water(), '+', Air(), '=', Water() + Air())
print(Fire(), '+', Air(), '=', Fire() + Air()) (edited)
'''

class MetaElement(type):
    elembase = dict()

    def __new__(mcs, name, bases, attrs):
        cls = super().__new__(mcs, name, bases, attrs)  

        if name != 'Element':
            if len(bases) == 1:
                mcs.elembase.setdefault(cls,dict())
            elif len(bases) == 2:
                mcs.elembase[bases[0]].setdefault(bases[1],cls)
            
        return cls
    

class Element(metaclass=MetaElement):
    tag = 'Elem'
    elembase = MetaElement.elembase
      
    def __add__(self, other):
        if type(self) in self.elembase:
            if type(other) in self.elembase[type(self)]:
                return self.elembase[type(self)][type(other)]()
        if type(other) in self.elembase:
            if type(self) in self.elembase[type(other)]:
                return self.elembase[type(other)][type(self)]()

    def __str__(self):
        return self.tag


class Fire(Element):
    tag = 'Fire'


class Water(Element):
    tag = 'Water'


class Air(Element):
    tag = 'Air'


class Earth(Element):
    tag = 'Earth'


class Storm(Air,Water):
    tag = 'Storm'


class Dust(Air, Earth):
    tag = 'Dust'


class Lighting(Fire, Air):
    tag = 'Lighting'


class Mud(Earth, Water):
    tag = 'Mud'


class Steam(Fire,Water):
    tag = 'Steam'

class Lava(Earth, Fire):
    tag = 'Lava'

class Glass(Fire, Dust):
    tag = 'Glass'

class Glasswater(Water, Glass):
    tag = 'Glass of water'

elems = [Fire(),Water(),Earth(),Air()]

from itertools import permutations as p
for e in p(elems,2):
	print(f'{e[0]} + {e[1]} =  {e[0]+e[1]}')
