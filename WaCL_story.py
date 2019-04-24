import json

def loadSetupData():
    with open("WaCL_setup.json") as data_waterCalc:
        data = json.load(data_waterCalc)


    water_calc = data["unit_info"]
    return water_calc

def get_the_parameters_of_users():
    with open('WaCl_resident.json') as setup:
        resident_data =json.load(setup)
        return resident_data

def printing_user_info(user_info):
    user = user_info['resident']
    print('Hi ' + user['FullName'] + '\n')
    print('These are your credentials: \n')
    for credential in user:
        print(credential + ' ---- ' + user[credential])

def printing_last_data(params):
    last_month = params["dates"][-1]
    for item in last_month:
        print(item + ' - ' + str(last_month[item]))
    
    
def saving_month_data(user_data,meter_data):
    dates = user_data['dates']
    usage_date = input("Please input the date:")
    unit = int(input("Please input the unit:"))
    is_paid = input("Is it paid? Yes or No:")
    for cube in meter_data:
        if cube == '1meter_cube_price':
            price = int(meter_data[cube])
            continue
        if unit < int(meter_data[cube]['limit']):
            price = int(meter_data[cube]['price'])
            break
    new_data = {
        "usage_date":usage_date,
        "unit":unit,
        "Price":price*unit,
        "isPaid":is_paid,
    }
    dates.append(new_data)
    return dates

def main():
    meterData = loadSetupData()
    parameters = get_the_parameters_of_users()
    printing_user_info(parameters)
    choose = int(input("\n\nPlease choose option 1 or 2:\n 1-If you want to see last month data\n 2-If you want to save new data\n"))
    if choose == 1:
        printing_last_data(parameters)
    elif choose == 2:
        new_data = saving_month_data(parameters,meterData)
        parameters["dates"] = new_data
        file = open("WaCl_resident.json", "w")
        file.write(json.dumps(parameters))
        file.close()
        print('New data is saved')
    else:
        print('You chose wrong option')

main()


