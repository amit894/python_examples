def divideNumbers(dividend,divisor):
    quotient=0
    signed_dividend=abs(dividend)
    signed_divisor=abs(divisor)
    max_overflow_value= pow(2,31)-1
    min_overflow_value= -1*pow(2,31)
    if (signed_divisor==1):
        quotient=divisor*dividend
        if quotient>=max_overflow_value:
            return(max_overflow_value)
        elif quotient<=min_overflow_value:
            return(min_overflow_value)
        else:
            return quotient
    else:
        while(signed_dividend>=signed_divisor):
            signed_dividend-=signed_divisor
            quotient+=1
        if dividend*divisor<=0:
            quotient=-1*quotient
        return quotient

print(divideNumbers(2147483647,2))
