import json

def loadSetupData():
    with open("WaCL_setup.json") as data_waterCalc:
        data = json.load(data_waterCalc)

    water_calc = data["unit_info"]
    return water_calc


def get_the_parameters_of_users():
    with open('WaCl_resident.json') as setup:
        resident_data = json.load(setup)
        return resident_data


def printing_user_info(user_info):
    user = user_info['resident']
    print('Hi ' + user['FullName'] + '\n')
    print('You`ve been logged into your account . You can observe your personal data as well as monthly water consumption`s units and the corresponding prices.'
          '\nThere are 3 different types of usage limits and their prices ,including low,average and high ones.'
          'For more detailed information ,\nyou can click on "About" in the right corner above the website.\nYour credentials are as follows: \n')
    for credential in user:
        print(credential + ' ---- ' + user[credential])


def printing_last_data(params):
    last_month = params["dates"][-1]
    for item in last_month:
        print(item + ' - ' + str(last_month[item]))


def saving_month_data(user_data, meter_data):
    dates = user_data['dates']
    usage_date = input('Please input the date as "dd.mm.yyyy":')
    unit = int(input("Please input the unit in cube meter:"))
    is_paid = input('Is it paid in a timely manner? Type "Yes" if you`ve already done it, otherwise type "No":') #check if it is paid or not
    for cube in meter_data:
        if cube == '1meter_cube_price':
            price = int(meter_data[cube])
            continue
        if unit < int(meter_data[cube]['limit']):
            price = int(meter_data[cube]['price'])
            break
    new_data = {
        "usage_date": usage_date,
        "unit": unit,
        "Price": price * unit,
        "isPaid": is_paid,
    }
    dates.append(new_data)
    return dates


def main():
    meterData = loadSetupData()
    parameters = get_the_parameters_of_users()
    printing_user_info(parameters)
    choose = int(input(
"\n In order to check or save your data ,please choose option 1 or 2 below based on your requirement.Note that there is no other option than 1 and 2 .\n\n 1-If you want to see last month data\n 2-If you want to save new data\n"))
    if choose == 1:
        printing_last_data(parameters)
    elif choose == 2:
        new_data = saving_month_data(parameters, meterData)
        parameters["dates"] = new_data
        file = open("WaCl_resident.json", "w")
        file.write(json.dumps(parameters))
        file.close()
        print('New data is saved')
    else:
        print('there`s no such option!')

main()
