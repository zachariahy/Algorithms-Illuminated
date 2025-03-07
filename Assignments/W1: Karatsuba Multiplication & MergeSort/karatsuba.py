def karatsuba(number1, number2):
    digits = max(len(number1), len(number2))
    number1 = number1.zfill(digits)
    number2 = number2.zfill(digits)
    
    if digits == 1:
        return str(int(number1) * int(number2))
    
    midpoint = digits // 2

    a = number1[:midpoint]
    b = number1[midpoint:]
    c = number2[:midpoint]
    d = number2[midpoint:]

    p = str(int(a) + int(b))
    q = str(int(c) + int(d))

    ac = int(karatsuba(a, c))
    bd = int(karatsuba(b, d))
    pq = int(karatsuba(p, q))

    adbc = pq - ac - bd
    
    power = pow(10, 2 * (digits - midpoint))
    return str(power * ac + pow(10, digits - midpoint) * adbc + bd)

x = '3141592653589793238462643383279502884197169399375105820974944592'
y = '2718281828459045235360287471352662497757247093699959574966967627'
output = int(karatsuba(x, y))
actual = int(x) * int(y)

print(f'Output: {output}\nActual: {actual}\nAnswer correct: {output==actual}')

# Output: 8539734222673567065463550869546574495034888535765114961879601127067743044893204848617875072216249073013374895871952806582723184
# Actual: 8539734222673567065463550869546574495034888535765114961879601127067743044893204848617875072216249073013374895871952806582723184
# Answer correct: True
