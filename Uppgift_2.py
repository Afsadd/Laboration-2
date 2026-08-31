pris = [30, 28, 25, 23]
vikt = float(input("Hur mycket väger paketet(kg): "))

match [vikt < 2, 2 <= vikt < 6, 6 <= vikt < 12, vikt >= 12]:
    case True, False, False, False:
        print("Det kommer att kosta " + str(pris[0] * vikt) + " Kr")
    case False, True, False, False:
        print("Det kommer att kosta " + str(pris[1] * vikt) + " Kr")
    case False, False, True, False:
        print("Det kommer att kosta " + str(pris[2] * vikt) + " Kr")
    case False, False, False, True:
        print("Det kommer att kosta " + str(pris[3] * vikt) + " Kr")
