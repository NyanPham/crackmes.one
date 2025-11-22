def gks(string, num):
    cloned = list(string)
    
    for i in range(len(cloned)):
        if (cloned[i].isalpha()):
            for j in range(num):
                if (cloned[i] == 'z'):
                    cloned[i] = 'a'
                elif (cloned[i] == 'Z'):
                    cloned[i] = 'A'
                else:
                    cloned[i] = chr(ord(cloned[i]) + 1)

    return "".join(cloned)


def run():
    usr_name = input("Enter user name: ")
    transformed = gks(usr_name, len(usr_name))
    print(transformed)

run()
