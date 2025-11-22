#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// Compute seed using an unsigned accumulator
unsigned int getSeed(void) {
    const char *key = "Gommage";
    unsigned int seed = 0;
    for (size_t i = 0; i < strlen(key); i++) {
        seed = seed * 31u + (unsigned char)key[i];
    }
    return seed;
}

// In-place Fisher–Yates shuffle of pw[0..pw_len-1]
void mutatePassword(char *pw, size_t pw_len, unsigned int seed) {
    if (pw_len == 0) return;
    srand(seed);
    for (size_t i = pw_len - 1; i > 0; i--) {
        size_t j = (size_t)(rand() % (i + 1));
        char tmp = pw[i];
        pw[i]     = pw[j];
        pw[j]     = tmp;
    }
}

void collectAllRanNums(int *randNums, size_t randNumsLen, unsigned int seed)
{
    srand(seed);
    
    for    reverseArray(randNums, len);
    revertMutation(comparePw, len, randNums);
    
    printf("%s\n", comparePw);
    
    for (size_t i = 0; i < len; i++)
    {
        printf("%d\n", randNums[i]);
    }
    
    
    return 0;
} (size_t i = 0; i < randNumsLen; i++)
    {
        randNums[i] = rand();
    }
}

void revertMutation(char *reverted, size_t revertedLen, int* randNums)
{
    for (size_t i = 1; i < revertedLen; i++)
    {
        int randNum = randNums[i];
        int rem = randNum % (i + 1);
        char tmp = reverted[i];
        reverted[i] = reverted[rem];
        reverted[rem] = tmp;
    }
}

void reverseArray(int *arr, size_t len) {
    size_t i = 0;
    size_t j = len ? len - 1 : 0;
    while (i < j) {
        int tmp = arr[i];
        arr[i] = arr[j];
        arr[j] = tmp;
        i++;
        j--;
    }
}

int main(void) {
    unsigned int seed = getSeed();

    // Allocate a writable copy, including the trailing '\0'
    // char pw[] = "nyanpham";
    // size_t len = strlen(pw);

    //mutatePassword(pw, len, seed);
    //printf("Mutated password: %s\n", pw);
    
    char comparePw[] = "Ygta_u3G_t0h_0aG_r3";
    size_t len = strlen(comparePw);
    int randNums[len];
    
    collectAllRanNums(randNums, len, seed);
    reverseArray(randNums, len);
    revertMutation(comparePw, len, randNums);
    
    printf("%s\n", comparePw);
    
    return 0;
}

