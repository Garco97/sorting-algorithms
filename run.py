from algorithms import bubble_sort, insertion_sort, merge_sort, quick_sort, selection_sort
from console import fg, bg, fx
import random
print(fg.green + "Introduzca número y pulse enter. Vacio y enter para empezar" + fg.default)
og_data = [1,2,3,4,5,6,7,8,9,10]
print("Input data:",fg.green + str(og_data) + fg.default)
random.shuffle(og_data)
print("Shuffled data:",fg.yellow + str(og_data) + fg.default)

data = og_data.copy()
print(fg.green + "bubble sort\n" + fg.default)
print(fg.green + str(bubble_sort(data)) + fg.default)
input()
data = og_data.copy()
print(fg.green + "insertion sort\n" + fg.default)
print(fg.green + str(insertion_sort(data)) + fg.default)
input()
data = og_data.copy()
print(fg.green + "merge sort\n" + fg.default)
print(fg.green + str(merge_sort(data)) + fg.default)
input()
data = og_data.copy()
print(fg.green + "quick sort\n" + fg.default)
print(fg.green + str(quick_sort(data)) + fg.default)
input()
data = og_data.copy()
print(fg.green + "selection sort\n" + fg.default)
print(fg.green + str(selection_sort(data)) + fg.default)
