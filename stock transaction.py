#Stock Transaction Program
#9/15/2016
#The program is asking will he make a profit or loss

#Create the variable
shares = 2000
paid = 40.00
commission = 0.03
sold = 42.75
sold_commision = 0.03
#calculate the price of shares
total_shares = 2000 * 40.00
#Calculate the commission
value = total_shares * 0.03
#Calculate the total sell
total = total_shares + value
#Calculate the value of shares
value_shares = 2000 * 42.75
#Calculate the commission of sold
value_sold = value_shares * 0.03
#Calculate the total sold
total_sold = value_shares + value_sold
#Caculate the amount left
profit = total_sold - total
#Display the results
print("Shares = ",total_shares)
print("Commission = ",value)
print("Total = ",total)

print("Total sold = ",value_shares)
print("Commission sold = ",value_sold)
print("Total = ",total_sold)

print(profit)

if profit > 0:
    print("Profit")
else:
    print("Loss")
