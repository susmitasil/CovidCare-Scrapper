import requests
import os

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
    print(data.json())
    image_file_descriptor.close()