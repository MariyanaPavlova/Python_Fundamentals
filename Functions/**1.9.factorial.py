def calc_fact(num):
    fact = 1

    for i in range(1,num+1):
        fact *= i
    return fact

def get_fact_div(fi,f2):
    return f1/f2

n = int(input())
n2 = int(input())

f1= calc_fact(n)
f2= calc_fact(n2)
result = get_fact_div(f1, f2)

print(f'{result:.2f}')