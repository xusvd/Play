#Importing the library

from urllib import request
from datetime import date
from datetime import datetime
import os
from bs4 import BeautifulSoup


# If there's a preb query!
if os.path.exists("QueryList.sql"):
    os.remove("QueryList.sql")
else:
    print("New file created!")


# Initializing variable
url = "https://www.bankofalbania.org/Markets/Official_exchange_rate/"
fer = BeautifulSoup(request.urlopen(url).read(),'html.parser')

# Extracting data for article section
bodyHtml = fer.find('div', {'class' : 'mb-2'})
bodyTable = fer.find('table', {'class' : 'table'})

# Calculating result
res = bodyHtml.get_text()
tdata = bodyTable.get_text()

# Printing the resultchrom
udate=res[13:23]


date_object = datetime.strptime(udate, '%d.%m.%Y').date()
# print(type(date_object))
# print(date_object)  # printed in default format
udate = date_object.strftime("%d/%m/%Y")
today = date.today()

d1 = today.strftime("%d/%m/%Y")
sysdate = datetime.strptime(d1, '%d/%m/%Y').date()

clst = tdata.split()
eur = clst[15]
usd = clst[11]

eur = float(eur)
usd = float(usd)

def exchange(): 
    print("Date on Website: ",udate)
    print("Today\'s date: ",sysdate)
    print("USD :",usd," EUR:",eur)
    print("==================================")
    
    if sysdate > date_object:
        print("Not Updated!")
    else:
        print("Currency Rate Updated.")    
    #select VF_CONFIG_CUR_RATES_FUNC ('8','102.00','840','USD to Albanian Lek','14/04/2023') from dual; 
    usdq=f"select VF_CONFIG_CUR_RATES_FUNC ('8','{usd}','840','USD to Albanian Lek','{udate}') from dual;"
    eurq=f"select VF_CONFIG_CUR_RATES_FUNC ('8','{eur}','978','EUR to Albanian Lek','{udate}') from dual;"
    dateq=f"select * from vf_config_cur_rates_t where effective_date in ('{udate}');"
    
    queryList=[usdq,eurq,dateq,'\n']
    
    with open('QueryList.sql', 'a') as f:
        f.write('\n'.join(queryList))

if __name__ == "__main__":
    exchange()