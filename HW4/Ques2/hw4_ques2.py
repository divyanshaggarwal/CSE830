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

def TimSort(array, timsort_constant):
	if(len(array)<=1):
		return
	if(len(array) <= timsort_constant):
		insertionSort(array)
	else:
		mid = len(array)//2
		L = array[:mid]
		R = array[mid:]
		TimSort(L, timsort_constant)
		TimSort(R, timsort_constant)
		i = j = k = 0		 
		while i < len(L) and j < len(R):
			if L[i] < R[j]:
				array[k] = L[i]
				i+= 1
			else:
				array[k] = R[j]
				j+= 1
			k+= 1
		while i < len(L):
			array[k] = L[i]
			i+= 1
			k+= 1
		while j < len(R):
			array[k] = R[j]
			j+= 1
			k+= 1

# time_timsort = np.zeros((11,51))
# for n in range(0,51):
# 	time_timsort_n = []
# 	for t in range(1000):
# 		time_timsort_t = []
# 		array = np.random.randint(1000000, size=n)
# 		for k in range(0,51,5):
# 			start_time = time.perf_counter()
# 			TimSort(np.copy(array),k)
# 			stop_time = time.perf_counter()
# 			time_timsort_t.append(stop_time - start_time)
# 		time_timsort_n.append(time_timsort_t)
# 	time_timsort_n = np.array(time_timsort_n)
# 	time_timsort_n = np.mean(time_timsort_n, axis=0)
# 	time_timsort[:,n] = time_timsort_n

# # time_timsort = np.array(time_timsort)
# time_timsort = 1000. * time_timsort
# for k in range(0,51,5):
# 	plt.plot(range(0, 51), time_timsort[(k//5)], label='k=' + str(k))

# plt.xlabel('Length of Array (N)')
# plt.ylabel('Average Run time (ms)')
# plt.legend()
# plt.show()


optimal_k = 15
time_insertion_sort = []
time_merge_sort = []
time_timsort = []

for n in range(2, 51):
	avg_insertion_sort_time = 0.00
	avg_merge_sort_time = 0.00
	avg_timsort_time = 0.00
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

		start_time = time.perf_counter()
		TimSort(np.copy(array), optimal_k)
		stop_time = time.perf_counter()
		avg_timsort_time = avg_timsort_time + (stop_time - start_time)

	time_insertion_sort.append(avg_insertion_sort_time/1000.0)
	time_merge_sort.append(avg_merge_sort_time/1000.0)
	time_timsort.append(avg_timsort_time/1000.0)

time_insertion_sort = np.array(time_insertion_sort)
time_merge_sort = np.array(time_merge_sort)
time_timsort = np.array(time_timsort)

time_insertion_sort = 1000. * time_insertion_sort
time_merge_sort = 1000. * time_merge_sort
time_timsort = 1000. * time_timsort

plt.plot(range(2, 51), time_insertion_sort, label='Insertion Sort', color='#28324b')
plt.plot(range(2, 51), time_merge_sort, label='Merge Sort', color='#f55158')
plt.plot(range(2, 51), time_timsort, label='TimSort', color='#f3c417')

plt.xlabel('Length of Array (N)')
plt.ylabel('Average Run time (ms)')
plt.legend()
plt.show()