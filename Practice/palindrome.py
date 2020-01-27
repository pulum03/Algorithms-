palindrome = []

def get_palindrome(num1, num2):
    max_palindrome = 0
    num2_org = num2
    while num1 > (num1/10): #why not 99? and (num1/10)?
        while num2 > (num2/10):
            multiple = num1 * num2
            if is_palindrome(multiple) and (max_palindrome < multiple):
                max_palindrome = multiple
            num2 -= 1
        num1 -= 1
        num2 = num2_org
    return max_palindrome

def is_palindrome(multiple):
        if str(multiple) == str(multiple)[::-1]: #[::-1] 는 역순으로 한칸씩
            return True
        else:
            return False

print(get_palindrome(999, 999))
