"""
问题描述：宠物、狗和猫的类如下：
class Pet:
    def __init__(self, type):
        self.type = type
    def get_pet_type(self):
        return self.type

class Dog(Pet):
    def __init__(self):
        super().__init__('dog')

class Cat(Pet):
    def __init__(self):
        super().__init__('cat')

实现一种猫狗队列的结构，要求如下：
1）用户可以调用add方法将cat类或者dog类的实例放入队列中
2）用户可以调用pollAll方法，将队列中的所有实例按照进队列的先后顺序依次弹出
3）用户可以调用pollDog方法，将队列中dog类的实例按照进队列的先后顺序依次弹出
4）用户可以调用pollCat方法，将队列中cat类的实例按照队列的先后顺序依次弹出
5）用户可以调用isEmpty方法，检查队列中是否还有dog或cat的实例
6）用户可以调用isDogEmpty方法，检查队列中是否有dog类的实例
7）用户可以调用isCatEmpty方法，检查队列中是否有cat类的实例

思路：实现一个带有保存时间（这里可以是逻辑上的时间，比如1、2、3等表先后顺序的属性）的队列，
用一个来保存猫，另外一个来保存狗即可
"""


class Pet:
    def __init__(self, type):
        self.type = type

    def get_pet_type(self):
        return self.type


class Dog(Pet):
    def __init__(self):
        super().__init__('dog')

    def __str__(self):
        return 'dog'


class Cat(Pet):
    def __init__(self):
        super().__init__('cat')

    def __str__(self):
        return 'cat'


class DogCatCounter:
    def __init__(self, pet, count):
        self.pet = pet
        self.count = count

    def get_type(self):
        return self.pet.get_pet_type()


class DogCatQueue:
    def __init__(self):
        self.dogcounter_queue = list()
        self.catcounter_queue = list()

    def isEmpty(self):
        return len(self.dogcounter_queue) and len(self.catcounter_queue)

    def isDogEmpty(self):
        return len(self.dogcounter_queue) == 0

    def isCatEmpty(self):
        return len(self.catcounter_queue) == 0

    def add(self, pet):
        count = len(self.dogcounter_queue) + len(self.catcounter_queue)
        if pet.get_pet_type() == 'dog':
            self.dogcounter_queue.append(DogCatCounter(pet, count))
        else:
            self.catcounter_queue.append(DogCatCounter(pet, count))

    def pollAll(self):
        if self.isEmpty():
            raise RuntimeError('No element in it')
        if self.isDogEmpty():
            return self.catcounter_queue.pop(0).pet
        if self.isCatEmpty():
            return self.dogcounter_queue.pop(0).pet

        first_dog = self.dogcounter_queue[0]
        first_cat = self.catcounter_queue[0]
        if first_dog.count < first_cat.count:
            return self.dogcounter_queue.pop(0).pet
        else:
            return self.catcounter_queue.pop(0).pet

    def pollDog(self):
        if self.isDogEmpty():
            raise RuntimeError('No dog in it')
        return self.dogcounter_queue.pop(0).pet

    def pollCat(self):
        if self.isCatEmpty():
            raise RuntimeError('No cat in it')
        return self.catcounter_queue.pop(0).pet


if __name__ == '__main__':
    dog_cat_queue = DogCatQueue()
    dog1 = Dog()
    dog2 = Dog()
    dog3 = Dog()
    cat1 = Cat()
    cat2 = Cat()
    cat3 = Cat()

    dog_cat_queue.add(dog1)
    dog_cat_queue.add(cat1)
    dog_cat_queue.add(dog2)
    dog_cat_queue.add(cat2)
    dog_cat_queue.add(dog3)
    dog_cat_queue.add(cat3)

    dog_cat_queue.add(dog1)
    dog_cat_queue.add(cat1)
    dog_cat_queue.add(dog2)
    dog_cat_queue.add(cat2)
    dog_cat_queue.add(dog3)
    dog_cat_queue.add(cat3)

    dog_cat_queue.add(dog1)
    dog_cat_queue.add(cat1)
    dog_cat_queue.add(dog2)
    dog_cat_queue.add(cat2)
    dog_cat_queue.add(dog3)
    dog_cat_queue.add(cat3)

    while not dog_cat_queue.isDogEmpty():
        print(dog_cat_queue.pollDog().get_pet_type())

    while not dog_cat_queue.isCatEmpty():
        print(dog_cat_queue.pollCat().get_pet_type())