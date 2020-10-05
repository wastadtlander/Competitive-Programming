"""
Using Testcase num : 3662277, arr : ["foo", "bar", "baz", "foobar", "emo", "cap", "car", "cat"]
Problem From https://youtu.be/PIeiiceWe_w
Solved by William Stadtlander at 3:13 am in like 15 minutes for some reason wow I need to sleep

"""


def inNumber(num, arr):
    tempArr = []
    tempArr = translate(arr)
    inArr = []
    [inArr.append(arr[i]) for i in range(len(arr)) if tempArr[i] in str(num)]
    return sorted(inArr)


def translate(arr):
    tempArr = []
    tempVal = ""
    phonePad = {
        2 : ['a', 'b', 'c'],
        3 : ['d', 'e', 'f'],
        4 : ['g', 'h', 'i'],
        5 : ['j', 'k', 'l'],
        6 : ['m', 'n', 'o'],
        7 : ['p', 'q', 'r', 's'],
        8 : ['t', 'u', 'v'],
        9 : ['w', 'x', 'y','z']
    }
    for i in range(len(arr)):
        for n in range(len(arr[i])):
            for k, v in phonePad.items():
                if arr[i][n] in v:
                    tempVal += str(k)
        tempArr.append(tempVal)
        tempVal = ""
    return tempArr


if __name__ == "__main__":
    print(inNumber(3662277, ["foo", "bar", "baz", "foobar", "emo", "cap", "car", "cat"]))
