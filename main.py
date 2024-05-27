import os
import time
import urllib3
from urllib3.exceptions import TimeoutError
import keyboard
import sys

# Warnas untuk warna
hijau = '\033[92m'
biru = '\033[94m'
merah = '\033[91m'
kuning = '\033[93m'
putih = '\033[0m'

def tanya(nomor):
    os.system("cls")
    autoketik(f"{merah}Apa Anda Yakin Untuk Mengulang Spam ke {nomor}?")
    autoketik(f"{hijau}1. Ulang Spam ke {nomor}")
    autoketik(f"{hijau}2. Tidak")
    while True:
        if keyboard.is_pressed('1'):
            autoketik("Mengulang Spam ke Nomor: {}".format(nomor))
            start(nomor, 1)
            break
        elif keyboard.is_pressed('2'):
            autoketik("Tidak Mengulang Spam")
            sys.exit()
        else:
            pass

def autoketik(text):
    for c in text:
        print(c, end='', flush=True)
        time.sleep(0.02)
    print()

def jam(nomor):
    # Mulai mengulangi request HTTP
    while True:
        try:
            http = urllib3.PoolManager()
            response = http.request('GET', f'http://103.20.232.228/kasir.php?nama={nomor}&no=0&pin=0&ref=000000000000&ttd=', timeout=2.0)
            autoketik(f"{hijau}Response Code: {response.status}")
            time.sleep(5) # Tunda 5 detik
            autoketik("--Meminta Data Ke Server--")
        except urllib3.exceptions.MaxRetryError:
            autoketik("--Koneksi Gagal--")
            time.sleep(1000) # Tunda 1000 detik
            rto = 1
        except TimeoutError:
            autoketik("--Koneksi Timeout--")
            time.sleep(1000) # Tunda 1000 detik
            rto = 1
        except Exception as e:
            autoketik(f"{merah}--Kesalahan Terjadi--")
            autoketik(f"{merah}{e}")
            time.sleep(1000) # Tunda 1000 detik
            rto = 1
        finally:
            if rto == 1:
                time.sleep(5) # Tunda 5 detik

def start(nomor, jml):
    print(f"""{kuning}Author      : {hijau}Ricky Khairul Faza
{kuning}Github      : {merah}github.com/rickyfazaa
{kuning}Instagram   : {biru}instagram.com/rickyfazaa""")
    for i in range(jml):
        jam(nomor)

def main():
    os.system("cls")
    autoketik("--Masukkan Nomor Tujuan--")
    while True:
        try:
            nomor = input()
            if nomor:
                tanya(nomor)
            else:
                autoketik("--Nomor Tujuan Tidak Boleh Kosong--")
        except ValueError:
            autoketik("--Inputan Tidak Valid--")
        except Exception as e:
            autoketik(f"{merah}--Kesalahan Terjadi--")
            autoketik(f"{merah}{e}")
            sys.exit()
