# mortgage.py


principal = 500000.0
rate = 0.05
payment = 2684.11
extra_payment_start_month = 61
extra_payment_end_month = 108
extra_payment = 1000
total_paid = 0.0
total_month = 0 

while principal > 0:
    total_month += 1   
    
    payment_this_month = payment
    if total_month >= extra_payment_start_month and total_month <= extra_payment_end_month: 
        payment_this_month += extra_payment

    if payment_this_month > principal:
        payment_this_month = principal
        principal = 0
    else:
        principal = principal * (1+rate/12) - payment_this_month
    
    print(f'{total_month} {payment_this_month:0.2f} {principal:0.2f}')
    total_paid = total_paid + payment_this_month

print(f'Total Paid {total_paid:0.2f}')
print(f'Total Month {total_month}')