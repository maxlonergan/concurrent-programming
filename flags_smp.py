'''
downloads flags with multiprocessing parallelism
'''
import time
import requests
import multiprocessing


# global grand_total_bytes
# grand_total_bytes = 0
full_flag = []
byte_lyst = []


def download(lyst):
    grand_total_bytes = 0
    website = 'https://www.sciencekids.co.nz/images/pictures/flags680/'
    for item in lyst:
        flag = item + '.jpg'
        response = requests.get(website + flag)
        with open('./flags/flags_smp/'+flag, 'wb') as flag_name_file:
            flag_name_file.write(response.content)
            grand_total_bytes += len(response.content)
    byte_lyst.append(grand_total_bytes)

with open('./flags.txt', 'r') as ft:
    for line in ft:
        x = line[:-1]
        full_flag.append(x)
        first_half = full_flag[:len(full_flag)//2]
        second_half = full_flag[len(full_flag)//2:]


def main():

    time_start = time.perf_counter()

    process1 = multiprocessing.Process(target=download(first_half))
    process2 = multiprocessing.Process(target=download(second_half))
    process1.start()
    process2.start()
    time_stop = time.perf_counter()

    with open('flags_smp.out', 'w') as smp_out:
        smp_out.write(f'Elapsed time {time_stop - time_start}\n')
        smp_out.write(f'{sum(byte_lyst)} bytes downloaded')
if __name__ == '__main__':
    main()
