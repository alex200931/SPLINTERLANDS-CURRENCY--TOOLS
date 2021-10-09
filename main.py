import requests

spacer = "*" * 75
spacer_B= "-" * 75

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
    print(spacer)
    print(decAmount,"is equivalent to $", numberInDollars, "\n","percent changed:", change)
    print(spacer)
    
   
def convertSPS():
    api = "https://api.coingecko.com/api/v3/simple/price?ids=splinterlands&vs_currencies=usd&include_24hr_change=true"
    spsAmount = float(input("SPS AMount?"))
    response = requests.get(api)
    response = response.json()
    data = response['splinterlands']
    spsPrice = data['usd']
    change= data['usd_24h_change']
    numberInDollars = float(spsAmount) * float(spsPrice)
    print(spacer)
    print(spsAmount,"is equivalent to $", numberInDollars,"\n","percent changed:", change)
    print(spacer)

def landPrice():
    api = "https://wax.api.atomicassets.io/atomicmarket/v1/sales?state=1&collection_name=splintrlands&template_id=57491&page=1&limit=1&order=asc&sort=price"
    response = requests.get(api)
    response = response.json()
    data= response["data"]

    landLowPriceDic = {}
    for k, v in [(key, d[key]) for d in data for key in d]:
        if k not in landLowPriceDic:
            landLowPriceDic[k] = [v]
        else:
            landLowPriceDic.append(v)

    
    
    
    data= landLowPriceDic
    lowPrice= data["listing_price"]
    lowPrice = str(lowPrice)[2:-10]
    landPrice= float(waxPrice) * float(lowPrice)
    print (spacer)
    print("Lowest Avalible Land Price: $", float(landPrice))
    print(spacer)


waxApi= "https://api.coingecko.com/api/v3/simple/price?ids=wax&vs_currencies=usd"
response = requests.get(waxApi)
response = response.json()
data= response["wax"]
waxPrice= data["usd"]




def menu():
    selection = input("""
    Splinterlands Price Converter\n
    A: DEC
    B: SPS
    C: LAND
    X: EXIT
    
    Select which currency you would like to convert to USD: )
    

    """)

    if selection.lower() == "a":
        convertDEC()
        print(spacer_B)
        print("CREDIT: whonixx 4 helping code shiet and learninshiet")
        print(spacer_B)
        menu()
    elif selection.lower() == "b":
        convertSPS()
      
        print(spacer_B)
        print("CREDIT: whonixx 4 helping code shiet and learninshiet")
        print(spacer_B)
        menu()
    elif selection.lower() == "c":
        print(spacer_B)
        landPrice()
        print(spacer_B)
        menu()

    elif selection.lower() == "x":
        exit()
    else:
        print(spacer_B)
        print("Invalid choice \n returning back to menue")
        print(spacer_B)
        menu()


menu()
