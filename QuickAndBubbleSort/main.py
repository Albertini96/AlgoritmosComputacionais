# -*- coding: utf-8 -*-

import Sort


#Sort.testAlgorithms([10, 20, 30, 40, 50, 60])

test = [3,2,3,4,45,66,1,22,42]

#Sort.Bubble(test)
Sort.QuickSort(test, 0, len(test) - 1, rand = True)
print(test)