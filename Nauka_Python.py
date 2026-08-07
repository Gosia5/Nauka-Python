# PĘTLA FOR --------------------------

#for i in range (5):
#    print(i)


# PĘTLA WHILE ------------------------

#i = 0 
#while i < 5:
#    print(i)
#    i += 1


# HASŁO - PYTANIE 3 RAZY -------------

#haslo="Haslo123"
#licznik=0
#for i in range(3):
#    proba=input("Podaj hasło: ")
#    if proba == haslo:
#        print("Hasło poprawne.")
#        break
#    else:
#        print("Błąd.")
#else:
#    print("Za dużo prób.")


# LISTA - DODAJ OWOCE ----------------

#owoce = []
#for i in range (5):
#    owoc = input("Podaj owoc: ")
#    owoce.append(owoc)
#print(owoce)


# ĆWICZENIE FORMAT STRING ------------

#name = input("Podaj imię: ")
#city = input("Podaj miasto: ")
#hobby = input("Podaj hobby: ")

#name = name.strip().capitalize()
#city = city.strip().upper()
#hobby = hobby.strip().capitalize()

#report = [
#    "RAPORT UŻYTKOWNIKA:", 
#    "Imię: " + name, 
#    "Miasto: " + city, 
#    "Hobby: " + hobby,
#    "",
#    "Witaj, " + name]

#print(*report, sep='\n')


# ĆWICZENIE FUNKCJE LIST ------------

#queue = ["Anna", "Bartek", "Celina"]

#queue.append("Daniel")
#served = queue.pop(0)
#print("Obsłużono:", served)
#print("Aktualna kolejka:\n", queue)
#print("Liczba oczekujących:", len(queue))


# ĆwWICZENIE 2

#queue = ["Jan", "Ola", "Marek"]

#queue.append("Ewa")
#queue.append("Kasia")

#served1 = queue.pop(0)
#served2 = queue.pop(0)

#print("Obsłużono:", served1)
#print("Obsłużono:", served2)
#print("Aktualna kolejka:")
#print(queue)
#print("Liczba pacjentów:", len(queue))
#print("Następny pacjent:", queue[0])


# ĆWICZENIE FUNCKJE NIESTANDARDOWE -----

#shopping_cart = []

#def add_to_cart(shopping_cart):
#    number_of_products = int(input("Podaj ilość produktów: "))
#    for _ in range (number_of_products):
#        product = input("Podaj produkt: ")
#        shopping_cart.append(product)

#def show_cart(shopping_cart):
#    for index, product in enumerate(shopping_cart, start=1):
#        print(index, product)


# ĆWICZENIE KALKULATOR

#def calculate(number1, number2, operation):
#    if operation == "+":
#        return number1 + number2
#    if operation == "-":
#        return number1 - number2
#    if operation == "*":
#        return number1 * number2
#    if operation == "/":
#        return number1 / number2
#    return False

#number1=int(input("Podaj pierwszą liczbę: "))
#number2=int(input("Podaj drugą liczbę: "))
#operation=input("Podaj symbol działania: ")

#print("Wynik:", calculate(number1, number2, operation))

# ĆWICZENIE DOSTAWA

def free_delivery(price):
    if price >= 100:
        return True
    return False

price=float(input("Podaj cenę: "))
result = free_delivery(price)
if result:
    print("Free delivery")
if not result:
    print("Delivery fee applies")
