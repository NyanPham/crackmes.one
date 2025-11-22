#include <stdio.h>
#include <stdlib.h>
#include <sys/ptrace.h>
#include <sys/types.h>

size_t getLength(const char *string)
{
    const char *counter = string;
    while(*counter++);
    return counter - string - 1;
}

void verify_key(char *input, size_t length)
{
	char *password = (char *) malloc(length * sizeof(char));
    unsigned int tmp = 97, c = 0, aux = 0;

	for(short i = 0; i < length; ++i)
	{
	   password[i] = tmp;
	   tmp++;
	}

	password[length] = '\0';

	for(unsigned int i = 0; i < length; ++i)
	{
		for(unsigned int j = 0; j < (length - 1); ++j)
		{
            aux = password[i];
            password[i] = password[j];
            password[j] = aux;
		}
	}

	for(short i = 0; i < length; ++i)
	{
		if(((int)input[i] ^ (int)password[i]) == 0)
			c--;
	}
	
    if(((c ^ 0xdeadbeef >> length & 0xc ^ 0xffffffff) + 5 ^ length) == 0) // 0xfffffff6
	{	puts("Cracked....");
		free(password);
		exit(0);
	}

    puts("Wrong key, ...try again...");
	free(password);
    exit(1);
}

void menu(void)
{
     puts("Welcome to this little crackme!!!!");
     puts("There is only one key, try to find it and decrypt the .zip");
     puts("Good luck");
     puts("Developed by Binary Newbie");
     puts("");
}

int main(int argc, char **argv)
{
   char *s;
   size_t length;

   if(argc == 2)
   {
		if(ptrace(PTRACE_TRACEME, 0, 0, 0) == -1)
		{
		   fprintf(stderr, "Nop...try again...\n");
		   return 1;
		}
        
        menu();
        puts("Humm lets see what you are doing .....");

		s = argv[1];
		length = getLength(s);

		if((length ^ 10) == 0)
		{
			s[length] = '\0';
			verify_key(s, length);
		}else
		{
			fprintf(stderr, "Invalid length...\n");
			return 1;
		}
   }else
   {
	   fprintf(stderr, "Usage %s <key>\n", argv[0]);
       return 1;
   }

   return 0;
}
