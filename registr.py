import tkinter as tk
from tkinter import messagebox
from tkinter import Entry, Label, Button, Radiobutton, Tk
import random
import string

kasutajad = []
paroolid = []
file_path = "andmebaas.txt"
parooli_valiku_valik = []
uue_parooli_valiku_valik = []

def registreeri():
    kasutajanimi = kasutajanimi_sisend.get()
    if kasutajanimi in kasutajad:
        messagebox.showerror("Viga", "Sellise nimega kasutaja juba eksisteerib!")
        return

    parooli_valik = parooli_valiku_valik.get()

    if parooli_valik == 1:
        parool = genereeri_parool()
        messagebox.showinfo("Info", f"Automaatselt genereeritud parool: {parool}")
    elif parooli_valik == 2:
        parool = parooli_sisend.get()
        if not kontrolli_parooli(parool):
            messagebox.showerror("Viga", "Parool ei vasta nõuetele!")
            return
    else:
        messagebox.showerror("Viga", "Vigane valik!")
        return

    kasutajad.append(kasutajanimi)
    paroolid.append(parool)
    salvesta_sõnastik(kasutajad, paroolid, file_path)
    messagebox.showinfo("Info", "Registreerimine õnnestus!")
    tühjenda_sisendid()

def autoriseeri():
    kasutajanimi = kasutajanimi_sisend.get()
    parool = parooli_sisend.get()
    if kasutajanimi in kasutajad:
        indeks = kasutajad.index(kasutajanimi)
        if paroolid[indeks] == parool:
            messagebox.showinfo("Info", "Autoriseerimine õnnestus!")
            tühjenda_sisendid()
            return

    messagebox.showerror("Viga", "Vale kasutajanimi või parool!")
    tühjenda_sisendid()

def muuda_andmeid():
    kasutajanimi = kasutajanimi_sisend.get()
    parool = parooli_sisend.get()

    if kasutajanimi in kasutajad:
        indeks = kasutajad.index(kasutajanimi)
        if paroolid[indeks] == parool:
            uus_kasutajanimi = uus_kasutajanimi_sisend.get()
            if uus_kasutajanimi in kasutajad:
                messagebox.showerror("Viga", "Kasutaja sellise nimega juba eksisteerib!")
                return
            uue_parooli_valik = uue_parooli_valiku_valik.get()
            if uue_parooli_valik == 1:
                uus_parool = genereeri_parool()
            elif uue_parooli_valik == 2:
                uus_parool = uus_parooli_sisend.get()
                if not kontrolli_parooli(uus_parool):
                    messagebox.showerror("Viga", "Uus parool ei vasta nõuetele!")
                    return
            else:
                messagebox.showerror("Viga", "Vigane valik!")
                return

            kasutajad[indeks] = uus_kasutajanimi
            paroolid[indeks] = uus_parool
            salvesta_sõnastik(kasutajad, paroolid, file_path)
            messagebox.showinfo("Info", "Andmed on edukalt muudetud!")
            messagebox.showinfo("Info", f"Automaatselt genereeritud parool: {parool}")
            tühjenda_sisendid()
            return

    messagebox.showerror("Viga", "Vale kasutajanimi või parool!")
    tühjenda_sisendid()

def unustasid_parooli():
    kasutajanimi = kasutajanimi_sisend.get()

    if not kasutajanimi:
        messagebox.showerror("Viga", "Palun sisesta kasutajanimi.")
        return

    kasutajad, paroolid = laadi_sõnastik(file_path)

    if kasutajanimi in kasutajad:
        indeks = kasutajad.index(kasutajanimi)
        uus_parool = genereeri_parool()
        paroolid[indeks] = uus_parool
        salvesta_sõnastik(kasutajad, paroolid, file_path)
        messagebox.showinfo("Info", f"Uus parool genereeritud: {uus_parool}")
        tühjenda_sisendid()
        return

    messagebox.showerror("Viga", "Vale kasutajanimi.")
    tühjenda_sisendid()

def genereeri_parool():
    pikkus = random.randint(8, 12)
    märgid = string.ascii_letters + string.digits + string.punctuation
    parool = ''.join(random.choice(märgid) for _ in range(pikkus))
    return parool

def kontrolli_parooli(parool):
    if len(parool) < 8:
        return False
    if not any(char.isdigit() for char in parool):
        return False
    if not any(char.isalpha() for char in parool):
        return False
    return True

def salvesta_sõnastik(kasutajad, paroolid, faili_tee):
    with open(faili_tee, "a", encoding="utf-8") as fail:
        for kasutajanimi, parool in zip(kasutajad, paroolid):
            fail.write(f"{kasutajanimi}:{parool}\n")

def laadi_sõnastik(faili_tee):
    kasutajad = []
    paroolid = []
    with open(faili_tee, "r", encoding="utf-8-sig") as fail:
        for rida in fail:
            rida = rida.strip().split(":")
            kasutajanimi = rida[0]
            parool = rida[1]
            kasutajad.append(kasutajanimi)
            paroolid.append(parool)
    return kasutajad, paroolid

def tühjenda_sisendid():
    kasutajanimi_sisend.delete(0, tk.END)
    parooli_sisend.delete(0, tk.END)
    uus_kasutajanimi_sisend.delete(0, tk.END)
    uus_parooli_sisend.delete(0, tk.END)

root = tk.Tk()
root.title("Kasutaja haldus")
root.geometry("400x600")
root.configure(bg="#ffedbd")



menüü_silt = tk.Label(root, text="Menüü:", fg="black", font=("Arial", 14, "bold"), bg="#ffedbd")
menüü_silt.pack()

kasutajanimi_silt = tk.Label(root, text="Kasutajanimi:", font=("Arial", 14, "bold"), bg="#ffedbd")
kasutajanimi_silt.pack()

kasutajanimi_sisend = tk.Entry(root)
kasutajanimi_sisend.pack()

parooli_valiku_silt = tk.Label(root, text="Parooli valik:", font=("Arial", 14, "bold"), bg="#ffedbd")
parooli_valiku_silt.pack()

parooli_valik = tk.IntVar()

automaatne_parool_nupp = tk.Radiobutton(root, text="Automaatne", variable=parooli_valik, value=1, font=("Arial", 14, "bold"), bg="#ffedbd")
automaatne_parool_nupp.pack()

käsitsi_parool_nupp = tk.Radiobutton(root, text="Käsitsi", variable=parooli_valik, value=2, font=("Arial", 14, "bold"), bg="#ffedbd")
käsitsi_parool_nupp.pack()

parooli_silt = tk.Label(root, text="Parool:", font=("Arial", 14, "bold"), bg="#ffedbd")
parooli_silt.pack()

parooli_sisend = tk.Entry(root, show="*")
parooli_sisend.pack()

uus_kasutajanimi_silt = tk.Label(root, text="Uus kasutajanimi:", font=("Arial", 14, "bold"), bg="#ffedbd")
uus_kasutajanimi_silt.pack()

uus_kasutajanimi_sisend = tk.Entry(root)
uus_kasutajanimi_sisend.pack()

uus_parooli_silt = tk.Label(root, text="Uus parool:", font=("Arial", 14, "bold"), bg="#ffedbd")
uus_parooli_silt.pack()

uus_parooli_sisend = tk.Entry(root, show="*")
uus_parooli_sisend.pack()

registreeri_nupp = tk.Button(root, text="Registreeri", command=registreeri, font=("Arial", 14, "bold"), bg="#f5cd62")
registreeri_nupp.pack()

autoriseeri_nupp = tk.Button(root, text="Autoriseeri", command=autoriseeri, font=("Arial", 14, "bold"), bg="#f5cd62")
autoriseeri_nupp.pack()

muuda_nupp = tk.Button(root, text="Andmete muutmine", command=muuda_andmeid, font=("Arial", 14, "bold"), bg="#f5cd62")
muuda_nupp.pack()

unustasid_parooli_nupp = tk.Button(root, text="Unustasid parooli?", command=unustasid_parooli, font=("Arial", 14, "bold"), bg="#f5cd62")
unustasid_parooli_nupp.pack()

root.mainloop()
