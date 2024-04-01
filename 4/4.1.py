import threading
import multiprocessing
import time


def fibonacci(n): # функция для вычисления чисел Фибоначчи
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)


def fibonacci_threading(n): # функция для запуска вычислений в потоках
    threads = []
    for _ in range(10):
        t = threading.Thread(target=fibonacci, args=(n,))
        threads.append(t)
        t.start()
    for t in threads:
        t.join()


def fibonacci_multiprocessing(n): # функция для запуска вычислений в процессах
    processes = []
    for _ in range(10):
        p = multiprocessing.Process(target=fibonacci, args=(n,))
        processes.append(p)
        p.start()
    for p in processes:
        p.join()


def run_comparison(): # функция для сравнения времени выполнения
    n = 32  # большое число для наглядности разницы во времени выполнения

    with open("4_1.txt", "w") as file:
        # синхронный запуск
        start_time = time.time()
        for _ in range(10):
            fibonacci(n)
        sync_time = time.time() - start_time
        file.write(f"Синхронный запуск: {sync_time}\n")

        # запуск с использованием threading
        start_time = time.time()
        for _ in range(10):
            fibonacci_threading(n)
        threading_time = time.time() - start_time
        file.write(f"Потоки: {threading_time}\n")

        # запуск с использованием multiprocessing
        start_time = time.time()
        for _ in range(10):
            fibonacci_multiprocessing(n)
        multiprocessing_time = time.time() - start_time
        file.write(f"Процессы: {multiprocessing_time}\n")

if __name__ == "__main__":
    run_comparison()