def pozdrav_ime(ime):
    return f"Pozdrav {ime}!"

dobrodosao_ime = lambda ime: f"Dobrodošao {ime}!"


def ispisi_dobrodoslicu(funkcija_za_dobrodoslicu, ime):
    poruka = funkcija_za_dobrodoslicu(ime)
    print(poruka)

ime = "Bože"

ispisi_dobrodoslicu(pozdrav_ime, ime)

ispisi_dobrodoslicu(dobrodosao_ime, ime)
