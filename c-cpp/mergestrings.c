/*
Merge Strings Alternately (LC 1768)
You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, 
starting with word1. If a string is longer than the other, append the additional letters onto the end 
of the merged string.
Return the merged string.
SOLUTION IN C
*/
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char * mergeAlternately(char * word1, char * word2){
    // find lengths of the input words
    size_t n1 = strlen(word1);
    size_t n2 = strlen(word2);

    // allocate enough space for all chars + null terminator (1 byte)
    // the null terminator ('\0') exists because in C strings are just arrays of characters
    char *out = (char*)malloc(n1 + n2 + 1);     // pointer to a char stored in out
    if (!out) return NULL;          // if malloc failed (out is NULL) return NULL

    // iterate over both words
    size_t i = 0;    // shared index for input strings
    size_t k = 0;    // index for writing to 'out'

    // keep looping as long as i < n1 or i <n2, until i has reached the end of both strings
    for (; i < n1 || i < n2; ++i) {             // for (initialization; condition; update)
        if (i < n1){                            // copy word1[i] into out[k] and increment k
            out[k] = word1[i];
            k = k + 1;
        };
        if (i < n2) out[k++] = word2[i];        // take next char from word2 if available
    }

    // terminate with '\0' so its a valid C string
    out[k] = '\0';

    return out;     // return pointer
}


char* mergeAlternately_ptr(char* word1, char* word2) {
    // find lengths for allocation
    size_t n1 = strlen(word1);
    size_t n2 = strlen(word2);
    char *out = (char*)malloc(n1 + n2 + 1);
    if (!out) return NULL;

    // set up three moving pointers
    char *p1 = word1;           // points to the current character in word1
    char *p2 = word2;           // reads characters from word2
    char *po = out;             // points to where you’ll write next in output buffer

    // alternate characters while both words still have data
    while (*p1 && *p2) {        // while both word1 and word2 still have characters left (until hits '\0')
        *po = *p1;              // copy the character from word1 into out
        po = po + 1;            // move to next position in out
        p1 = p1 + 1;            // move to next position in word1

        *po++ = *p2++;          // copy char from word2, then advance both pointers
    }

    // append any leftovers (if one string is longer)
    while (*p1 != '\0') {
        *po = *p1;              // copy current char from word1 to out
        po = po + 1;
        p1 = p1 + 1;
    }
    while (*p2) *po++ = *p2++;   // copy remaining word2 chars

    // terminate with '\0'
    *po = '\0';

    return out;
}