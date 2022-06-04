from json import loads
import requests
from terminaltables import AsciiTable
from requests import get
import categories

chose = 3

def weather():
    cities = []
    url = requests.get = "https://danepubliczne.imgw.pl/api/data/synop"
    response = get(url)
    print("Enter the name of the cities for which you want to view weather data. \nConfirm each city with enter. Enter 0 to finish choosing cities. \nRemember to use Polish characters")
    city = "1"
    while not city == "0":
        city = str(input(""))
        cities.append(city.capitalize())
        rows = [
            ["City", "Temperature", "Rainfall", "Pressure"]
                ]
    miasto_jest = 0
    for row in loads(response.text):
        if row['stacja'] in cities:
            miasto_jest = 1
            rows.append([
                row['stacja'],
                row['temperatura'],
                row['suma_opadu'],
                row['cisnienie']
                        ]) 
    if miasto_jest != 1:
        print("The weather cannot be checked in any of the selected cities")
        return
    table = AsciiTable(rows)
    print(table.table)
    print("Some cities may have been missed because not all of them can be checked")

def exchange_rate():
    code = str(input("Enter the code of the currency whose exchange rate you want to check\n"))
    response = requests.get(f"http://api.nbp.pl/api/exchangerates/rates/a/{code}/")
    try:
        unpacked_value = response.json()
        rates = unpacked_value["rates"]
        unpacked_value = rates[0]
        print("The rate of the selected currency is :" + str(unpacked_value["mid"]))
    except:
        print("There is no such currency")



def news():
    category = categories.category()
    if categories.category() == 1:
        return
    response = requests.get(f"https://inshorts.deta.dev/news?category={category}")
    only_dictionary = response.json()
    data = only_dictionary["data"]
    unpacked_value = data[0]
    print("Author - ", unpacked_value["author"])
    print("Date - ",unpacked_value["date"])
    print("Content - ",unpacked_value["content"])
    print("Url - ",unpacked_value["url"])

# main

while chose == 3:
    chose = input("1 - Check the weather \n2 - Check the exchange rate of the selected currency \n3 - Read the news \n0 - Exit\n")
    if chose == '0':
       exit(0)
    elif chose == '1':
        weather()
        chose = 3
    elif chose == '2':       
        exchange_rate()
        chose = 3
    elif chose == '3':
        news()
        chose = 3




