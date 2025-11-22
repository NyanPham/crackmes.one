def run():
    inp = list("mgdilolmsoamasiug")

    for i in range(len(inp)):
        n = ord(inp[i])
        r = n % len(inp)
        inp[r] = inp[i]
    
    print("".join(inp))

run()
