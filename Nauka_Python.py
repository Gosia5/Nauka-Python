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


# NEXT


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

#def free_delivery(price):
#    if price >= 100:
#        return True
#    return False

#price=float(input("Podaj cenę: "))
#result = free_delivery(price)
#if result:
#    print("Free delivery")
#if not result:
#    print("Delivery fee applies")


# ĆWICZENIE 1

#def convert_temperature(temperature, unit):
#    """Funkcja do konwertowania temperatury"""
#    if unit == "C":
#        return (temperature * 9/5 + 32)
#    elif unit == "F":
#        return ((temperature - 32) * 5/9)

#temperature = float (input("Podaj ilość stopni: "))
#unit = input("Podaj jednostkę stopni (C/F): ")

#result = convert_temperature(temperature, unit)
#print("Przekonwertowana temperatura:", result)


#ĆWICZENIE 2

def validate_email(email):
    """Funcja do sprawdzania obecności znaków @ i . w adresie email"""
    if "@" in email and "." in email:
        return True
    else:
        return False

email=input("Podaj adres email: ")
result=validate_email(email)
if result:
    print("Valid email")
if not result:
    print("Invalid email")