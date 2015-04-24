def basic_calculator():
    fst = float(input('Enter the length : '))
    lst = float(input('Enter the length : '))
    if fst and lst or fst == 0 or lst == 0:
        if -10000 <= fst <= 10000 and -10000 <= lst <= 10000:
            print "%.2f"%(fst+lst)
            print "%.2f"%(fst-lst)
            print "%.2f"%(fst*lst)
            print "%.2f"%(fst/lst)
            print "%.2f"%(fst//lst)


if __name__ == '__main__':
    basic_calculator()







