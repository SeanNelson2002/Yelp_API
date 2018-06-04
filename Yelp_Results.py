import Yelp_Business_API as Yelp
token = '<Token Here>'
Info_Back = ['Name','Rating']
Field_Name = 'yes'
Params_1 = {
    'phone':'+15128582221'
    }
Params_2 = {
    'location':'2440 E Hwy 290 Dripping Springs, TX 78620 United States',
    'latitude':'30.1942506',
    'longitude':'-98.0526925'
    }
Params_3 = {
    'location':'92440 E Hwy 290 Dripping Springs, TX 78620 United States',
    'latitude':'30.1942506',
    'longitude':'-98.0526925',
    'transaction_type':'delivery'
    }
Params_4 = {
    'locale':'en_US',
    'Alias':'flores-mexican-restaurant-dripping-springs'
    }
Params_5 = {
    'name':'flores mexican restraunt',
    'address1':'2440 E Hwy 290 Dripping Springs, TX 78620 United States',
    'city':'Dripping Springs',
    'state':'TX',
    'country':'US'
    }
Params_6 = {
    'id':'flores-mexican-restaurant-dripping-springs',
    'locale':'en_US'
    }
Params_7 = {
    'location':'92440 E Hwy 290 Dripping Springs, TX 78620 United States',
    'latitude':'30.1942506',
    'longitude':'-98.0526925',
    'locale':'en_US'
    }
print('Yelp API Module Example\nAuthor: Sean Nelson\nEmail: n.sean.360@gmail.com\nPython Version: 3.6\nCreated: 6/4/2018 11:52 AM\n')
print('------------Example------------')
print('Business: flores mexican restraunt')
print('Location: 92440 E Hwy 290 Dripping Springs, TX 78620 United States')
print('Latitude: 30.1942506')
print('Longitude: -98.0526925')
print('Alias: flores-mexican-restaurant-dripping-springs')
print('locale: en_US')
print('phone: +15128582221')
print('\n--------Business-Search--------')
print('Phone Search Endpoint ('+Yelp.Search.Phone(Params_1, token, Info_Back, Field_Name)+')\n\tNote: Very Accurate\n')
print('Business Detail Endpoint ('+Yelp.Search.Business_Details(Params_4, token, Info_Back, Field_Name)+')\n\tNote: Very Accurate\n')
print('Business Match Endpoint ('+Yelp.Search.Business_Match(Params_5, token, Info_Back, Field_Name)+')\n\tNote: Mostly Accurate\n')
print('Business Search Endpoint ('+Yelp.Search.Business(Params_2, token, Info_Back, Field_Name)+')\n\tNote: Mostly Accurate\n')
print('Transaction Search Endpoint ('+Yelp.Search.Transaction(Params_3, token, Info_Back, Field_Name)+')\n\tNote: Not very Accurate\n')
print('------------Events------------')
print('Event Lookup Endpoint ('+Yelp.Search.Event_Lookup(Params_6, token, Info_Back, Field_Name)+')\n\tNote: Very Accurate\n')
print('Event Featured Endpoint ('+Yelp.Search.Event_Featured(Params_7, token, Info_Back, Field_Name)+')\n\tNote: Very Accurate\n')
