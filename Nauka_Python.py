
#for i in range (5):
#    print(i)

#i = 0 
#while i < 5:
#    print(i)
#    i += 1

haslo="Haslo123"
licznik=0
for i in range(3):
    proba=input("Podaj hasło: ")
    if proba == haslo:
        print("Hasło poprawne.")
        break
    else:
        print("Błąd.")
else:
    print("Za dużo prób.")