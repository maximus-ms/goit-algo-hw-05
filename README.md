# GoITNeo Algo HW-5

## Task1
Add a ```delete(key)``` method for removing key-value pairs from the HashTable implemented in the outline.

### Solution
File ```HashTable.py```. Can be used as a module.
Class ```HashTable``` has methods:
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

### Solution
File ```BinarySearch.py```. Can be used as a module.

## Task3
Compare the efficiency of substring search algorithms: Boyer-Moore, Knuth-Morris-Pratt, and Rabin-Karp based on two text files:
 - article 1 file: "data/стаття1.txt" or (URL: https://drive.google.com/file/d/18_R5vEQ3eDuy2VdV3K5Lu-R-B-adxXZh/view?usp=sharing)
 - article 2 file: "data/стаття2.txt" or (URL: https://drive.google.com/file/d/13hSt4JkJc11nckZZz2yoFHYL89a4XkMZ/view?usp=sharing)

Using timeit, measure the execution time of each algorithm for two types of substrings: one that actually exists in the text and another - fictional (choose substrings as you wish). Based on the obtained data, determine the fastest algorithm for each text separately and overall.

### Solution
File ```TextSearch.py```. Can be used as a module.
We will do search for 3 words:
 - "наступні" - it appears in both texts (valid)
 - "абабагаламага" - it doesn't appear in texts (non-valid)
 - "наступні_" - it appears in texts, but with different ending (semi-valid)

### Results
```
Boyer-Moore        ( Txt_1, pattern valid      ) t = 0.043629
Boyer-Moore        ( Txt_1, pattern non-valid  ) t = 0.032874
Boyer-Moore        ( Txt_1, pattern semi-valid ) t = 0.063606
Boyer-Moore        ( Txt_2, pattern valid      ) t = 0.056799
Boyer-Moore        ( Txt_2, pattern non-valid  ) t = 0.048915
Boyer-Moore        ( Txt_2, pattern semi-valid ) t = 0.077471
Knuth-Morris-Pratt ( Txt_1, pattern valid      ) t = 0.129215
Knuth-Morris-Pratt ( Txt_1, pattern non-valid  ) t = 0.157702
Knuth-Morris-Pratt ( Txt_1, pattern semi-valid ) t = 0.146211
Knuth-Morris-Pratt ( Txt_2, pattern valid      ) t = 0.131663
Knuth-Morris-Pratt ( Txt_2, pattern non-valid  ) t = 0.203107
Knuth-Morris-Pratt ( Txt_2, pattern semi-valid ) t = 0.208664
Rabin-Karp         ( Txt_1, pattern valid      ) t = 0.276103
Rabin-Karp         ( Txt_1, pattern non-valid  ) t = 0.368551
Rabin-Karp         ( Txt_1, pattern semi-valid ) t = 0.330640
Rabin-Karp         ( Txt_2, pattern valid      ) t = 0.352691
Rabin-Karp         ( Txt_2, pattern non-valid  ) t = 0.508180
Rabin-Karp         ( Txt_2, pattern semi-valid ) t = 0.575210
```

### Conclusions
As result for our cases we have a list from best to worst:
 - "Boyer-Moore" - the fastest search method
 - "Knuth-Morris-Pratt"
 - "Rabin-Karp"

Also, it is important to mention that in most cases a searching for a pattern which mostly exists in a text but not fully is taking more time than a pattern which is doesn't appear in the text at all.
We have to understand, that different method are more suitable for different sizes of text and pattern.
