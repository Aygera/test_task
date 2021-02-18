import sys, json, math

filename = sys.argv[-1]

with open(filename, "r") as read_file:
    data = json.load(read_file)
    
def cumip(interest, periods, loan, start, end):
    
    #Return error if either rate, periods, or value are lower than or equal to zero
    if (interest <= 0 or periods <= 0 or loan <= 0):
        return 'rate, periods, or loan cannot be <= 0!'

    # Return error if start < 1, end < 1, or start > end, or end > periods
    if (start < 1 or end < 1 or start > end or end > periods):
        return 'Wrong perdios for start or end';
    
    payment = payment_calc(interest, periods, loan)
    result = 0
    
    if (start == 1):
        result = -loan
        start+=1
    
    for i in range (start, end+1):
        result += following_payments(interest, i - 1, payment, loan);
    rate = interest/100/12
    result *= rate

    #Return cumulative interest
    return result;

def payment_calc(interest_rate, payment_periods, loan):

    #Return payment
    rate = interest_rate/100/12
    term = pow((1+rate),payment_periods);
    result = loan*(rate + rate/(term-1))
    
    #Return monthly payment
    return -result;
    
def following_payments(interest_rate, payment_periods, payment, loan):

    rate = interest_rate/100/12
    term = pow(1 + rate, payment_periods);
    result = loan * term + payment * (term - 1) / rate;
    
    #return future payments
    return -result
    
    
cum =  cumip(**data)

print("Cumulative interest rate is: ", cum)

