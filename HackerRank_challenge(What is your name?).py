
first_name = raw_input()
last_name = raw_input()

if first_name and last_name:
    if len(first_name) <= 10 and len(last_name) <= 10:
        print "Hello, %s %s! you just delved into python."%(first_name, last_name)
    else:
        print "first and last name should be less then or equal to 10"
else:
    print "Empty will not allowed"
