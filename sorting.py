def list_sort(num_list):
  if len(num_list) <= 1:
    return num_list
  element = num_list[0]
  left = list(filter(lambda x : x < element, num_list))
  center = [i for i in num_list if i == element]
  right = list(filter(lambda x : x > element, num_list))
  return list_sort(left) + center + list_sort(right)

def index_search(num_list, number, start, end):
  if start > end:
    return f'Искомое число отсутствует в последовательности.\nИндекс числа, которое {"больше" if number < num_list[0] else "меньше"} искомого: {0 if number < num_list[0] else len(num_list) - 1}'
  middle = (start + end) // 2
  if num_list[middle] == number or (num_list[middle] > number and num_list[middle - 1] < number):
    return f'Индекс числа, которое больше или равно искомому: {middle}\nИндекс числа, которое меньше искомого: {middle - 1 if middle != 0 else "отсутствует в последовательности"}'
  if number < num_list[middle]:
    return index_search(num_list, number, start, middle - 1)
  else:
    return index_search(num_list, number, middle + 1, end) 

while True:
  try:
    list_of_numbers = list(map(int, input('Введите последовательность целых чисел через пробел:\n').split()))
    user_number = int(input('Введите искомое число: '))
  except ValueError:
    print('Необходимо вводить только целые числа! Попробуйте еще раз.')
    continue
  else:
    break
       
sorted_list = list_sort(list_of_numbers)
print(f'Последовательность чисел упорядочена по возрастанию:\n{sorted_list}')
print(index_search(sorted_list, user_number, 0, len(sorted_list) - 1))
