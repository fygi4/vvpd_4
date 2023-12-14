from typing import List

def syracuse_sequence(n: int) -> List[int]:
    sequence = [n]
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        sequence.append(n)
    return sequence

def syracuse_max(n: int) -> int:
    sequence = syracuse_sequence(n)
    max_num = sequence[0]
    for num in sequence:
        if num > max_num:
            max_num = num
    return max_num

def main():
    while True:
        print('___________________________________________________')
        print('[1] - Ввести новое число')
        print('[2] - Выход')
        choice = input('Выберите опцию:')
        print('___________________________________________________')

        if choice == '1':
            try:
                number = int(input('Введите натуральное число:'))
                if number > 0:
                    print(f'Последовательность для числа {number}: {syracuse_sequence(number)}')
                    print(f'Максимальное значение в последовательности:{syracuse_max(number)}')
                elif number == 0:
                    print('Нужно натуральное число')
                else:
                    print('Введите положительное число')
            except ValueError:
                print('Введите целое число')
        elif choice == '2':
            print('Выход ')
            break
        else:
            print('Некорректный выбор')


if __name__ == "__main__":
    main()
