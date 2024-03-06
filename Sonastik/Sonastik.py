
import random

def loe_failist(fail: str) -> list:
    try:
        with open(fail, "r", encoding="utf-8") as f:
            jarjend = [rida.strip() for rida in f]
        return jarjend
    except FileNotFoundError:
        print(f"Faili {fail} ei leitud.")
        return []

def kirjuta_failist(fail: str, jarjend=None):
    if jarjend is None:
        jarjend = []
    
    try:
        with open(fail, "w", encoding="utf-8") as f:
            for element in jarjend:
                f.write(element + '\n')
    except Exception as e:
        print(f"Viga faili {fail} kirjutamisel: {e}")

def tõlgi(sõnastik, sõna, keel1, keel2):
    if sõna in sõnastik[keel1]:
        indeks = sõnastik[keel1].index(sõna)
        return sõnastik[keel2][indeks]
    else:
        print(f"{sõna} puudub sõnastikus. Kas soovite selle lisada?")
        vastus = input("Jah (j) / Ei (e): ").lower()
        if vastus == 'j':
            lisa_sõna(sõnastik, sõna, keel1, keel2)
            return tõlgi(sõnastik, sõna, keel1, keel2)
        else:
            return "Sõna ei leitud."

def lisa_sõna(sõnastik, sõna, keel1, keel2):
    uus_sõna = input(f"Sisestage tõlge sõnale '{sõna}' {keel2}-keelde: ")
    sõnastik[keel1].append(sõna)
    sõnastik[keel2].append(uus_sõna)
    print(f"Sõna '{sõna}' lisatud sõnastikku.")

def kontrolli_õigsust(sõnastik, keel1, keel2):
    õiged_vastused = 0
    kõik_sõnad = len(sõnastik[keel1])

    for i in range(kõik_sõnad):
        juhuslik_sõna = random.choice(sõnastik[keel1])
        print(f"Tõlkige sõna '{juhuslik_sõna}' {keel2}-keelde:")
        kasutaja_tõlge = input("Vastus: ")
        
        õige_tõlge = tõlgi(sõnastik, juhuslik_sõna, keel1, keel2)
        if kasutaja_tõlge == õige_tõlge:
            print("Õige!\n")
            õiged_vastused += 1
        else:
            print(f"Vale! Õige tõlge: {õige_tõlge}\n")

    protsent_õigsust = (õiged_vastused / kõik_sõnad) * 100
    print(f"Kontrolli õigsus: {protsent_õigsust}%")

rus = loe_failist("rus.txt")
est = loe_failist("est.txt")

def est_to_rus():
    sõna = input("Введите слово на эстонском: ")
    tõlge = tõlgi({"est": est, "rus": rus}, sõna, "est", "rus")
    print(f"Перевод на русский: {tõlge}")

def rus_to_est():
    sõna = input("Введите слово на русском: ")
    tõlge = tõlgi({"est": est, "rus": rus}, sõna, "rus", "est")
    print(f"Перевод на эстонский: {tõlge}")

print("1.Перевести с эстонского на русский")
print("2.Перевести с русского на эстонский")
print("3.Контроль знаний")

while True:
    valik = input("Выбор (1/2/3): ")
    if valik == '1':
        est_to_rus()
    elif valik == '2':
        rus_to_est()
    elif valik == '3':
        kontrolli_õigsust({"est": est, "rus": rus}, "est", "rus")
    else:
        print("Неверный выбор. Попробуйте еще раз.")

