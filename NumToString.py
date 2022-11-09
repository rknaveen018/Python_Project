# num = input("Enter the number:- ")
#
# num_len = len(num)

NumToStrDict = {1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine",
                0: "zero", 10: "ten", 11: "eleven", 12: "twelve", 13: "thirteen", 14: "fourteen", 15: "fifteen",
                16: "sixteen", 17: "seventeen", 18: "eighteen", 19: "nineteen", 20: "twenty", 30: "thirty", 40: "forty",
                50: "fifty", 60: "sixty", 70: "seventy", 80: "eighty", 90: "ninety", 100: "hundred", 1000: "thousand"}


def nts(num):
    num_len = len(num)
    char = ""
    if num_len == 1:
        char += NumToStrDict[int(num)]

    elif num_len == 2:
        if int(num) in NumToStrDict.keys():
            char += NumToStrDict[int(num)]
        else:
            num_1 = num[0] + "0"
            char += NumToStrDict[int(num_1)] + " " + NumToStrDict[int(num[1])]

    elif num_len == 3:
        if int(num) in NumToStrDict.keys():
            char += NumToStrDict[int(num)]
        else:
            if num[1] == "0" and num[0] == "1":
                num_1 = num[0] + "00"
                char += NumToStrDict[int(num_1)] + " and " + NumToStrDict[int(num[2])]
            elif (num[1] != "0") and (num[0] == "1") and (num[1:] in NumToStrDict):
                num_1 = num[0] + "00"
                char += NumToStrDict[int(num_1)] + " and " + NumToStrDict[int(num[1:])]
            elif num[1] != "0" and num[0] == "1" and num[1:] in NumToStrDict and num[2] == 0:
                num_1 = num[0] + "00"
                num_2 = num[1] + "0"
                char += NumToStrDict[int(num_1)] + " and " + NumToStrDict[int(num_2)] + NumToStrDict[int(num[2])]

    return char


for i in range(121):
    print(f'from number {i} to string is {nts(str(i))}')

