sukupoli = input("Anna biolooginen sukupoli:")
sukupoli = sukupoli.lower()
hemoglobiiniarvo = int(input("Anna hemoglobiiniarvo arvo:"))

if sukupoli == "Nainen":
    if hemoglobiiniarvo >= 117 and hemoglobiiniarvo <= 175:
        print("Hemoglobiinin arvo on normaali.")
    elif hemoglobiiniarvo < 117:
        print("Hemoglobiinin arvo on alhainen")
    elif hemoglobiiniarvo > 175:
        print("Hemoglobiinin arvo on korkea")

if sukupoli == "Mies":
    if hemoglobiiniarvo >= 134 and hemoglobiiniarvo <= 195:
        print("Hemoglobiinin arvo on normaali.")
    elif hemoglobiiniarvo < 134:
        print("Hemoglobiinin arvo on alhainen")
    elif hemoglobiiniarvo > 195:
        print("Hemoglobiinin arvo on korkea")