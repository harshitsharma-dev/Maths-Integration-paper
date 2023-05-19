from sympy import *
x = symbols('x')
n = 0
a = 4
expr = (x**(2))
expr_saved = expr

upperlimit = 10

lowerlimit =0
termlist = []
sum_indefinite = 0
sum_definite = 0
while True:
    n+=1
    if n == 1:
        termlist.append((x*(expr_saved)))
        sum_indefinite = termlist[0]
        sum_definite = (limit(sum_indefinite,x,upperlimit) - limit(sum_indefinite,x,lowerlimit)).evalf()
    else:
        expr = diff(expr, x)
        if expr!= 0:
            z = (((-1)**(n+1))*(x**n)*expr)/factorial(n)
            termlist.append(z)
            prev_sum_indefinite = poly(sum_indefinite)
            sum_indefinite += z
            sum_definite = (limit(sum_indefinite,x,upperlimit) - limit(sum_indefinite,x,lowerlimit)).evalf()

            foundtan = True

            if sum_indefinite == prev_sum_indefinite:
                print('break due to repetetion')
                break
            else:
                print(termlist)
                print((sum_definite))
                print(poly(sum_indefinite))
        else:
            print('break due to diff = 0')
            break
print(termlist)
print(poly(sum_indefinite))
print(sum_definite)
