import math 
import concurrent.futures 
import time  
import logging 

# настроййка системы логирования: все логи будут записываться в файл 'integration_log.txt' с уровнем INFO и форматом времени и сообщения
logging.basicConfig(filename='integration_log.txt', level=logging.INFO, format='%(asctime)s - %(message)s')

def integrate(f, a, b, *, n_jobs=1, n_iter=1000):
    start_time = time.time()

    acc = 0  # переменная для суммирования значений функции
    step = (b - a) / n_iter  # шаг интегрирования

    # создание пула потоков для выполнения параллельных задач с помощью ThreadPoolExecutor
    with concurrent.futures.ThreadPoolExecutor(max_workers=n_jobs) as executor:
        futures = []  
        # для каждой итерации выполняем асинхронное вычисление значения функции и добавляем его в список задач
        for i in range(n_iter):
            futures.append(executor.submit(f, a + i * step))
        for future in concurrent.futures.as_completed(futures):
            acc += future.result() * step

    end_time = time.time()

    # логируем завершение выполнения функции, указывая количество рабочих и время выполнения
    logging.info(f"Finished integration with {n_jobs} workers in {end_time - start_time} seconds")
    return acc

# Функция для сравнения времени выполнения интеграции с разным количеством рабочих
def compare_execution_times():
    cpu_num = 2 # количество ядер процессора
    n_iter = 1000  # количество итераций

    results = {}  

    # создание пула процессов для выполнения параллельных задач с помощью ProcessPoolExecutor
    with concurrent.futures.ProcessPoolExecutor() as executor:
        # проходим по различным значениям количества рабочих от 1 до двойного числа доступных ядер процессора
        for n_jobs in range(1, cpu_num * 2 + 1):
            start_time = time.time() 
            integrate(math.cos, 0, math.pi / 2, n_jobs=n_jobs, n_iter=n_iter)

            end_time = time.time()

            results[n_jobs] = end_time - start_time

    # Запись результатов сравнения времени выполнения в файл
    with open("execution_time_comparison.txt", "w") as f:
        f.write("Number of Workers (n_jobs) | Time (seconds)\n")
        for n_jobs, time_taken in results.items():
            f.write(f"{n_jobs} | {time_taken}\n")

compare_execution_times()

