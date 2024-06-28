from PetsFriends import Pets

cat_1= Pets ("Барон", "мальчик", 2)
cat_2= Pets ( "Сэм", "мальчик", 2)

class Cats:
    def _str_(self):
        return f'имя: {self.name}, пол: {self.gender}, возраст: {self.age} '

print(" Первый кот ", Cats._str_(cat_1))
print(" Второй кот ", Cats._str_(cat_2))


