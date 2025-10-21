/*
Kids With the Greatest Number of Candies (LC 1431)
There are n kids with candies. You are given an integer array candies, where each candies[i] represents
the number of candies the ith kid has, and an integer extraCandies, denoting the number of extra candies that you have.
Return a boolean array result of length n, where result[i] is true if, after giving the ith kid all 
the extraCandies, they will have the greatest number of candies among all the kids, or false otherwise.
Note that multiple kids can have the greatest number of candies.
*/
// array: input an array, output an array
// For each kid check if candies[i] + extraCandies ≥ maximum in Candies[i]
// Note: The returned array must be malloced, assume caller calls free().
#include <stdlib.h>
#include <stdbool.h>
bool* kidsWithCandies(int* candies, int candiesSize, int extraCandies, int* returnSize) {
    // must find max val manually
    int maxVal = candies[0];
    for (int i = 1; i < candiesSize; i++) {
        if (candies[i] > maxVal) {
            maxVal = candies[i];
        }
    }

    // array for result cant be declared like this int result[candiesSize] = {0}; bc size of the array must be a constant expression         
    bool* result = (bool*)malloc(candiesSize * sizeof(bool));
    if (!result) return NULL;  // check allocation

    for (int i = 0; i<candiesSize; i++){
        if (candies[i] + extraCandies >= maxVal){
            result[i] = true;
        }
        else {
            result[i] = false;
        }
    }

    // need to set returnSize var
    *returnSize = candiesSize;
    return result;
}

/*
Final Value of Variable After Performing Operations (LC 2011)
There is a programming language with only four operations and one variable X:
++X and X++ increments the value of the variable X by 1.
--X and X-- decrements the value of the variable X by 1.
Initially, the value of X is 0.
Given an array of strings operations containing a list of operations, 
return the final value of X after performing all the operations. 
*/
// There are only two operations to keep track of
// Use a variable to store the value after each operation
int finalValueAfterOperations(char** operations, int operationsSize) {
    int result = 0;

    for (int i = 0; i<operationsSize; i++){
        // check the middle character
        if (operations[i][1] == '+'){
            result++;
        }
        else{
            result--;
        }
    }

    return result;
}