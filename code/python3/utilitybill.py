# utilitybill.py: calculates utility bill for a give consumption in kWh
# S. Bulut  2019
# T. Topper 2015

print('''
====================
Bill Calculator
--------------------
''')

kwh = eval(input("Enter kWh used: "))
if kwh < 0:
    print('\nRecheck input value!')
    print("It was negative and meters\ndon't run backwards")
else:
    if kwh <= 500.0:
        amount = 20.0
    elif kwh <= 1000.0:
        amount = 20.0 + 0.03*(kwh-500.)
    else:
        amount = 35.0 + 0.02*(kwh-1000.)