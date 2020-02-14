num = int(input("enter num"))
factorial = 1
if num == 0:
    print("no factorial")
elif num ==0:
    print("thhe factoorial of 0 is 1")
else:
    for i in range (1, num+1):
        factorial = factorial*i
        print ( "the fact of ",num,"is ",factorial)