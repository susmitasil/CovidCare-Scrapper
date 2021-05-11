import csv
import os

# path = 'c:\\temp\\'
def read_info_from_csv(location):

    path = os.path.dirname(__file__)
    path = os.path.join(path,"../resources/"+location+"/")
    file=open( path +location +".csv", "r")
    reader = csv.reader(file)
# for line in reader:
#     t=line[0]
#     print(t)

    req_list = [line[0] for line in reader]
    return(req_list[1:])
    # return(req_list)


# profiles = read_info_from_csv('profiles')
# hashtags = read_info_from_csv('hashtags')

# print(profiles)
# print(hashtags)