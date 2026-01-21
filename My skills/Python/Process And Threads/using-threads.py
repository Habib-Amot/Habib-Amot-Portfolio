import queue
import threading
from multi_processing import get_opt, get_files

def main():
    file_queue = queue.Queue()  # queue to hold the files that are found in the folders and subfolder
    command_line_opts = get_opt()
    print(command_line_opts)
    filelist = get_files(command_line_opts.locations, recurse_dir=True)

    # creating the threads that will handle the processing of the files
    for count in range(command_line_opts.threads):
        thread = Worker_Thread(file_queue, command_line_opts.search_word)
        thread.daemon = True
        thread.start()
    
    # putting each filename in the Queue
    for file in filelist:
        file_queue.put(file)


class Worker_Thread(threading.Thread):
    def __init__(self, queue: queue.Queue, word_to_search):
        super().__init__()
        self.queue = queue
        self.word_to_search = word_to_search
    

    def run(self):
        CHUNK_SIZE = 1000
        while True:
            if self.word_to_search:  # checking if there is any file in the queue
                filename = self.queue.get()
                print(filename)
                try:
                    with open(filename, 'rb') as file:
                        chunk = file.read(CHUNK_SIZE)
                        if not chunk:
                            break
                        if self.word_to_search in chunk.decode('utf8', 'ignore'):
                            print("{0:.<24}{1}".format(self.word_to_search, file))
                            print(filename)
                            break
                        if len(chunk) < CHUNK_SIZE:
                            break
                except EnvironmentError as err:
                    print(err)
                finally:
                    self.queue.task_done()


if __name__ == '__main__':
    main()
