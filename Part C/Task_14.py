# 14. Create a dictionary with 5 countries as keys and their capitals as values. Loop through the dictionary and print each country with its capital.

countries = { "Pakistan" : "Islamabad", 
             "Saudi Arabia": "Riyad ",
               "Oman" : "Muscat",
                 "Bahrian" : "Manama",
                 "Iran" : "Tehran"
                 }

for country in countries.values():
    print(country)