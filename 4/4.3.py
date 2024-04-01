import multiprocessing
import time
import codecs


def process_a(queue_ab, pipe_ab):
    """Функция получает сообщение из очереди (queue_ab), преобразует его в нижний регистр,
    кладет обратно в очередь и отправляет в процесс B через канал pipe_ab.
    Выполняется до тех пор, пока не получит сообщение 'STOP'"""
    while True:
        message = queue_ab.get()
        if message == 'STOP':
            pipe_ab.send('STOP')
            break
        message_lower = message.lower()
        pipe_ab.send(message_lower)
        time.sleep(5)


def process_b(pipe_ab, queue_b_main):
    """Функция получает сообщение из канала (pipe_ab),
    кодирует его с помощью ROT13 и отправляет обратно в главный процесс через очередь queue_b_main.
    Выполняется до тех пор, пока не получит сообщение 'STOP'"""
    while True:
        message = pipe_ab.recv()
        if message == 'STOP':
            queue_b_main.put('STOP')
            break
        encoded_message = codecs.encode(message, 'rot_13')
        queue_b_main.put(encoded_message)


if __name__ == "__main__":
    queue_ab = multiprocessing.Queue()  # очередь для обмена сообщениями между процессами A и главным процессом
    queue_b_main = multiprocessing.Queue()  # очередь для обмена сообщениями между процессами B и главным процессом
    pipe_ab, pipe_ba = multiprocessing.Pipe()  # канал для обмена сообщениями между процессами A и B

    process_a_instance = multiprocessing.Process(target=process_a, args=(queue_ab, pipe_ab))
    process_b_instance = multiprocessing.Process(target=process_b, args=(pipe_ba, queue_b_main))

    process_a_instance.start()
    process_b_instance.start()

    while True:
        try:
            message = input("Enter a message: ")
            if message.lower() == 'stop':
                queue_ab.put('STOP')
                break

            else:
                queue_ab.put(message)
                received_message = queue_b_main.get()
                print(f"Encoded message: {received_message}")

                with open('interaction_log.txt', 'a') as f:
                    f.write(f"{time.strftime('%Y-%m-%d %H:%M:%S')} - {message} - {received_message}\n")

        except KeyboardInterrupt:
            queue_ab.put('STOP')
            break

    process_a_instance.join()
    process_b_instance.join()

