#mediaan
import random as rd
numbers = []
for i in range(11):
    numbers.append(rd.randint(1,100))

numbers.sort()
print(numbers)
length = len(numbers)

if length % 2 == 0:
    mediaan1 = numbers[length//2]
    mediaan2 = numbers[length//2 - 1]
    mediaan = (mediaan1 + mediaan2) / 2
else:
    mediaan = numbers[length//2]

print(f"De mediaan is: {round(mediaan)}")

# incl btw naar excl btw
incl_btw = int(input("Van welk bedrag wilt u de btw aftrekken?\n"))

if isinstance(incl_btw,int or float):
    excl_btw = incl_btw/1.21
    print(f"Het bedrag € {incl_btw} is € {excl_btw} exclusief 21% btw.")
else:
    print("Foute invoerwaarde, probeer opnieuw!")

# bereken de procentuele stijging
startbedrag = float(input("Wat is het startbedrag?\n"))
eindbedrag = float(input("Wat is het eindbedrag na de stijging?\n"))

print(f"De procentuele stijging van € {startbedrag} naar € {eindbedrag} is {round((eindbedrag/startbedrag - 1)*100)}%.")

# 2 dobbelstenen simuleren
def dobbelstenen(aant_worpen):
    import random as rd
    worpen = []
    counter = 1
    while counter <= aant_worpen:
        worp = rd.choice([1,2,3,4,5,6]) + rd.choice([1,2,3,4,5,6])
        worpen.append(worp)
        counter += 1
    print(f"Het gemiddelde van {len(worpen)} worpen met 2 dobbelstenen is {sum(worpen)/len(worpen)}.")

dobbelstenen(100)

