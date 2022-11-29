
import requests
import time

time_start = time.perf_counter()

flag_txt = []
total_bytes = 0


with open('./flags.txt', 'r') as ft:
    for line in ft:
        x = line[:-1]
        flag_txt.append(x)

website = 'https://www.sciencekids.co.nz/images/pictures/flags680/'


# for item in flag_txt:
#     flag = item + '.jpg'
#     response = requests.get(website + flag)
flag = 'Afghanistan.jpg'
with open('./flags/'+flag, 'wb') as flag_name_file:
    print('it works')

time_stop = time.perf_counter()

print(f'Elapsed time: {time_stop-time_start} seconds')
