print("Simple Interest")

def calculate_simple_interest(principle, inerest, duration):
    total_interest = principle * inerest * 0.01 * duration
    total_amount = total_interest + principle
#    return total_amount
    return principle + ( principle * inerest * 0.01 * duration  )
total_amount = calculate_simple_interest(1000, 16, 4)
print (total_amount)
print (calculate_simple_interest(1000,17,4))
