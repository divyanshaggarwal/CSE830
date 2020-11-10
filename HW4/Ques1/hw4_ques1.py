import math
import sys
import time
import numpy as np
from matplotlib import pyplot as plt

# https://www.geeksforgeeks.org/insertion-sort/
def insertionSort(arr): 
	for i in range(1, len(arr)): 
		key = arr[i] 
		j = i-1
		while j >= 0 and key < arr[j] : 
				arr[j + 1] = arr[j] 
				j -= 1
		arr[j + 1] = key

# https://www.geeksforgeeks.org/merge-sort/
def mergeSort(arr):
	if len(arr) >1:
		mid = len(arr)//2
		L = arr[:mid]
		R = arr[mid:]
		mergeSort(L)
		mergeSort(R)
		i = j = k = 0		 
		while i < len(L) and j < len(R):
			if L[i] < R[j]:
				arr[k] = L[i]
				i+= 1
			else:
				arr[k] = R[j]
				j+= 1
			k+= 1
		while i < len(L):
			arr[k] = L[i]
			i+= 1
			k+= 1
		while j < len(R):
			arr[k] = R[j]
			j+= 1
			k+= 1


time_insertion_sort = []
time_merge_sort = []

for n in range(2, 51):
	avg_insertion_sort_time = 0.00
	avg_merge_sort_time = 0.00
	for t in range(1000):
		array = np.random.randint(1000000, size=n)

		start_time = time.perf_counter()
		insertionSort(np.copy(array))
		stop_time = time.perf_counter()
		avg_insertion_sort_time = avg_insertion_sort_time + (stop_time - start_time)

		start_time = time.perf_counter()
		mergeSort(np.copy(array))
		stop_time = time.perf_counter()
		avg_merge_sort_time = avg_merge_sort_time + (stop_time - start_time)

	time_insertion_sort.append(avg_insertion_sort_time/1000.0)
	time_merge_sort.append(avg_merge_sort_time/1000.0)

time_insertion_sort = np.array(time_insertion_sort)
time_merge_sort = np.array(time_merge_sort)

time_insertion_sort = 1000. * time_insertion_sort
time_merge_sort = 1000. * time_merge_sort
plt.plot(range(2, 51), time_insertion_sort, label='Insertion Sort', color='#28324b')
plt.plot(range(2, 51), time_merge_sort, label='Merge Sort', color='#f55158')
plt.xlabel('Length of Array (N)')
plt.ylabel('Average Run time (ms)')
plt.legend()
plt.show()