vikt = float(input("Hur mycket väger paketet(kg): "))

sum = 0
pris = 0

if vikt < 12:
    pris = 25 + 2 * (vikt < 2) + 3 * (vikt < 6)
else:
    pris = 23 * vikt
sum += pris * vikt

print("Det kommer att kosta " + str(sum) + " kr.")
