def is_prime(func):
    def check_prime(*args):
        number = func(*args)
        if not isinstance(number,int) or number <= 1:
            print("Не простое")
            return number
        for i in range(2, (number >> 1) + 1):
            if number % i == 0:
                print("Составное")
                return number
        print('Простое')
        return number
    return check_prime


@is_prime
def sum_three(a,b,c):
    return a+b+c

result = sum_three(2, 3, 6)
print(result)