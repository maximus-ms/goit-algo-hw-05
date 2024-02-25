# GoITNeo Algo HW-5

## Task1
Add a ```delete(key)``` method for removing key-value pairs from the HashTable implemented in the outline.

### Solution
File ```HashTable.py```. Can be used as a module.
Class ```HashTable``` has a set of methods:
 - ```insert(key, value)``` - add a new item or update if exist. Return True.
 - ```get(key)``` - get value for a *key* or ```None``` if doesn't exist.
 - ```delete(key)``` - delete *(key, value)* and return ```True```. Return ```False``` if *key* doesn't exist.
 - ```get_hash(key)``` - return a hash value of a *key*.

#### How to use:
```python
import HashTable

ht = HashTable(5)
ht.insert("apple", 10)
ht.insert("orange", 20)

ht.get("apple")
ht.get("orange")

ht.delete("orange")
```

## Task2
Implement binary search for a sorted array of floating-point numbers. The binary search function should return a tuple, where the first element is the number of iterations needed to find the element. The second element should be the 'upper bound' - the smallest element that is greater than or equal to the given value.

## Task3
Compare the efficiency of substring search algorithms: Boyer-Moore, Knuth-Morris-Pratt, and Rabin-Karp based on two text files:
 - article 1 (https://drive.google.com/file/d/18_R5vEQ3eDuy2VdV3K5Lu-R-B-adxXZh/view?usp=sharing)
 - article 2 (https://drive.google.com/file/d/13hSt4JkJc11nckZZz2yoFHYL89a4XkMZ/view?usp=sharing)
Using timeit, measure the execution time of each algorithm for two types of substrings: one that actually exists in the text and another - fictional (choose substrings as you wish). Based on the obtained data, determine the fastest algorithm for each text separately and overall.

