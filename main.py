'''
Этот модуль вычисляет сумму, максимальное и минимальное значение, а также самое часто встречаемое число в матрице (моду)
Сделано мной и учителем
'''


def matrix_result(matrix_numbers):
    matrix_sum = 0
    matrix_max = matrix_numbers[0][0]
    matrix_min = matrix_numbers[0][0]
    matrix_mode = 0
    frequencies = {}
    max_frequencies = (0, 0)

    for row in matrix_numbers:
        for i in row:
            if i > matrix_max:
                matrix_max = i
            if i < matrix_min:
                matrix_min = i
            if i not in frequencies:
                frequencies[i] = 1
            else:
                frequencies[i] += 1
            matrix_sum += i

    for i in frequencies.items():
        if i[1] > max_frequencies[1]:
            max_frequencies = i

    matrix_mode = max_frequencies[0]
    keys = {"sum": matrix_sum, "max": matrix_max, "min": matrix_min, "mode": matrix_mode}
    return keys


# Эта проверка выводит результат в консоль
if __name__ == "__main__":
    matrix_numbers = [[15, 2, 7, 8, 9, 10, 3, 5, 14, 11], [6, 12, 18, 4, 3, 9, 17, 11, 6, 2],
                      [13, 5, 8, 9, 1, 20, 6, 17, 3, 14], [7, 11, 4, 16, 10, 9, 2, 14, 8, 6],
                      [5, 3, 1, 6, 12, 7, 19, 8, 14, 15], [9, 13, 11, 15, 5, 7, 2, 6, 3, 10],
                      [2, 7, 13, 10, 9, 8, 5, 4, 12, 1], [6, 17, 9, 4, 3, 12, 14, 5, 8, 20],
                      [16, 5, 11, 13, 3, 9, 6, 8, 10, 1], [4, 18, 7, 9, 13, 11, 2, 3, 6, 8]]
    output = matrix_result(matrix_numbers)
    print(output)
