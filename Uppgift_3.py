packages_to_send = int(input("Hur många paket vill du skicka? "))
weight_of_packages = []

while len(weight_of_packages) < packages_to_send:
    current_package = float(
        input("Ange vikt för paket " + str(len(weight_of_packages) + 1) + ": ")
    )
    weight_of_packages.append(current_package)

i = 0
sum = 0
pris = 0
while i < len(weight_of_packages):
    if weight_of_packages[i] < 12:
        pris = (
            25
            + 2 * bool((weight_of_packages[i] < 2))
            + 3 * bool((weight_of_packages[i] < 6))
        )
    else:
        pris = 23 * bool(weight_of_packages[i])
    sum += pris * weight_of_packages[i]
    i += 1

print("Det kommer att kosta " + str(round(sum)) + " kr.")
