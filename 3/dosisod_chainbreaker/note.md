# Bin: chainbreaker
## Author: dosisod

```
main():
    seed = user_input() 
    next_seed = seed

    x = ((seed ^ 0x7b) + (seed ^ 0x141)) * 0x533d
    r = int((x / 100) * 100) # get x % 100, but truncate towards zero

    if r < 0:
        r = -r
    if r == 0:
        r = 10

    i = 0
    while (i <= 99) and (i < r):
        next_seed = parse(seed, next_seed, i)
        sleep_time = next_seed < 0 ? -next_seed : next_seed
        dur_ms = int_to_millis(sleep_time)
        sleep(dur_ms)
        i++

        
    if i == 99:
        failure_max_iter()
    else if (i > 99) or (i >= r):
        if seed != next_seed:
            failure_seed_unmatch()
        else:
            SUCCEED()
```


We succeed when we make i >= r, while the next_seed is back to the same value as seed.
So the value of `seed`, and the algorithm of `parse(int, int, int)` (that produces `next_seed`) is important.
Let's look at the `parse` func:

```
parse(a, b, c):
    if (b == 0):
        failure_invalid_chain_produced()
        exit()
    
    # bound check to make sure -4096 < b < 4096
    if (b < -4096) or (b > 4096):
        b = -(b % 4096)

    x = 1
    for (i = 0; i <= 2; i++):
        x ^= b << i

    return (x + ((a + c - 1) ^ b) + a - 15)
``` 

We know the `parse` logic. The logic is complicated with `xor`, `bitshifting`, and modulo conditions as well...
The actually best solution now is to brute force it. Let's continue to finish the `solve.py`, which is to brute force the seed!
