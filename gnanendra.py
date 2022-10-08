import requests

URL = "<jenkins server>/computer/api/json"

responce = requests.get(URL)

data = responce.json()
# data = responce.content

my_len = len(data["computer"])
print(my_len)
my_len = my_len - 1

for i in range(0, my_len):
    # print(data["computer"][i]["assignedLabels"][0]["name"])
    if data["computer"][i]["offline"] is True:
        print(" stopped slave: {}, slave name: {}".format(data["computer"][i]["offline"],
                                                          data["computer"][i]["assignedLabels"][0]["name"]))
        # file_object = open("filename", "mode")
        f = open("offline_slaves.txt", "w+")
        f.write(" stopped slave: {}, slave name: {}".format(data["computer"][i]["offline"],
                                                          data["computer"][i]["assignedLabels"][0]["name"]))
        # f.close()
