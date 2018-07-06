def luckyNumbers(a, b):
    #
    # Write your code here.
    found=0
    for i in range(a,b):
        x=int(a)
        digits = []
        remainder = 0
        while(x is not 0):
            remainder = remainder + x%10
            digits.append(x%10)
            x=int(x/10)
        sum = remainder + x
        square=0
        for i in digits:
            square = square+i*i
        prime=1
        for i in range(2,sum):
            if sum%i==0:
                prime=0
                break
        if prime==1:
            for i in range(2,square):
                if square%i==0:
                    prime=0
                    break
        if sum == 1 and square ==1:
            prime=0
        if prime==1:
            found=found+1
        a=a+1
    return found

print(luckyNumbers(487162823133062956,681177519744583339))