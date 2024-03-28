import time
import sys
from multiprocessing import Process, Queue
import codecs
import select

def process_a(input, output):
    while True:
        message = input.get()
        processed_message = message.lower()
        output.put(processed_message)
        if message == "exit":
            break
        time.sleep(5)

def process_b(input, output):
    while True:
        message = input.get()
        if message == "exit":
            break
        encoded_message = codecs.encode(message, 'rot_13')
        output.put(encoded_message)

def main():
    queue_a = Queue()
    queue_b = Queue()
    main_queue = Queue()

    process_a_obj = Process(target=process_a, args=(queue_a, queue_b))
    process_b_obj = Process(target=process_b, args=(queue_b, main_queue))

    process_a_obj.start()
    process_b_obj.start()

    while True:
        if sys.stdin in select.select([sys.stdin], [], [], 0)[0]:
            message = sys.stdin.readline().strip()
            if (message == "terminate"):
                break
            print(f"{time.strftime('%H:%M:%S')} - send {message}")
            queue_a.put(message)

        while not main_queue.empty():
            encoded_message = main_queue.get()
            print(f"{time.strftime('%H:%M:%S')} - receive {encoded_message}")

    process_a_obj.terminate()
    process_b_obj.terminate()

if __name__ == "__main__":
    main()