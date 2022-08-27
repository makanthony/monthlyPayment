# -*- coding: utf-8 -*-
"""
August 27 2022

Anthony Mak
"""

def payment(pv, rAPR, nMonths):
    """
    

    Parameters
    ----------
    pv : TYPE Float
        DESCRIPTION. how much $ is borrowed
    rAPR : TYPE float
        DESCRIPTION. annual interest rate
    nMonths : TYPE integer
        DESCRIPTION. length of loan in months

    Returns
    -------
    pmt : TYPE float
        DESCRIPTION. monthly payment

    """
    payment =  rAPR/1200*pv/(1-(1+(rAPR/1200))**(-nMonths))
    return payment

while(1):
    PV = float(input('Enter your principal investment: '))
    if PV == 0:
        break
    APR = float(input('Enter your monthly APR: '))
    Months = int(input('Enter length of loan in months: '))
    paymentDollars = payment(PV, APR, Months)
    print('Payment is ${:.2f}'.format(paymentDollars))
print('Loop exited')