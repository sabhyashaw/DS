def xor(a, b):
    result = ""

    for i in range(1, len(b)):
        if a[i] == b[i]:
            result += "0"
        else:
            result += "1"

    return result


def mod2div(dividend, divisor):
    pick = len(divisor)
    temp = dividend[0:pick]

    while pick < len(dividend):
        if temp[0] == '1':
            temp = xor(divisor, temp) + dividend[pick]
        else:
            temp = xor('0' * pick, temp) + dividend[pick]

        pick += 1

    if temp[0] == '1':
        temp = xor(divisor, temp)
    else:
        temp = xor('0' * pick, temp)

    return temp


data = input("Enter Data: ")
divisor = input("Enter Divisor: ")

append_data = data + '0' * (len(divisor) - 1)

crc = mod2div(append_data, divisor)

codeword = data + crc

print("\nOriginal Data :", data)
print("Divisor :", divisor)
print("CRC Bits :", crc)
print("Transmitted Codeword :", codeword)