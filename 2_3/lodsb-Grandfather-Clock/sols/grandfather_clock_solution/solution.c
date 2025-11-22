#include <stdio.h>
#include <stdlib.h>

#define KEY_LENGTH 28

int main(void) {
    char key[KEY_LENGTH + 1];
    char flag[KEY_LENGTH + 1];
    FILE *fd;

    if ((fd = fopen("grandfather_clock", "rb")) == NULL) {
        puts("error opening file [grandfather_clock]");
        exit(EXIT_FAILURE);
    } 

    fseek(fd, 0x2020, SEEK_SET);
    fread(key, 1, KEY_LENGTH, fd);

    fclose(fd);

    key[KEY_LENGTH] = 0;

    for (int i = 0, j = KEY_LENGTH - 1, k = -2; i < KEY_LENGTH; ++i) {
        flag[j] = key[i] + 32;
        j += k;
        
        if (j == -1) {
            k = 2;
            j = 0;
        }
    }

    flag[KEY_LENGTH] = 0;

    if ((fd = fopen("arg", "wb")) == NULL) {
        puts("error opening file [arg]");
        exit(EXIT_FAILURE);
    }

    printf("%s\n", flag);
    fprintf(fd, "%s", flag);

    fclose(fd);
    
    return EXIT_SUCCESS;
}
