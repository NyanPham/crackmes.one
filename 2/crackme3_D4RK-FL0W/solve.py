p1 = [1,3,1,1,4,4,4,6,6,6]
p2 = [10,10,10,6,70,70,70,35,35,35]
p3 = [7,68,68,68,23,23,23,40,40,40]
p4 = [4,3,3,3,5,5,5,7,7,7]

def get_num(nums):
    nums_len = len(nums)
    
    ret = 0
    acc = 0
    for i in range(nums_len):
        acc |= nums[i] & ret
        ret ^= nums[i]
        tmp = ~(ret & acc)
        ret &= tmp
        acc &= tmp

    return ret


def run():
    assert len(p1) == 10
    assert len(p2) == 10
    assert len(p3) == 10
    assert len(p4) == 10

    num1 = get_num(p1)
    num2 = get_num(p2)
    num3 = get_num(p3)
    num4 = get_num(p4)
    
    print(num1)
    print(num2)
    print(num3)
    print(num4)

run()
