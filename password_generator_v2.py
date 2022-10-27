import random
characters = "QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm\|`¬1234567890-=!£$%^&*()_+[]{};'#:@~,./<>?123456789"
myarray = []
choice = int(input("How many characters do you want in your password? "))
list = list(characters)
random.shuffle(list)
characters_shuffled = "".join(list)
for choice in range(choice):
    random_number_generator = random.randint(0, 103)
    characters_selected = characters_shuffled[random_number_generator]
    myarray.append(characters_selected)
    product = "".join(myarray)
print(product)
