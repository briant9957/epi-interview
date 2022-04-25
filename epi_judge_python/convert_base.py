from test_framework import generic_test


def convert_base(num_as_string: str, b1: int, b2: int) -> str:
    stringToNumberMap = {'1': 1,
                         '2': 2,
                         '3': 3,
                         '4': 4,
                         '5': 5,
                         '6': 6,
                         '7': 7,
                         '8': 8,
                         '9': 9,
                         'A': 10,
                         'B': 11,
                         'C': 12,
                         'D': 13,
                         'E': 14,
                         'F': 15,
                         '0': 0}

    numberToStringMap = { 1: '1',
                          2: '2',
                          3: '3',
                          4: '4',
                          5: '5',
                          6: '6',
                          7: '7',
                          8: '8',
                          9: '9',
                          10: 'A',
                          11: 'B',
                          12: 'C',
                          13: 'D',
                          14: 'E',
                          15: 'F',
                          0: '0'}
    
    baseTenFormat = 0
    power = 0
    negative = True if num_as_string[0] == "-" else False

    for char in reversed(num_as_string):
        if char == '-':
            continue
        baseTenFormat += stringToNumberMap[char] * (b1 ** power)
        power += 1

    finalBaseConversionForm = []
    while baseTenFormat != 0:
        finalBaseConversionForm.insert(0, numberToStringMap[baseTenFormat % b2])
        baseTenFormat = baseTenFormat // b2

    if negative:
        finalBaseConversionForm.insert(0, '-')
    return "".join(finalBaseConversionForm) if len(finalBaseConversionForm) != 0 else "0"

# Care of negatives when dealing with numbers
# check case when number is actually 0
if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('convert_base.py', 'convert_base.tsv',
                                       convert_base))
