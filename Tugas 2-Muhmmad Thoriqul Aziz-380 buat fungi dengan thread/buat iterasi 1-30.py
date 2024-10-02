import threading
import time


sem = threading.Semaphore(1)


current_number = 2


def print_even_numbers(thread_id):
    global current_number
    while current_number <= 30:
        sem.acquire()
        try:
            if current_number <= 30:
                print(f"Thread {thread_id}: {current_number}")
                current_number += 2
                time.sleep(0.1)  # Mensimulasikan waktu eksekusi
        finally:
            sem.release()

# Membuat dan menjalankan 3 thread
threads = []
for i in range(3):
    thread = threading.Thread(target=print_even_numbers, args=(i+1,))
    threads.append(thread)

# Memulai semua thread
for thread in threads:
    thread.start()

# Menunggu semua thread selesai
for thread in threads:
    thread.join()
