#include <stdio.h>

#define LEN 0x15

int main(void) {
	unsigned a[LEN];
	FILE *fd;

	fd = fopen("crackme", "rb");

	fseek(fd, 0x1231, SEEK_SET);

	for (unsigned i = 0; i < LEN; ++i) {
		fread(a+i, 4, 1, fd);
		fseek(fd, 0x3, SEEK_CUR);
	}

	fclose(fd);

	fd = fopen("arg", "wb");

	for (unsigned i = 0; i < LEN; ++i) {
		fputc(a[i] ^ ("sup3r_s3cr3t_k3y_1337"[i] - 0x22), fd);
	}

	fclose(fd);

	return 0;
}
