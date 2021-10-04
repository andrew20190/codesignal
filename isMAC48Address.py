import re
def isMAC48Address(inputString):
    res = re.findall("^([A-F0-9]{2}-[A-F0-9]{2}-[A-F0-9]{2}-[A-F0-9]{2}-[A-F0-9]{2}-[A-F0-9]{2})$", inputString, re.IGNORECASE)
    print(res)
    return len(res) == 1

isMAC48Address("00-1B-63-84-45-E6")
