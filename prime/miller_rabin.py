# N to be tested
# t is parameter
import sys
from math import log, sqrt, floor
from random import randint
from fractions import gcd

def is_prime(N, t = 10):
    if is_even(N):
        return False
    if is_perfect_power(N):
        return False
    (r, u) = compute_r_u(N) # compute r >= 1 and u odd such that N - 1 = 2^r*u
    for j in range(t):
        a = get_rand(N) #  {1, ... , N-1}
        if gcd(a, N) != 1 :
            return False
        if is_strong_witness(a, r, u, N) :
            return False
    return True

def mod_pow(x, n, m):
    l = []
    while n != 1:
        if n % 2 == 0:
            l.append(0)
        else:
            l.append(1)
        n = n // 2
    l.append(1)
    l.reverse()
    mod = 1
    for i in l:
        if i == 0:
            mod = (mod * mod) % m
        else:
            mod = ((mod * mod) * x ) % m
    return mod

def is_strong_witness(a, r, u, N):
    mod = mod_pow(a, u, N)
    #while (u != 0):
    #    if (u < 0):
    #        print "ERROR u equals to %d\n" % u
    #        sys.exit(1)
    #    round_mod = a % N
    #    exp = long(log(u,2))
    #    if u - 2 ** exp < 0:
    #        exp = exp - 1
    #    print "exp %d u %d\n" % (exp, u)
    #    for i in range(exp):
    #        round_mod = (round_mod * round_mod) % N
    #    mod = (mod * round_mod) % N
    #    u = u - 2 ** exp
    if mod == 1:
        return False
    if mod == N - 1:
        return False
    for i in range(1, r):
        mod = (mod * mod) % N
        if mod == N - 1:
            return False
    return True

def compute_r_u(N):
    tmp = N - 1 # tmp guaranteed to be even in the beginning
    r = 0
    while (tmp % 2 == 0) :
        tmp = tmp / 2
        r = r + 1
    #print "r %d u %d\n" % (r, tmp)
    return (r, tmp)

def is_even(N):  # can be optimized by using bit operations, I think
    if N % 2 == 0:
        return True
    return False

def is_perfect_power(N):
    # e range 2 to log(N, 2)
    max_e = long(log(N,2)) + 1
    minimum = 2
    #maximum = sqrt(N)
    maximum = N-1
    mid = (minimum + maximum) // 2
    for e in range(2, max_e + 1):
        #print "e %d n' %d\n" % (e, mid)
        while minimum <= maximum:
            val = mid ** e
            if N == val:
                return True
            if N > val:
                minimum = mid + 1
            else:
                maximum = mid - 1
            mid = (minimum + maximum) // 2
    return False

def get_rand(N): # returns random integer from {1, ... , N-1}
    return randint(1, N-1)

