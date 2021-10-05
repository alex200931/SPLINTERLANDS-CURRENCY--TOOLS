import requests
from colorama import Fore 

RED = Fore.RED
RESET = Fore.RESET


def convertDEC():
    api= 'https://api.coingecko.com/api/v3/simple/price?ids=dark-energy-crystals&vs_currencies=usd&include_24hr_change=true&include_last_updated_at=true'
    decAmount = float(input("DEC Amount? "))
    response = requests.get(api)
    response = response.json()
    data = response['dark-energy-crystals']
    decPrice = data['usd']
    change = data['usd_24h_change']
    last_update= data['last_updated_at']
    numberInDollars = (decAmount) * (decPrice)
    print("is equivalent to $", numberInDollars, "\n","percent changed:", change)
   
def convertSPS():
    api = "https://api.coingecko.com/api/v3/simple/price?ids=splinterlands&vs_currencies=usd"
    spsAmount = float(input("SPS AMount?"))
    response = requests.get(api)
    response = response.json()
    data = response['splinterlands']
    spsPrice = data['usd']
    numberInDollars = float(spsAmount) * float(spsPrice)
    print(spsAmount, "is equivalent to $", int(numberInDollars))


def menu():
    selection = input("""
    Splinterlands Price Converter\n
    A: DEC
    B: SPS
    X: EXIT

    (CREDIT: whonixx 4 helping code "shiet" and "learninshiet")
    
    Select which currency you would like to convert to USD: )
    """)

    if selection.lower() == "a":
        convertDEC(), menu()
    elif selection.lower() == "b":
        convertSPS(), menu()
    elif selection.lower() == "x":
        exit()
    else:
        print(f"{RED}Invalid choice{RESET}")
        menu()


menu()