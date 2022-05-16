import numpy


def generation(line):
    arr = list(line)

    for i in range(10):
        arr2 = numpy.array(arr)
        for j in range(-1, len(line) - 1):
            sosed1 = arr[j - 1] == '1'
            sosed2 = arr[j] == '1'
            sosed3 = arr[j + 1] == '1'
            if (sosed1 and sosed2 and sosed3) or (sosed1 and sosed2 and not sosed3) \
                    or (sosed1 and not sosed2 and sosed3) or (not sosed1 and not sosed2 and not sosed3):
                arr2[j + 1] = '0'
            else:
                arr2[j + 1] = '1'
        arr = numpy.array(arr2)

    return ''.join(arr)


print(generation("1001000101111100000101111001011011101101101111110111110000000000000011000001011001100011111101001001"))

