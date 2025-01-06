from multiprocessing import Pool
from datetime import datetime

def read_info(name):
    all_data = []
    with open(name, 'r', encoding='UTF-8') as f:
        while True:
            data = f.readline()
            if not data:
                break
            all_data.append(data.strip())
filenames = [f'./file {number}.txt' for number in range(1, 5)]

# Линейный вызов
start_lin = datetime.now()
for name in filenames:
    read_info(name)
end_lin = datetime.now()
print(f'Линейный вызов: {end_lin - start_lin}')

# Многопроцессный
# if __name__ == '__main__':
#     start_multi = datetime.now()
#     with Pool(4) as p:
#         p.map(read_info, filenames)
#     end_multi = datetime.now()
#     print(f'Многопроцессный вызов: {end_multi - start_multi}')