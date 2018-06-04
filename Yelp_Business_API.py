import requests
def Info_Finder(Results, key):
    if key in Results:
        start = Results.index(key)+len(key)
        x = 0
        end = Results.find(',',start)
        found = Results[start:end]
        Resulting=''
        for char in found:
            if char == '[':
                pass
            elif char == ']':
                pass
            elif char == '{':
                pass
            elif char == '}':
                pass
            elif char == '"':
                pass
            elif char == "'":
                if key == "'name': ":
                    Resulting += char
            else:
                Resulting += char
        if key =="'name': ":
            if Resulting[0] == "'":
                Resulting = Resulting[1:len(Resulting)-1]
        Result = Resulting
        return str(Result)
def Parse(Results, Info_Back, Field_Name):
    Total = Info_Finder(Results, "'total': ")
    Rating = Info_Finder(Results, "'rating': ")
    Price = Info_Finder(Results, "'price': ")
    Phone = Info_Finder(Results, "'phone': ")
    ID = Info_Finder(Results, "'id': ")
    Alias = Info_Finder(Results, "'alias': ")
    Is_Closed = Info_Finder(Results, "'is_closed': ")
    Review_Count = Info_Finder(Results, "'review_count': ")
    Name = Info_Finder(Results, "'name': ")
    URL = Info_Finder(Results, "'coordinates': ")
    Image_URL = Info_Finder(Results, "'image_url': ")
    City = Info_Finder(Results, "'city': ")
    Country = Info_Finder(Results, "'country': ")
    Address1 = Info_Finder(Results, "'address1': ")
    Address2 = Info_Finder(Results, "'address2': ")
    Address3 = Info_Finder(Results, "'address3': ")
    State = Info_Finder(Results, "'state': ")
    Zip_Code = Info_Finder(Results, "'zip_code': ")
    Distance = Info_Finder(Results, "'distance': ")
    Attending_Count = Info_Finder(Results, "'attending_count': ")
    Category = Info_Finder(Results, "'category': ")
    Cost = Info_Finder(Results, "'cost': ")
    Cost_Max = Info_Finder(Results, "'cost_max': ")
    Description = Info_Finder(Results, "'description': ")
    Event_Site_URL = Info_Finder(Results, "'event_site_url': ")
    Interested_Count = Info_Finder(Results, "'interested_count': ")
    Is_Canceled = Info_Finder(Results, "'is_canceled': ")
    Is_Free = Info_Finder(Results, "'is_free': ")
    Is_Official = Info_Finder(Results, "'is_official': ")
    Latitude = Info_Finder(Results, "'latitude': ")
    Longitude = Info_Finder(Results, "'longitude': ")
    Tickets_URL = Info_Finder(Results, "'tickets_url': ")
    Time_End = Info_Finder(Results, "'time_end': ")
    Time_Start = Info_Finder(Results, "'time_start': ")
    Cross_Streets = Info_Finder(Results, "'cross_streets': ")
    Business_ID = Info_Finder(Results, "'business_id': ")
    result = ''
    for x in Info_Back:
        if x == 'Total':
            if Field_Name != 'yes' and 1:
                result += str(Total)+', '
            else:
                result += 'Total: '+str(Total)+', '
        elif x == 'Rating':
            if Field_Name != 'yes' and 1:
                result += str(Rating)+', '
            else:
                result += 'Rating: '+str(Rating)+', '
        elif x == 'Category':
            if Field_Name != 'yes' and 1:
                result += str(Category)+', '
            else:
                result += 'Category: '+str(Category)+', '
        elif x == 'Latitude':
            if Field_Name != 'yes' and 1:
                result += str(Latitude)+', '
            else:
                result += 'Latitude: '+str(Latitude)+', '
        elif x == 'Business_ID':
            if Field_Name != 'yes' and 1:
                result += str(Business_ID)+', '
            else:
                result += 'Business ID: '+str(Business_ID)+', '
        elif x == 'Cross_Streets':
            if Field_Name != 'yes' and 1:
                result += str(Cross_Streets)+', '
            else:
                result += 'Cross Streets: '+str(Cross_Streets)+', '
        elif x == 'Time_End':
            if Field_Name != 'yes' and 1:
                result += str(Time_End)+', '
            else:
                result += 'Time Ending: '+str(Time_End)+', '
        elif x == 'Time_Start':
            if Field_Name != 'yes' and 1:
                result += str(Time_Start)+', '
            else:
                result += 'Time Starting: '+str(Time_Start)+', '
        elif x == 'Tickets_URL':
            if Field_Name != 'yes' and 1:
                result += str(Tickets_URL)+', '
            else:
                result += 'Tickets URL: '+str(Tickets_URL)+', '
        elif x == 'Longitude':
            if Field_Name != 'yes' and 1:
                result += str(Longitude)+', '
            else:
                result += 'Longitude: '+str(Longitude)+', '
        elif x == 'Official':
            if Field_Name != 'yes' and 1:
                result += str(Is_Official)+', '
            else:
                result += 'Official: '+str(Is_Official)+', '
        elif x == 'Free':
            if Field_Name != 'yes' and 1:
                result += str(Is_Free)+', '
            else:
                result += 'Free: '+str(Is_Free)+', '
        elif x == 'Canceled':
            if Field_Name != 'yes' and 1:
                result += str(Is_Canceled)+', '
            else:
                result += 'Canceled: '+str(Is_Canceled)+', '
        elif x == 'Interested_Count':
            if Field_Name != 'yes' and 1:
                result += str(Interested_Count)+', '
            else:
                result += 'People Interested: '+str(Interested_Count)+', '
        elif x == 'Event_URL':
            if Field_Name != 'yes' and 1:
                result += str(Event_Site_URL)+', '
            else:
                result += 'Event URL: '+str(Event_Site_URL)+', '
        elif x == 'Description':
            if Field_Name != 'yes' and 1:
                result += str(Description)+', '
            else:
                result += 'Description: '+str(Description)+', '
        elif x == 'Cost_Max':
            if Field_Name != 'yes' and 1:
                result += str(Cost_Max)+', '
            else:
                result += 'Cost Max: '+str(Cost_Max)+', '
        elif x == 'Cost':
            if Field_Name != 'yes' and 1:
                result += str(Cost)+', '
            else:
                result += 'Cost: '+str(Cost)+', '
        elif x == 'Attending_Count':
            if Field_Name != 'yes' and 1:
                result += str(Attending_Count)+', '
            else:
                result += 'People Attending: '+str(Attending_Count)+', '
        elif x == 'Price':
            if Field_Name != 'yes' and 1:
                result += str(Price)+', '
            else:
                result += 'Price: '+str(Price)+', '
        elif x == 'Phone':
            if Field_Name != 'yes' and 1:
                result += str(Phone)+', '
            else:
                result += 'Phone: '+str(Phone)+', '
        elif x == 'ID':
            if Field_Name != 'yes' and 1:
                result += str(ID)+', '
            else:
                result += 'ID: '+str(ID)+', '
        elif x == 'Alias':
            if Field_Name != 'yes' and 1:
                result += str(Alias)+', '
            else:
                result += 'Alias: '+str(Alias)+', '
        elif x == 'Is_Closed':
            if Field_Name != 'yes' and 1:
                result += str(Is_Closed)+', '
            else:
                result += 'Is_Closed: '+str(Is_Closed)+', '
        elif x == 'Review_Count':
            if Field_Name != 'yes' and 1:
                result += str(Review_Count)+', '
            else:
                result += 'Review Count: '+str(Review_Count)+', '
        elif x == 'Name':
            if Field_Name != 'yes' and 1:
                result += str(Name)+', '
            else:
                result += 'Name: '+str(Name)+', '
        elif x == 'URL':
            if Field_Name != 'yes' and 1:
                result += str(URL)+', '
            else:
                result += 'URL: '+str(URL)+', '
        elif x == 'Image_URL':
            if Field_Name != 'yes' and 1:
                result += str(Image_URL)+', '
            else:
                result += 'Image URL: '+str(Image_URL)+', '
        elif x == 'City: ':
            if Field_Name != 'yes' and 1:
                result += str(City)+', '
            else:
                result += 'City: '+str(City)+', '
        elif x == 'Country':
            if Field_Name != 'yes' and 1:
                result += str(Country)+', '
            else:
                result += 'Country: '+str(Country)+', '
        elif x == 'Address1':
            if Field_Name != 'yes' and 1:
                result += str(Address1)+', '
            else:
                result += 'Address 1: '+str(Address1)+', '
        elif x == 'Address2':
            if Field_Name != 'yes' and 1:
                result += str(Address2)+', '
            else:
                result += 'Address 2: '+str(Address2)+', '
        elif x == 'Address3':
            if Field_Name != 'yes' and 1:
                result += str(Address3)+', '
            else:
                result += 'Address 3: '+str(Address3)+', '
        elif x == 'State':
            if Field_Name != 'yes' and 1:
                result += str(State)+', '
            else:
                result += 'State: '+str(State)+', '
        elif x == 'Zip_Code':
            if Field_Name != 'yes' and 1:
                result += str(Zip_Code)+', '
            else:
                result += 'Zip Code: '+str(Zip_Code)+', '
        elif x == 'Distance':
            if Field_Name != 'yes' and 1:
                result += str(Distance)+', '
            else:
                result += 'Distance: '+str(Distance)+', '
    result = result[0:len(result)-2]
    return result
class Search():
    def Business(parameters, token, Info_Back, Field_Name='yes'):
        parameters_sort = 0
        for x in parameters:
            if x == 'sort_by':
                parameters_sort += 1
        if parameters_sort == 0:
            parameters['sort_by'] = 'distance'
        headers = {
            'Authorization':'Bearer %s' % token,
        }
        r = requests.request('GET','https://api.yelp.com/v3/businesses/search', headers=headers, params=parameters)
        data = []
        data.append(r.json())
        data = str(data)
        if data == "[{'error': {'code': 'NOT_FOUND', 'description': 'Resource could not be found.'}}]":
            return "Could not find business (location & latitude & longitude required)"
        else:
            return Parse(data, Info_Back, Field_Name)
    def Phone(parameters, token, Info_Back, Field_Name='yes'):
        headers = {
            'Authorization':'Bearer %s' % token,
        }
        r = requests.request('GET','https://api.yelp.com/v3/businesses/search/phone', headers=headers, params=parameters)
        data = []
        data.append(r.json())
        data = str(data)
        if data == "[{'error': {'code': 'NOT_FOUND', 'description': 'Resource could not be found.'}}]":
            return "Phone number not found (US example +1XXXXXXXXXX)"
        else:
            return Parse(data, Info_Back, Field_Name)
    def Transaction(parameters, token, Info_Back, Field_Name='yes'):
        keyed_loc = 0
        keyed_cor = 0
        for k in parameters:
            if k == 'location':
                keyed_loc += 1
            elif k == 'latitude':
                keyed_cor += 1
            elif k == 'longitude':
                keyed_cor += 1
        parameters_1 = {}
        parameters_2 = ''
        if keyed_loc == 1:
            for k in parameters:
                if k == 'location':
                    parameters_1[k] = parameters[k]
                elif k == 'transaction_type':
                    parameters_2+= parameters[k]
        else:
            if keyed_cor == 2:
                for k in parameters:
                    for v in parameters[k]:
                        if k == 'latitude':
                            parameters_1[k] = parameters[k]
                        elif k == 'longitude':
                            parameters_1[k] = parameters[k]
                        elif k == 'transaction_type':
                            parameters_2+= parameters[k]
        headers = {
            'Authorization':'Bearer %s' % token,
        }
        r = requests.request('GET','https://api.yelp.com/v3/transactions/'+parameters_2+'/search', headers=headers, params=parameters_1)
        data = []
        data.append(r.json())
        data = str(data)
        if data == "[{'error': {'code': 'NOT_FOUND', 'description': 'Resource could not be found.'}}]":
            return "Business doesn't do this type of transaction (example 'delivery')"
        else:
            return Parse(data, Info_Back, Field_Name)
    def Business_Details(parameters, token, Info_Back, Field_Name='yes'):
        params_1 = {}
        params_2 = ''
        for k in parameters:
            if k == 'Alias':
                params_2 = parameters[k]
            elif k == 'locale':
                params_1[k] = parameters[k]
        headers = {
            'Authorization':'Bearer %s' % token,
        }
        r = requests.request('GET','https://api.yelp.com/v3/businesses/'+str(params_2), headers=headers, params=params_1)
        data = []
        data.append(r.json())
        data = str(data)
        if data == "[{'error': {'code': 'NOT_FOUND', 'description': 'Resource could not be found.'}}]":
            return "Incorrect Alias (example flores-mexican-restraunt-dripping-springs) and could not find business"
        else:
            return Parse(data, Info_Back, Field_Name)
    def Business_Match(parameters, token, Info_Back, Field_Name='yes'):
        parameters_threshold = 0
        for x in parameters:
            if x == 'match_threshold':
                parameters_threshold += 1
        if parameters_threshold == 0:
            parameters['match_threshold'] = 'default'
        headers = {
            'Authorization':'Bearer %s' % token,
        }
        r = requests.request('GET','https://api.yelp.com/v3/businesses/matches', headers=headers, params=parameters)
        data = []
        data.append(r.json())
        data = str(data)
        if data == "[{'error': {'code': 'NOT_FOUND', 'description': 'Resource could not be found.'}}]":
            return "No matching businesses (name & address1 & city & state & country required)"
        else:
            return Parse(data, Info_Back, Field_Name)
    def Event_Lookup(parameters, token, Info_Back, Field_Name='yes'):
        params_1 = {}
        params_2 = ''
        for k in parameters:
            if k == 'id':
                params_2 = parameters[k]
            elif k == 'locale':
                params_1[k] = parameters[k]
        headers = {
            'Authorization':'Bearer %s' % token,
        }
        r = requests.request('GET','https://api.yelp.com/v3/events/'+str(params_2), headers=headers, params=params_1)
        data = []
        data.append(r.json())
        data = str(data)
        if data == "[{'error': {'code': 'NOT_FOUND', 'description': 'Resource could not be found.'}}]":
            return "Business doesn't have an event (Alias required & example flores-mexican-restaurant-dripping-springs)"
        else:
            return Parse(data, Info_Back, Field_Name)
    def Event_Featured(parameters, token, Info_Back, Field_Name='yes'):
        keyed_loc = 0
        keyed_cor = 0
        for k in parameters:
            if k == 'location':
                keyed_loc += 1
            elif k == 'latitude':
                keyed_cor += 1
            elif k == 'longitude':
                keyed_cor += 1
        parameters_1 = {}
        parameters_2 = ''
        if keyed_loc == 1:
            for k in parameters:
                if k == 'location':
                    parameters_1[k] = parameters[k]
                elif k == 'locale':
                    parameters_1[k] = parameters[k]
        else:
            if keyed_cor == 2:
                for k in parameters:
                    for v in parameters[k]:
                        if k == 'latitude':
                            parameters_1[k] = parameters[k]
                        elif k == 'longitude':
                            parameters_1[k] = parameters[k]
                        elif k == 'locale':
                            parameters_2[k] = parameters[k]
        headers = {
            'Authorization':'Bearer %s' % token,
        }
        r = requests.request('GET','https://api.yelp.com/v3/events/featured', headers=headers, params=parameters_1)
        data = []
        data.append(r.json())
        data = str(data)
        if data == "[{'error': {'code': 'NOT_FOUND', 'description': 'Resource could not be found.'}}]" or '[{}]':
            return "Business doesn't have an featured event (location & latitude & longitude required)"
        else:
            return Parse(data, Info_Back, Field_Name)
