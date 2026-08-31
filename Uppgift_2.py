pris = [30, 28, 25, 23]
vikt = float(input("Hur mycket väger paketet(kg): "))

if vikt < 2:
    print("Det kommer att kosta " + str(pris[0] * vikt) + " Kr")
elif 2 <= vikt < 6:
    print("Det kommer att kosta " + str(pris[1] * vikt) + " Kr")
elif 6 <= vikt < 12:
    print("Det kommer att kosta " + str(pris[2] * vikt) + " Kr")
elif vikt >= 12:
    print("Det kommer att kosta " + str(pris[3] * vikt) + " Kr")
