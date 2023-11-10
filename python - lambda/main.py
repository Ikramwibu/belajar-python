# def sayHello(name):
#    print("Selamat Datang", name)

sayHello = lambda name: print("selamat datang", name)

sayHello("Jaka")

# def addition(num1, num2):
#  result = num1 + num2
#  print(result)

addition = lambda num1, num2 : print(num1+num2)
addition(10,12)

# lambda tanpa argumen
(lambda : print("Selamat Datang"))()

# lambda dengan argumen
(lambda fruit : print("Saya Suka", fruit))("nanas")

# lambda dengan defaul argume
(lambda name="" : print("Selamat Datang", name))()