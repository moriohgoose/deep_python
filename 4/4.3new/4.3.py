import multiprocessing
import time
from datetime import datetime
import sys
import codecs

def process_a(input_queue, output_queue):
# получает сообщение из входной очереди input_queue, 
# выводит его на экран с текущим временем и отправляет в нижнем регистре в выходную очередь output_queue, 
# после этого засыпает на 5 секунд
    while True:
        if not input_queue.empty():
            message = input_queue.get()
            timestamp = time.strftime("[%Y-%m-%d %H:%M:%S]")
            print(f"{timestamp} Message from Process A: {message}")
            message_lower = message.lower()
            output_queue.put(message_lower)
            time.sleep(5)


def process_b(input_queue, output_queue):
# получает сообщение из входной очереди input_queue, 
# выводит его на экран с текущим временем,
# кодирует его с помощью ROT13,
# отправляет в выходную очередь output_queue
    while True:
        if not input_queue.empty():
            message = input_queue.get()
            timestamp = time.strftime("[%Y-%m-%d %H:%M:%S]")
            print(f"{timestamp} Message from Process B: {message}")
            encoded_message = codecs.encode(message, 'rot_13')
            output_queue.put(encoded_message)


def main():
    input_queue_to_a = multiprocessing.Queue()
    output_queue_from_a_to_b = multiprocessing.Queue()
    output_queue_from_b_to_main = multiprocessing.Queue()

    process_a_instance = multiprocessing.Process(target=process_a, args=(input_queue_to_a, output_queue_from_a_to_b))
    process_b_instance = multiprocessing.Process(target=process_b, args=(output_queue_from_a_to_b, output_queue_from_b_to_main))

    process_a_instance.start()
    process_b_instance.start()

    for stdin in sys.stdin:
    # читает ввод из командной строки построчно (пока ввод есть) и отправляет каждую строку в input_queue_to_a. 
    # после этого получает закодированное сообщение из output_queue_from_b_to_main, выводит его на экран с текущим временем и повторяет цикл.
        stdin = stdin.strip()
        timestamp = time.strftime("[%Y-%m-%d %H:%M:%S]")
        print(f"{timestamp} Input in cmd: {stdin}")

        input_queue_to_a.put(stdin)

        message = output_queue_from_b_to_main.get()
        timestamp = time.strftime("[%Y-%m-%d %H:%M:%S]")
        print(f"{timestamp} Output in main: {message}\n")

    process_a_instance.terminate()
    process_b_instance.terminate()


if __name__ == "__main__":
    main()






