import requests
import os
# from csv import *
import csv

url = 'http://covidtextlabel.centralindia.cloudapp.azure.com:5000/add'

def upload_files_by_folder():
    
    path = os.path.dirname(os.path.realpath('__file__'))
    print(path)
    folder = os.path.join(path,'data_collected\hashtags\covid_resources\\')
    print(folder)

    for files in os.listdir(folder):
        image_file_descriptor = open(folder+files , "rb")
        print(image_file_descriptor)
# Requests makes it simple to upload Multipart-encoded files 
        files_data = {'image': image_file_descriptor}
# url = '...'
        data = requests.post(url, files=files_data)
        print(data.json())
        image_file_descriptor.close()

def upload_single_file(file_path):
    image_file_descriptor = open(file_path , "rb")
    print(image_file_descriptor)
# Requests makes it simple to upload Multipart-encoded files 
    files_data = {'image': image_file_descriptor}
# url = '...'
    data = requests.post(url, files=files_data)
    # print(data.json())
    image_file_descriptor.close()
    collect_records(data.json())

def collect_records(json_data):
    path = os.path.dirname(os.path.realpath('__file__'))
    print(path)
    folder = os.path.join(path,'data_collected\\records\\')
    field_names = ['help_cat','help_type','loc','loc_extra','nums','per','text','tid','time']

    with open(folder+'record.csv', 'a') as f_object:

    # Pass the file object and a list 
    # of column names to DictWriter()
    # You will get a object of DictWriter
        dictwriter_object = csv.DictWriter(f_object, fieldnames=field_names)
        # Tot_rows=len(dictwriter_object) 
        # print(Tot_rows)
    #Pass the dictionary as an argument to the Writerow()
        dictwriter_object.writerow(json_data)
  
    #Close the file object
        f_object.close()

    # with open('records.csv','r',encoding='UTF-8') as F0: 
	#     Reader=csv.reader(F0,delimiter=',') 
	#     Rows=list(Reader) 
	#     Tot_rows=len(Rows) 

# collect_records({'help_cat':'hi','help_type':'hi','loc':'hi','loc_extra':'hi','nums':'hi','per':'hi','text':'hi','tid':'hi','time':'hi'})