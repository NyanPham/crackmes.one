def get_hamming_weight(x):
    return sum(c != '0' for c in '{:b}'.format(x))

with open('good_boy', 'rb') as f:
    good_boy = [int(b) for b in f.read()]

avg_weights = dict()

for L in range(1, 21):
    avg_weight = 0
    N = int(len(good_boy)/L)

    for i in range(N-1): 
        for j in range(L):
            avg_weight += get_hamming_weight(good_boy[L*i+j] ^ good_boy[L*(i+1)+j])

    avg_weight /= L*(N-1)
    avg_weights[L] = avg_weight

for x in sorted([(k, avg_weights[k]) for k in avg_weights], key=lambda x:x[1]):
    print('Length {:2d}: average Hamming weight per byte: {:f}'.format(x[0], x[1]))
