from datetime import datetime
from multiprocessing import Pool


def read_info(name):
    all_data = []
    with open(name, 'r') as file:
        while True:
            line = file.readline()
            if line == '':
                break
            all_data.append(line)


if __name__ == "__main__":
    filenames = [f'./file {number}.txt' for number in range(1, 5)]
    time_start = datetime.now()
    for name in filenames:
        read_info(name)
    print(f'Время работы (Линейный вызов): {datetime.now() - time_start}')

    time_start = datetime.now()
    with Pool(5) as pool:
        pool.map(read_info, filenames)
    print(f'Время работы (многопроцессный вызов) : {datetime.now() - time_start}')
