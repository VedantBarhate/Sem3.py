import csv

# with open("students.csv", 'r', newline="") as csvfile:
#     reader = csv.reader(csvfile)

#     for i in reader:
#         print(i)


# with open("students.csv", 'r', newline="") as csvfile:
#     reader = csv.DictReader(csvfile)

#     for i in reader:
#         print(i)


# data = [["max", "fy", 5.9],
#         ["bob", "sy", 8.4],
#         ["joe", "ty", 9.4],
#         ["john", "ly", 4.7],
#         ["ken", "fy", 9.4]]

# with open("data.csv", 'w', newline="") as csvfile:
#     writer = csv.writer(csvfile, delimiter="|")
#     writer.writerows(data)


data2 = [
    {"name":"max", "class":"fy", "cgpa":9.8},
    {"name":"rob", "class":"sy", "cgpa":7.5},
    {"name":"bob", "class":"ty", "cgpa":7.6},
    {"name":"joe", "class":"ly", "cgpa":4.5},
    {"name":"ben", "class":"fy", "cgpa":5.8}
]

with open("data2.csv", 'w', newline="") as csvfile:
    headers = ["name", "class", "cgpa"]
    writer = csv.DictWriter(csvfile, headers)
    writer.writeheader()
    writer.writerows(data2)