from abc import ABCMeta, abstractmethod

class Animal(metaclass=ABCMeta):
    @abstractmethod
    def __init__(self, animal_type, body_type, character):
        self.animal_type = animal_type
        self.body_type = body_type
        self.character = character
    #是否属于凶猛动物：同时满足  “体型 >= 中等” “食肉类型”  “性格凶猛”
    @property
    def is_fierce(self):
        if  (self.body_type == "中" or self.body_type == "大") and self.animal_type == '食肉' and self.character == '凶猛':
            return True
        else:
            return False

class Cat(Animal):
    mew = 'miao'
    def __init__(self, name, animal_type, body_type, character):
        self.name = name
        super().__init__(animal_type, body_type, character)
    @property
    def is_pet(self):
        return not self.is_fierce

class Zoo(object):
    def __init__(self, name):
        self.name = name
        self.animals = []
    #“添加动物”方法要实现同一只动物（同一个动物实例）不能被重复添加的功能。
    def add_animal(self, animal_name):
        if animal_name not in self.animals:
            self.animals.append(animal_name)
        else:
            print("This animal had existed.")

if __name__ == '__main__':
	
    # 实例化动物园
    z = Zoo('时间动物园')
	
    # 实例化一只猫，属性包括名字、类型、体型、性格
    cat1 = Cat('大花猫 1', '食肉', '小', '温顺')

    # 增加一只猫到动物园
    z.add_animal(cat1)
	
    # 动物园是否有猫这种动物
    have_cat = getattr(z, 'Cat')