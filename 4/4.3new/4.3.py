import multiprocessing
import time
import sys
import codecs

def process_a(input_queue, output_queue):
    while True:
        if not input_queue.empty():
            message = input_queue.get()
            message_lower = message.lower()
            output_queue.put(message_lower)
            time.sleep(5)

def process_b(input_queue, output_queue):
    while True:
        if not input_queue.empty():
            message = input_queue.get()
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

    log_file = open("interaction_log_4_3.txt", "a")

    while True:
        # Read input from stdin
        user_input = input("Enter a message: ")
        timestamp = time.strftime("[%Y-%m-%d %H:%M:%S]")
        log_file.write(f"{timestamp} User input: {user_input}\n")
        if user_input == 'exit':
            break
        input_queue_to_a.put(user_input)

        # Check for messages from process B
        while not output_queue_from_b_to_main.empty():
            message_from_b = output_queue_from_b_to_main.get()
            timestamp = time.strftime("[%Y-%m-%d %H:%M:%S]")
            log_file.write(f"{timestamp} Message from Process B: {message_from_b}\n")
            print(f"[Main Process] Received message from Process B: {message_from_b}")

        # Ensure we're not overwhelming the CPU with too much polling
        time.sleep(0.1)

    log_file.close()
    # End the processes
    process_a_instance.terminate()
    process_b_instance.terminate()

if __name__ == "__main__":
    main()






