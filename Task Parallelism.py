import threading
import time

# Task 1

def addition():
    for i in range(1, 6):
        print(f"Penjumlahan: {i} + {i} = {i+i}")
        time.sleep(1)

# Task 2

def multiplication():
    for i in range(1, 6):
        print(f"Perkalian: {i} x {i} = {i*i}")
        time.sleep(1)

# Task 3

def subtraction():
    for i in range(1, 6):
        print(f"Pengurangan: {i} - 1 = {i-1}")
        time.sleep(1)

# Membuat thread
thread1 = threading.Thread(target=addition)
thread2 = threading.Thread(target=multiplication)
thread3 = threading.Thread(target=subtraction)

# Menjalankan thread
thread1.start()
thread2.start()
thread3.start()

# Menunggu semua thread selesai
thread1.join()
thread2.join()
thread3.join()

print("\nSemua task selesai dijalankan")