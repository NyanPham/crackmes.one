#include <stdio.h>
#include <stdlib.h>

#define KEY_LENGTH 7

void generate_key(char *);
void write_to_file(char *);

int main(void) {
    char key[KEY_LENGTH + 1];
    key[KEY_LENGTH] = 0;

    generate_key(key);
    write_to_file(key);

    return EXIT_SUCCESS;
}

void generate_key(char *key) {
    for (size_t i = 0; i < KEY_LENGTH; ++i) {
        key[i] = 0x42 ^ i[".-8.4.p"];
    }
}

void write_to_file(char *key) {
    FILE *fd;

    if ((fd = fopen("input", "wb")) == NULL) {
        puts("Error opening file, input");
        exit(EXIT_FAILURE);
    }

    fprintf(fd, "%s\n", key);

    fclose(fd);
}

