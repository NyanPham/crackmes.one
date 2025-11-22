#include <cstdlib>
#include <cstring>
#include <iostream>
#include <string>

using namespace std;

struct password {
    password() {
        ch = 0x42;
        str = "x_.1:.-8.4.p6-e.!-";
    }

    bool checkLength(int length) {
        int number = 0x168;
        string str = to_string(number);

        char ch = str.at(1);
        str = ch;
        this->length = atoi(str.c_str()) + 1;

        return length == this->length; 
    }

    bool checkPassword(string copy) {
        string key;

        for (size_t i = 0; i < copy.length(); ++i) {
            key += this->ch ^ copy.at(i);
        }

        char _copy[this->length + 1];
        size_t copied = this->str.copy(_copy, this->length, 5);
        _copy[copied] = 0;

        string actual_key(_copy);

        return key == actual_key;
    }

    void wrongPassword(void) {
        cout << "Login failed" << endl;
    }

    void rightPassword(void) {
        cout << "Login successful" << endl;
    }

    private:
        int length;
        char ch;
        string str;
};

int main(int argc, char **argv) {
    string input;
    getline(cin, input);

    password password{};

    if (!password.checkLength(input.length())) {
        password.wrongPassword();
        return EXIT_SUCCESS;
    }

    string copy(input);

    if (password.checkPassword(copy)) {
        password.rightPassword();
    }
    else {
        password.wrongPassword();
    }

    return EXIT_SUCCESS;
}

