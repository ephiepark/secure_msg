from miller_rabin import is_prime

for i in range(3, 1000):
    if is_prime(i):
        print "%d \n" % i

#i = 2 ** 2048
#while True:
#    if is_prime(i):
#        print  "found prime ! %d " % i
#        break
#    else:
#        i = i - 1
#        print "%d \n" % i
