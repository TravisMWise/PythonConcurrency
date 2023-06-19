from time import sleep
from multiprocessing import Process
 
# a simple task that blocks for a moment and prints a message
def task():
    for i in range(5):
        sleep(1)
        print(i, flush=True)
 
# entry point for the program
if __name__ == '__main__':
    process = Process(target=task)
    process.start()
    print('Waiting for the new process to finish...')
    process.join()