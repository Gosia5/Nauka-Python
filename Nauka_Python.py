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


# ŚWICZENIA FORMAT STRING ------------

name = input("Podaj imię: ")
city = input("Podaj miasto: ")
hobby = input("Podaj hobby: ")

name = name.strip().capitalize()
city = city.strip().upper()
hobby = hobby.strip().capitalize()

report = [
    "RAPORT UŻYTKOWNIKA:", 
    "Imię: " + name, 
    "Miasto: " + city, 
    "Hobby: " + hobby,
    "",
    "Witaj, " + name]

print(*report, sep='\n')
