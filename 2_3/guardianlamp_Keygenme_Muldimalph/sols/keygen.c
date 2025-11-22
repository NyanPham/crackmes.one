#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#define LEN 16
#define A_LEN 0x7ff0

int main(void) {
    char buf[LEN + 1];
    char a[A_LEN];
    float x, y, z;
    int ecx, edx, eax;
    FILE *fd;

    srand(time(NULL));

    if ((fd = fopen("muldimalph", "rb")) == NULL) {
        puts("error opening file [muldimalph]");
        exit(EXIT_FAILURE);
    }

    fseek(fd, 0x2020, SEEK_SET);
    fread(a, 1, A_LEN, fd);
    fclose(fd);

    for (int i = 0; i < 3; ++i) {
        buf[i] = rand() % 0x4b + 0x30;
    }

    x = buf[0] / (float) 122;
    y = buf[1] / (float) 122;
    z = buf[2] / (float) 122;

    for (int i = 3, j; i < LEN; ++i) {
        ecx = (float) i * z + (float) i * z;
        edx = (float) i * y + (float) i * y;
        eax = (float) i * x + (float) i * x;

        j = (edx + ecx * 32) * 32 + eax;

        buf[i] = a[j];
    }

    buf[LEN] = 0;

    if ((fd = fopen("arg", "wb")) == NULL) {
        puts("error opening file [arg]");
        exit(EXIT_FAILURE);
    }

    fprintf(fd, "%s", buf);
    fclose(fd);

    return EXIT_SUCCESS;
}
