class Employee:
    def __init__(self, name, lastname):
        self.name = name
        self.lastname = lastname
    def walk(self):
        return 'I can walk!'
    def work(self):
        return 'I am working!'

class Developer(Employee):
    def __init__(self, name, lastname, language):
        super().__init__(name, lastname)
        self.__language = language
    def coding(self):
        return "I am coding!"
    def work(self):
        return 'I am coding!'
    def get_language(self):
        return f'My language is {self.__language}'
    def set_language(self, newlang):
        self.__language = newlang

class Tester(Employee):
    def __init__(self, name, lastname, language, test_framework ):
        super().__init__(name, lastname)
        self.language = language
        self.test_framework = test_framework
    def testing(self):
        return 'I can write tests!'
    def work(self):
        return "I am writing tests!"

dev1 = Developer('Max', 'Frolov', 'Python')
 # print(dev1.walk())
# dev1.name = 'Maksim'
# print(dev1.name)
# print(dev1.lastname)
# # print(dev1.language)
# print(dev1.coding())
# print(dev1.work())
# dev1.__language = 'java' #???????
# print(dev1.get_language())
# print(dev1.__language)
# dev1.set_language('JavaScript')
# print(dev1.get_language())
print(dev1.__dict__)
print(dev1)
dev1._Developer__language = 'sdfsdf'
print(dev1.__dict__)
print(dev1)
# d = dev1.__dict__ # вытащили атрибуты в отдельный словарь
# print(d)
# print(type(d))
#
# tester1 = Tester('Anna', 'Ivaniva', 'Java', 'TestNG')
# print(tester1.name)
# print(tester1.lastname)
# print(tester1.language)
# print(tester1.test_framework)
# print(tester1.testing())
# print(tester1.work())
#
# empl1 = Employee('Alex', "Smith")
# print(empl1.name)
# print(empl1.lastname)
# print(empl1.walk())
#
# empl2 = Employee('Vladislav', 'Popov')
# print(empl2.name)
# print(empl2.lastname)
