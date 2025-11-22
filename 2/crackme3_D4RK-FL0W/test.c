#include <stdio.h>

int get_digit(int* intarray, int intarrlength) {
	// Assembly form consistency purposes
	int* var_18h = intarray;
	int var_1ch = intarrlength;
	// Initialized variables
	int var_4h = 0, var_8h = 0;
	// Loop
	for (int var_ch = 0; var_ch < var_1ch; var_ch++) { // Loop through every number in array
		// Step 1
		var_8h |= intarray[var_ch] & var_4h;
		// Step 2
		var_4h ^= intarray[var_ch];		  
		// Step 3
		int var_10h = ~(var_4h & var_8h); // Removing common bits
		var_4h &= var_10h;
		var_8h &= var_10h;
	}
	return var_4h; // Result
}

int main() {
	int array[4][10] = {
		{ 0x01, 0x03, 0x01, 0x01, 0x04, 0x04, 0x04, 0x06, 0x06, 0x06 },
		{ 0x0a, 0x0a, 0x0a, 0x06, 0x46, 0x46, 0x46, 0x23, 0x23, 0x23 },
		{ 0x07, 0x44, 0x44, 0x44, 0x17, 0x17, 0x17, 0x28, 0x28, 0x28 },
		{ 0x04, 0x03, 0x03, 0x03, 0x05, 0x05, 0x05, 0x07, 0x07, 0x07 }
	};
	for (int i = 0; i < 4; i++) {
		printf("%d\n", get_digit(array[i], 0xa));
	}
	return 0;
}


