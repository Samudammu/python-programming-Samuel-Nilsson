# övning 1.1

i = int(input("Skriv in ett tal: "))

if i > 0:
    print(f"{i} är positivt")
elif i < 0:
    print(f"{i} är negativt")
else:
    print(f"{i} är noll")



# övning 1.2

tal1 = int(input("Ange första talet: "))
tal2 = int(input("Ange andra talet: "))

if tal1 > tal2:
    print(f"{tal1} är större än {tal2}")
elif tal1 < tal2:
    print(f"{tal2} är större än {tal1}")
else:
    print(f"{tal1} är lika stort som {tal2}")



#övning 1.3

a = int(input("ange första vinkeln: "))
b = int(input("ange andra vinkeln: ")) 
c = int(input("ange tredje vinkeln: "))
# kan också gör såhär: a, b, c = map(int, input("ange tre vinklar: ").split())

if a + b + c == 180:
    print("det är en triangel")
else:
    print("det är inte en triangel")



# övning 1.4

weight = float(input("Hur mycket väger du (kg): "))
age = float(input("Hur gammal är du: "))

if weight >= 40 or age > 12:
    print("1-2 piller rekommenderas")
elif 26 <= weight < 40 or 7 <= age <= 12:
    print("1/2-1 piller rekommenderas")
elif 15 <= weight <= 25 or 3 <= age < 7:
    print("1/2 piller rekommenderas")
else:
    print("Antingen är du för liten eller så har du inte angett rätta värden")



# övning 1.5

n = int(input("Skriv in ett nummer: "))

if n % 2 == 0 and n % 5 == 0:
    print(f"{n} är jämnt och kan delas med 5")
elif n % 5 == 0:
    print(f"{n} går att dela med 5")
elif n % 2 == 0:
    print(f"{n} är ett jämt tal")
else:
    print("Ditt tal är udda och går inta att dela med 5")



# övning 1.6

w = int(input("Hur mycket väger din väska: "))
l = int(input("Vilken mått har din väska(längd, bredd och höjd) i cm: "))
b = int(input(":"))
h = int(input(":"))

if w < 8 and l < 55 and b < 40 and h < 23:
    print("Välkommen")
else:
    print("Din packning är för stor")