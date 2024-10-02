import threading

def hitung_luas_segitiga(alas, tinggi):
    luas = 0.5 * alas * tinggi
    print(f"Luas segitiga dengan alas {alas} dan tinggi {tinggi} adalah: {luas}")


def hitung_luas_persegi_panjang(panjang, lebar):
    luas = panjang * lebar
    print(f"Luas persegi panjang dengan panjang {panjang} dan lebar {lebar} adalah: {luas}")


def main():
    thread_segitiga = threading.Thread(target=hitung_luas_segitiga, args=(20, 5))
    
    
    thread_persegi_panjang = threading.Thread(target=hitung_luas_persegi_panjang, args=(12, 6))
    
    # Menjalankan thread
    thread_segitiga.start()
    thread_persegi_panjang.start()
    
    # Menunggu kedua thread selesai
    thread_segitiga.join()
    thread_persegi_panjang.join()

# Menjalankan fungsi main
if __name__ == "__main__":
    main()
