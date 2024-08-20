def kokonaisluvut():
    x = int(input("Anna ensimmäinen kokonaisluku: "))
    y = int(input("Anna toinen kokonaisluku: "))
    z = int(input("Anna kolmas kokonaisluku: "))
    summa = x + y + z
    tulo = x * y * z
    keskiarvo = summa / 3
    print(summa, tulo, keskiarvo)

kokonaisluvut()