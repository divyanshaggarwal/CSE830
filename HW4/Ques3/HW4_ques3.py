import random
from BTrees.OOBTree import OOBTree
import time
from matplotlib import pyplot as plt


hashtable_dict_time = []
btree_dict_time = []
insertions = []

num_insertions = 1
while (True):
	hashtable_dict = {}
	start_time = time.perf_counter()
	for n in range(num_insertions):
		hashtable_dict[n] = random.randint(0,1000000)
	stop_time = time.perf_counter()
	hashtable_dict_time.append(stop_time - start_time)

	btree_dict = OOBTree()
	start_time = time.perf_counter()
	for n in range(num_insertions):
		btree_dict.update({n:random.randint(0,1000000)})
	stop_time = time.perf_counter()
	btree_dict_time.append(stop_time - start_time)
	insertions.append(num_insertions)
	if(hashtable_dict_time[-1]>=3 or btree_dict_time[-1]>=3):
		break
	num_insertions = num_insertions * 10

plt.plot(insertions, hashtable_dict_time, label="Hash Table Backend Implementation",color='#28324b')
plt.plot(insertions, btree_dict_time, label="Binary Tree Backend Implementation", color='#f55158')
plt.xlabel('Number of Insertions (N)')
plt.xscale('log')
plt.ylabel('Insertion Time (seconds)')
plt.legend()
plt.show()