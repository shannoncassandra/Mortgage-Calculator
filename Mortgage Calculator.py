# House price
while True:
    try:
        house_price = int(input("What is the price of the house? "))
        break
    except ValueError:
        print('Try again!')

#Interest rate
while True:
    try:
        int_rate = float(input("What is the interest rate? "))
        break
    except ValueError:
        print('Try again!')

#Loan term
while True:
    try:
        loan_term = int(input("How many years will the term be? "))
        break
    except ValueError:
        print('Try again!')

#PMI including calculation, and also defines loan amount and down payment
while True:
    try:
        pmi_ask = int(input("How much are you putting down? "))
        break
    except ValueError:
        print('Try again!')
if pmi_ask in range(0,19):
    pmi_amt = int(((loan_amt - pmi_ask)*.007)/12)
    down_pmt = house_price * (pmi_ask/100)
    loan_amt = house_price - down_pmt
    print('You will have to pay PMI of ${} a month'.format(pmi_amt))
if pmi_ask in range(20,99):
        pmi_amt = int(0)
        down_pmt = house_price * (pmi_ask/100)
        loan_amt = house_price - down_pmt
        print('Yay, no PMI! :)')
if pmi_ask >= 100:
    if (pmi_ask / house_price) >=.2:
        pmi_amt = int(0)
        loan_amt = house_price - pmi_ask
        print('Yay, no PMI! :)')
    if (pmi_ask / house_price) <.2:
        pmi_amt = int(((house_price - pmi_ask)*.007)/12)
        loan_amt = house_price - pmi_ask
        print('You will have to pay PMI of ${} a month'.format(pmi_amt))

#Property tax
prop_tax_quest = input("Do you know how much property taxes are? ")
if prop_tax_quest == 'yes':
    prop_tax = int((input("How much are they annually? ")))/12
if prop_tax_quest == 'Yes':
    prop_tax = int((input("How much are they annually? ")))/12   
if prop_tax_quest == 'no': 
    prop_tax = int(165)
    print('We will just estimate $165 a month')
if prop_tax_quest == 'No': 
    prop_tax = int(165)
    print('We will just estimate $165 a month') 

#Insurance
ins_quest = input("Do you know how much insurance will be? ")
if ins_quest == 'yes':
    ins = int((input("How much will insurance be annually? ")))/12
if ins_quest == 'Yes':
    ins = int((input("How much will insurance be annually? ")))/12
if ins_quest == 'no': 
    ins = int(50)
    print('We will just estimate $50 a month')
if ins_quest == 'No': 
    ins = int(50)
    print('We will just estimate $50 a month')    

#Payment Calculation
mortgage = (loan_amt * (((int_rate/100)/12)*(1+((int_rate/100)/12))**(loan_term*12)/((1+((int_rate/100)/12))**(loan_term*12)-1))) + prop_tax + ins + pmi_amt

#Yay!
print('Your monthly mortgage will be ${}'.format(int(mortgage)))
