#Project Euler Implementation
#ProbleTitle: Multiples of 3 or 5
#ProblemID: 1


# solved with O(1) complexity
# first exercise

# The solution consist on sum of multiples of 3 below 1000 + sum of multiples of 5 bellow 1000 - sum of comom multiples of 3 and 5 which is 15
# Because 15 represents the sequence of multiples

#We now that bellow 100 the last multiple of 3 is 999 and  999/3 is the quantity of multiples
#We also know that all multiples of 3 are always the thirds natural element: 3 6 9 12 ...
#So we can go for PA, an of 3 is 999 and an of 5 995 and an 15 990
dict_an = {"5":995,"3":999, "15": 990}

def sum_multiples(n, m):
    m = m//n
    return n*(m*(m+1)//2)

print(sum_multiples(3, dict_an['3']) + sum_multiples(5,dict_an['5']) - sum_multiples(15,dict_an['15']))