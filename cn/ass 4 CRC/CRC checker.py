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


received_data = input("Enter Received Data: ")
divisor = input("Enter Divisor: ")

remainder = mod2div(received_data, divisor)

print("\nRemainder :", remainder)

if int(remainder) == 0:
    print("No Error Detected")
else:
    print("Error Detected")