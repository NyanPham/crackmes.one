

def run():
    i = 1
    j = 2

    target_str = "Evilzone"
    user_input = "69helloworldojhajsbdaas"
    string = []

    for k in range(len(target_str)):
       string.append(ord(target_str[k]))

    print(''.join(map(str, string)))
    
if __name__ == '__main__':
    run()
