# Longest Peak

- Write a function that takes in an array of int and returns the length of the longest peak in the array.

- A peak is defined as adjacent int in the array that are strictly increasing until they reach a tip and then begin to decrease

- Ex: [1, 4, 10, 2] forms a peak, but the int 4 ,0, 10 don't neigther do the int [1, 2, 2, 0]. similarly, the int [1, 2, 3] dont form a peak because there aren't strictly decreasing int after the 3.

- EX input :
array = [1, 2, 3, 3, 4, 0, 10, 6, 5 , -1, -3, 2, 3]

- EX output :
6 

- the ansswer is 6 because the peak that is the longest is [0, 10, 6, 5, -1, -3]