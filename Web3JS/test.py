from datetime import datetime
import pandas as pd 
from dateutil.relativedelta import relativedelta


def func_import():
    print("Run this program for each tranche")
    p = int(input("Principal Amount?"))
    i = float(input("Interest Rate?"))
    t = int(input("Total Term Length (in months)?"))
    io = int(input("Months of Interest Only?"))
    sd = input("Loan Start Date? (MM/DD/YYYY)")
    m = int(sd[0:2])
    d = int(sd[3:5])
    y = int(sd[6:10])
    arr = list()
    dt = datetime(y, m, d)
    arr.append(p)
    arr.append(i)
    arr.append(t)
    arr.append(io)
    arr.append(dt)
    return arr;

def calculate(info):
    #Collecting the information
    start_date = info[4]
    principal = info[0]
    rate = info[1]/100
    term = info[2]
    io = info[3]

    #Getting the dates
    dt_list = list()
    dt_list.append(start_date)
    count = 0 
    while count < term:
        l = len(dt_list)
        future = dt_list[l-1] + relativedelta(months = 1)
        dt_list.append(future)
        count += 1
    print(dt_list)

    #Custom WTI calculation
    intrate = rate/12.0
    total_io = principal * intrate * io
    new_term = term - io 
    value = principal
    payment = ((intrate * value) / (1 - pow(1+intrate,-new_term)))
    i_normal = []
    p_normal = []
    while value > 0:
        pay_interest = (value * intrate)
        i_normal.append(pay_interest)
        pay_principle = payment - pay_interest
        p_normal.append(pay_principle)
        if value - payment < 0:
            pay_principle = value
        value = value - pay_principle

    interest_totals = list()
    io_list = [interest_totals.append(total_io/io) for n in range(0, io)]
    interest_totals += i_normal
    principal_totals = list()
    po_list = [principal_totals.append(0) for n in range(0, io)]
    principal_totals += p_normal
    print(len(dt_list))
    print(len(interest_totals))
    print(len(principal_totals))
    return [dt_list, interest_totals, principal_totals]

def output_to_excel(arr):
    dates = arr[0][1:]
    df = pd.DataFrame(data = {"Dates": dates, "Interest": arr[1], "Principal": arr[2]})
    print(df)

output_to_excel(calculate(func_import()));
