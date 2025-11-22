"""
strlen(usr_input) == 21
usr_input.startswith("da_")

tmp_str = [0, 0, 0, 0]
tmp_str[0] = usr_input[3]
tmp_str[1] = user_input[4]
tmp_str[2] = user_input[5]
tmp_str[3] = user_input[6]

0   1  2  3  4  5  6  7  8  9  0  1  2  3  4  5  6  7  8  9  0
[d][a][-][1][0][0][3][-][0][8][X][3][2][-][a][b][d][c][-][d][a]
da-1003-08X32-abdc-da
"""


def luna():
    a = 20
    b = 30
    anubis()

def serial():
    """
        Does the same thing as anubis
        Seems like no actual impact on the program
    """
    pass


def anubis():
    """
        This function creates numbers on the stack, but then returns 
        a number, but that number is not used anywhere
    """
    a = 0x00616E754C00000009
    b = 0x000000666f2073736564646F47
    c = 0x0072756F662079746E657754

    # return dword of c

def salt():
    """
    This function may seems similar to another foo functions,
    but it actually initializes the firstFour array for us
    """
    a = 0
    b = 1

    firstFour = [None] * 200

    while b <= 2000:
        if b%20 == 3:
            if b > 1000:
                firstFour[a] = b
                a += 1
                b += 1
            else:
                b += 1
        else:
            b += 1
    return firstFour

def pepper(num, usr_input):
    """
    Checks the remaining parts of the usr_input is correct
    after checking the firstFour bytes
    """

    assert usr_input[7] == '-'
    assert usr_input[10] == 'X'
    assert usr_input[13] == '-'
   
    s2 = []

    a = 2 * ((num //3 ) + 16)
    if a <= 999:
        a = 7 * (num//3) + 42

    num_str = f"{a}"
    
    s2.append(num_str[3])
    s2.append(num_str[2])
    s2.append('X')
    s2.append(num_str[1])
    s2.append(num_str[0])

    s2 = ''.join(s2)
    print(s2)
    
    s1 = usr_input[8:13]
    
    assert s1 == s2
    
    gaia(usr_input)

def gaia(usr_input):
    assert usr_input[14] <= usr_input[16]
    assert usr_input[17] >= usr_input[15]
    assert usr_input[13] == '-'
    thor(usr_input)

def thor(usr_input):
    assert usr_input[18:21] == '-da'
    
    anhilla = 'odjbyumd t'
    scarab = 'Go o o aei!'

    for i in range(10):
        print(f"{scarab[i]}{anhilla[i]}", end="")
    print('\n')

def run():
    firstFour = salt()
    firstFour = list(filter(lambda x : x is not None, firstFour))
    print(firstFour)

    usr_input = input("Your serial key: ")
    assert len(usr_input) == 21
    assert usr_input.startswith('da-')

    num_str = usr_input[3:7]
    num = int(num_str)

    if num in firstFour:
        pepper(num, usr_input)
    else:
        print("hades")
    

if __name__ == '__main__':
    run()
