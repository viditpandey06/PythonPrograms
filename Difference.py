def close_number(num1, num2, num3):
    if (abs(num1-num3) <= 1 and (abs(num2-num1) >= 2 and abs(num2-num3) >= 2)):
        return True
    elif (abs(num2-num3) <= 1 and (abs(num1-num2) >= 2 and abs(num1-num3) >= 2)):
        return True
    elif (abs(num1-num2) <= 1 and (abs(num3-num2) >= 2 and abs(num3-num2) >= 2)):
        return True
    else:
        return False


print(close_number(4, 5, 6))
