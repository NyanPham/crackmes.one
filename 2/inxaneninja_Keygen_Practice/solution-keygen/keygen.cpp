#include <iostream>
#include <cstdlib>
#include <cstring>
#include <vector>
#include <string>
#include <unordered_map>

#include <sys/time.h>
#include <signal.h>
#include <unistd.h>

/**
 * Extracted by disassembling program in Ghidra, even though it is by the NSA. I
 * must say I really love Ghidra, more so than IDA or BinaryNinja!
*/
const int correct_checksum = 0xcdaa;

// Timeout after 5 seconds of not generating anything
const int generation_timeout = 5;

/**
 * Get a reasonable random seed that is not based on seconds...
 *
 * https://stackoverflow.com/a/322995/2047576
*/
void init_random() {
  struct timeval time;
  gettimeofday(&time,NULL);

  // microsecond has 1 000 000
  // Assuming you did not need quite that accuracy
  // Also do not assume the system clock has that accuracy.
  srand((time.tv_sec * 1000) + (time.tv_usec / 1000));
}

/**
 * Generate a range of characters allowed in the random passwords, these
 * values can be used in our keygen. I chose a-zA-Z0-9 because those are
 * easy to type!
*/
std::vector<char> get_valid_characters() {
  std::vector<char> characters;

  // a-z, A-Z
  for (int i = 'a'; i < 'z'; i += 1)
    characters.push_back((char)i), characters.push_back((char)(i - 32));

  // 0-9
  for (int i = '0'; i < '9'; i += 1)
    characters.push_back((char)i);

  return characters;
}

/**
 * Generate a random password based on a specific collection of characters of
 * a certain length.
*/
std::string get_valid_password(const std::vector<char>& characters, int length) {
  std::string password = "";

  for (int i = 0; i < length; i += 1)
    password += characters[rand() % characters.size()];

  return password;
}

/**
 * Calculate a checksum of a string based on the algorithm we reversed from the
 * inxaneninja_keygen_practise binary.
*/
int calc_checksum(const std::string& password) {
  int checksum = 0;

  for (auto it = password.begin(); it != password.end(); it++)
    checksum += ((int)*it * (int)password.size() * (int)password.size());

  return checksum;
}

/**
 * Verify that a NUL-terminated string consists only of digits
*/
bool is_integer(const char *value) {
  for (int i = 0; i < strlen(value); i += 1)
    if (!std::isdigit(value[i]))
      return false;

  return true;
}

/**
 * Executed when generation_timeout seconds have passed without generating enough
 * passwords, this function exits the program.
*/
void timeout_handler(int) {
  std::cout << "Not enough passwords generated for over " << generation_timeout << " seconds, exiting..." << std::endl;
  exit(2);
}

int main(int argc, char **argv) {
  // Ensure the process will not hang
  signal(SIGALRM, timeout_handler);

  // Set the alarm
  alarm(generation_timeout);

  // Get the list of valid characters
  auto characters = get_valid_characters();

  // Init the PRNG by setting a seed based on microseconds
  init_random();

  // variables regarding the generation of passwords
  int rounds = 1; // generate 1 password by default
  int length = 9; // i have found that a length of 9 only yields good results

  // overwrite number of passwords from parameters?
  if (argc >= 2) {
    if (!is_integer(argv[1])) {
      std::cout << "error: number of rounds must be an integer!" << std::endl;
      return 1;
    }

    rounds = atoi(argv[1]);
  }

  // overwrite length of passwords from parameters?
  if (argc >= 3) {
    if (!is_integer(argv[2])) {
      std::cout << "error: password length must be an integer!" << std::endl;
      return 1;
    }

    length = atoi(argv[2]);
  }

  std::string password;                          // each generated password
  std::unordered_map<std::string, bool> visited; // don't generate duplicates
  int checksum;                                  // the simple checksum

  // Generate passwords until we found enough valid ones
  for (int i = 0, found_passwords = 0; found_passwords < rounds; i += 1) {

    // Keep trying until we found a valid one, generating a new one on each try
    while (true) {
      password = get_valid_password(characters, length);
      checksum = calc_checksum(password);

      if (checksum == correct_checksum && visited.find(password) == visited.end()) {
        visited[password] = true;
        found_passwords += 1;

        std::cout << password << std::endl;
        break;
      }
    }
  }

  return 0;
}
