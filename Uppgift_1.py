distance = float(input("Ange körsträcka i km: "))
fuel = float(input("Ange förbrukat bränsle i liter: "))
print(
    "Bränsleförbrukningen för bilen är "
    + str(round(100 * fuel / distance, 3))
    + " l/100 km"
)
