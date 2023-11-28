import tkinter as tk


def topla_MKYLisans():
    if sayi1.get().strip() and sayi2.get().strip() and sayi1.get().replace(".", "").replace("-","").isdigit() and sayi2.get().replace(".", "").replace("-", "").isdigit():
        s1 = float(sayi1.get())
        s2 = float(sayi2.get())
        sonuc.configure(text=str(s1 + s2))
        hata_mesaji.configure(text="")
    else:
        hata_mesaji.configure(text="Hata: Lütfen geçerli sayılar girin.")

def cikar_MKYLisans():
    if sayi1.get().strip() and sayi2.get().strip() and sayi1.get().replace(".", "").replace("-","").isdigit() and sayi2.get().replace(".", "").replace("-", "").isdigit():
        s1 = float(sayi1.get())
        s2 = float(sayi2.get())
        sonuc.configure(text=str(s1 - s2))
        hata_mesaji.configure(text="")
    else:
        hata_mesaji.configure(text="Hata: Lütfen geçerli sayılar girin.")

def carpma_MKYLisans():
    if sayi1.get().strip() and sayi2.get().strip() and sayi1.get().replace(".", "").replace("-", "").isdigit() and sayi2.get().replace(".", "").replace("-", "").isdigit():
        s1 = float(sayi1.get())
        s2 = float(sayi2.get())
        sonuc.configure(text=str(s1 * s2))
        hata_mesaji.configure(text="")
    else:
        hata_mesaji.configure(text="Hata: Lütfen geçerli sayılar girin.")


def bolme_MKYLisans():
    if sayi1.get().strip() and sayi2.get().strip() and sayi1.get().replace(".", "").replace("-", "").isdigit() and sayi2.get().replace(".", "").replace("-", "").isdigit():
        s1 = float(sayi1.get())
        s2 = float(sayi2.get())
        sonuc.configure(text=str(s1 / s2))
        hata_mesaji.configure(text="")
    else:
        hata_mesaji.configure(text="Hata: Lütfen geçerli sayılar girin.")


def resetle_MKYLisans():
    sayi1.delete(0, tk.END)
    sayi2.delete(0, tk.END)
    sonuc.configure(text="")
    hata_mesaji.configure(text="")

def pencere_boyutunu_guncelle(event):
    genislik = event.width
    yukseklik = event.height
    print(f"Pencere Boyutu: {genislik} x {yukseklik}")

pencere = tk.Tk()
pencere.title('Hesap Makinesi MKYLisans')
pencere.bind("<Configure>", pencere_boyutunu_guncelle)
baslangic_genislik = 600
baslangic_yukseklik = 600
pencere.geometry(f"{baslangic_genislik}x{baslangic_yukseklik}")





font_style_MKY_lisans = ("Times New Roman", 24, "bold")



tus1 = tk.Button(pencere, text="+", font=font_style_MKY_lisans, command=topla_MKYLisans)
tus1.grid(row=2, column=0, padx=10, pady=10)

tus2 = tk.Button(pencere, text="-", font=font_style_MKY_lisans, command=cikar_MKYLisans)
tus2.grid(row=3, column=0, padx=10, pady=10)

tus3 = tk.Button(pencere, text="x", font=font_style_MKY_lisans, command=carpma_MKYLisans)
tus3.grid(row=4, column=0, padx=10, pady=10)

tus4 = tk.Button(pencere, text="/", font=font_style_MKY_lisans, command=bolme_MKYLisans)
tus4.grid(row=5, column=0, padx=10, pady=10)

tus5 = tk.Button(pencere, text="Temizle", font=font_style_MKY_lisans, command=resetle_MKYLisans)
tus5.grid(row=6, column=0, padx=10, pady=10)

sayi1 = tk.Entry(pencere, font="Courier 16 bold", width=15, justify="right")
sayi1.grid(row=0, column=0, padx=10, pady=10)

sayi2 = tk.Entry(pencere, font="Courier 16 bold", width=15, justify="right")
sayi2.grid(row=1, column=0, padx=10, pady=10)

sonuc = tk.Label(pencere, text="Sonuç: ", font="Courier 18 bold", width=30, justify="center")
sonuc.grid(row=7, column=0, columnspan=1, padx=10, pady=10)

hata_mesaji = tk.Label(pencere, text="")
hata_mesaji.grid(row=8, column=0, columnspan=2, padx=10, pady=10)


sayi1.focus()
pencere.mainloop()