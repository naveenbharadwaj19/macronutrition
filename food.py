import requests
import json
from datetime import date , datetime

"""CHOCDF is Total carbohydrate , ENERC_KCAL is calories , FIBTG is fiber , PROCNT is protein . All this
measured for 100 g"""

def fetch_data():
    url = "https://edamam-food-and-grocery-database.p.rapidapi.com/parser"

    querystring = {"ingr":input("Enter food \n:")}

    headers = {
        'x-rapidapi-host': "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
        'x-rapidapi-key': "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx" # to get api key visit https://rapidapi.com
        }
    # search edman food and grocery in api marketplace
    
    response = requests.request("GET", url, headers=headers, params=querystring)
    data = response.json()
    remove_keys = data["hints"][0]["food"] # removing particular keys in dict
    remove_keys.pop("foodId")
    remove_keys.pop("category")
    today = date.today().strftime("%d/%m/%Y")
    current_time = datetime.now().strftime("%H:%M:%S")

    remove_keys["Foodname"] = querystring["ingr"]
    remove_keys["Date"] = today
    remove_keys["Time"] = current_time

    # dumping json first time
    first_time_dump = []
    first_time_dump.append(remove_keys)

    class Json_data():
        def serialize(self):
            try:
                with open("trackmyfood.json") as read_json:
                    main_data = []
                    json_load = json.load(read_json)
                    for i in json_load:
                        main_data.append(i)
                    main_data.append(remove_keys)
                with open("trackmyfood.json",'w') as write_json:
                    json.dump(main_data,write_json,indent=4,sort_keys= True)
            except Exception:
                print("No JSON data creating one!")
                return self.first_serialize()
        
        def first_serialize(self):
            with open("trackmyfood.json","w") as write_json:
                json.dump(first_time_dump,write_json,indent=4 , sort_keys= True)

    jd = Json_data()
    jd.serialize()

if __name__ == "__main__":
    print("Press ctrl + z and then press ENTER")
    try:
        while True:
            fetch_data()
    except Exception:
        print("Stopped")
