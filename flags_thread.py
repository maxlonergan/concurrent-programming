'''
downloads flags using threads
'''
# look up thread pool execute function

import time
import requests
import threading

full_flag = []
byte_lyst = []

with open('./flags.txt', 'r') as ft:
    for line in ft:
        x = line[:-1]
        full_flag.append(x)
        first_half = full_flag[:len(full_flag)//2]
        second_half = full_flag[len(full_flag)//2:]

def download(lyst):
    grand_total_bytes = 0
    website = 'https://www.sciencekids.co.nz/images/pictures/flags680/'
    for item in lyst:
        flag = item + '.jpg'
        response = requests.get(website + flag)
        with open('./flags/flags_thread/'+flag, 'wb') as flag_name_file:
            flag_name_file.write(response.content)
            grand_total_bytes += len(response.content)
    byte_lyst.append(grand_total_bytes)

def main():
    time_start = time.perf_counter()
    thread1 = threading.Thread(target=download(first_half))
    thread2 = threading.Thread(target=download(second_half))

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()

    time_stop = time.perf_counter()

    with open('flags_thread.out', 'w') as thread_out:
        thread_out.write(f'Elapsed time {time_stop - time_start} \n')
        thread_out.write(f'{sum(byte_lyst)} bytes downloaded')

if __name__ == '__main__':
    main()
