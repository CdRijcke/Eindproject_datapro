
import csv
import json

# def name_converter(number_city):
#     if int(number_city) == 269:
#         return "Lelystad"
#     elif int(number_city) == 270:
#         return "Leeuwarden"

def check_fill(number_value, month_variable):
    if not number_value.isspace():
        return number_value
    else:
        return (month_variable/counter)

# converts the KNMI_data.csv file to  the KNMI_info.json file
temp_store = {}

with open('BMI_obesity.csv', 'r') as csvfile:
    barchart_csv = csv.reader(csvfile)
    types = barchart_csv.next()
    print types
    years = barchart_csv.next()
    print years
    first = barchart_csv.next()
    print first
    first = barchart_csv.next()
    print first
    first = barchart_csv.next()
    print first
    print years[3] # year
    print years[1] # country_code
    print years[0] # country_name
    print years[2] # sex
    print years[4] # mean BMI
    print years[7] # mean overweight
    print years[10] #  mean obesity

    temp_store = {years[3]:{years[2]:"super obese"}}


    for line in barchart_csv:
        if line[3] in temp_store.keys():
            if line[2] in temp_store[line[3]].keys():
                temp_store[line[3]][line[2]] = {line[1]:"hoi"}
                # {"mean_bmi":line[4], "country_code": line[1], "country_name": line[0], "fraction_overweight": line[7], "fraction_obese":line[10]}
            else:
                temp_store[line[3]][line[2]] = {line[1]:{"mean_bmi":line[4], "country_code": line[1],"country_name": line[0], "fraction_overweight": line[7], "fraction_obese":line[10]}}
        else:
            temp_store[line[3]] = {line[2]:{line[1]:{"mean_bmi":line[4], "country_code": line[1],"country_name": line[0], "fraction_overweight": line[7], "fraction_obese":line[10]}}}

    print temp_store, "\n"
    print temp_store["1992"]
    first = True

    country_list = []
    country_data = {}
    setted_country_list = set(country_list)

    # with open('obesity_data.json', 'w') as outfile:
    #     outfile.write('[')
    #     for first_line in barchart_csv:
    #         print first_line[6]
    #     csvfile.close()
    #     with open('data-verbose.csv', 'r') as csvfile:
    #         barchart_csv = csv.reader(csvfile)
    #     for first_line in barchart_csv:
    #         print first_line[7]
        #     setted_country_list = set(country_list)
        #     if first_line[10] not in setted_country_list and first_line[1] == "2011":
        #         country_list.append(first_line[10])
        #         with open('vegetables_import.csv', 'r') as csv_file:
        #             import_file = csv.reader(csv_file)
        #             for second_line in import_file:
        #                 if first_line[10] == second_line[10] and first_line[1] != second_line[1]:
        #                     country_data[second_line[1]] = second_line[31]
        #                     print "secondline:  ", second_line
        #             if first == True:
        #                 json.dump({str(first_line[10]):{"country": first_line[9], "2011" : str(first_line[31]), "2012" : str(country_data["2012"]), "2013" : str(country_data["2013"]), "2014" : str(country_data["2014"]), "2015" : str(country_data["2015"])}}, outfile)
        #                 first = False
        #             else:
        #                 outfile.write(',\n')
        #                 json.dump({str(first_line[10]):{"country": first_line[9], "2011" : str(first_line[31]), "2012" : str(country_data["2012"]), "2013" : str(country_data["2013"]), "2014" : str(country_data["2014"]), "2015" : str(country_data["2015"])}}, outfile)
        # outfile.write(']')
        # print "JSON file created"
    # outfile.close()
