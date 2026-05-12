from multiprocessing import Pool
import time

def square_number(x):
    print(f"Processing data: {x}")
    time.sleep(1)
    return x * x

if __name__ == "__main__":
    numbers = [1, 2, 3, 4, 5, 6, 7, 8]

    start = time.time()

    with Pool() as p:
        result = p.map(square_number, numbers)

    end = time.time()

    print("Hasil:", result)
    print("Waktu eksekusi:", end - start)