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

#def shipping_cost(weight):
#    cost = 8 + (weight * 2)
#    return cost

#pack1 = shipping_cost(3)
#pack2 = shipping_cost(7)
#pack3 = shipping_cost(12)

#print("Koszt wysyłki:", pack1, "zł")
#print("Koszt wysyłki:", pack2, "zł")
#print("Koszt wysyłki:", pack3, "zł")


# ŚWICZENIE ENUMERATE

#cart=["chleb", "masło", "mleko"]

#def show_cart(cart):
#    for index, product in enumerate(cart, start=1):
#        print(index, product.capitalize())
   
#show_cart(cart)




