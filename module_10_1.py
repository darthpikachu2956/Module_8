import threading as t
from time import sleep
from datetime import datetime


# word_count - количество записываемых слов
# file_name - название файла, куда будут записываться слова
def write_words(word_count, file_name):
    with open(file_name, 'a') as file:
        for i in range(1, word_count + 1):
            file.write(f"Word number {i}\n")
            sleep(0.1)
    print(f"The recording process into {file_name} has finished.")


start1 = datetime.now()
write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')
stop1 = datetime.now()
time_result1 = stop1 - start1
print(f"Time result: {time_result1}.\n")

start2 = datetime.now()
thr1 = t.Thread(target=write_words, args=(10, 'example5.txt'))
thr2 = t.Thread(target=write_words, args=(30, 'example6.txt'))
thr3 = t.Thread(target=write_words, args=(200, 'example7.txt'))
thr4 = t.Thread(target=write_words, args=(100, 'example8.txt'))
thr1.start()
thr2.start()
thr3.start()
thr4.start()
thr1.join()
thr2.join()
thr3.join()
thr4.join()
stop2 = datetime.now()
time_result2 = stop2 - start2
print(f"Time result: {time_result2}.\n")
