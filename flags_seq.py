'''
downloads flags sequentially
'''
import time
import requests

time_start = time.perf_counter()

flag_txt = []
total_bytes = 0

with open('./flags.txt', 'r') as ft:
    for line in ft:
        x = line[:-1]
        flag_txt.append(x)

website = 'https://www.sciencekids.co.nz/images/pictures/flags680/'

for item in flag_txt:
    flag = item + '.jpg'
    response = requests.get(website + flag)
    with open('./flags/flags_seq/'+flag, 'wb') as flag_name_file:
        flag_name_file.write(response.content)
        total_bytes += len(response.content)
time_stop = time.perf_counter()

print(f'Elapsed time: {round(time_stop-time_start, 2)} seconds')
print(f'{total_bytes} bytes downloaded')

with open('flags_seq.out', 'w') as seq_out:
    seq_out.write(f'Elapsed time: {time_stop-time_start} seconds \n')
    seq_out.write(f'{total_bytes} bytes downloaded')