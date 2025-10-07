# övning 5.1

word = input("Skriv ett ord: ")

# (a)
print(len(word))

# (b)
upper = 0
lower = 0

for char in word:
    if char.isupper():
        upper += 1
    elif char.islower():
        lower += 1

print("Antal stora bokstäver: ", upper)
print("Antal små bokstäver: ", lower)



# övning 5.2

mening = "A picture says more than a thousand words, a matematical formula says more than a thousand pictures."
print(f"{mening} består av {len(mening.split())} ord")



# övning 5.3

text = input("Skriv ett eller flera ord för att se om det är ett palindrom: ")

cleanText = text.replace(" ","").lower()

if cleanText == cleanText[::-1]:
    print(text, "är ett palindrom")
else:
    print(text, "är inte ett palindrom")