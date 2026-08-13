students = [ [201, "Arun Kumar", "11", 87],
             [202, "Meenakshi R", "12", 82],
             [203, "Rajeshwari Nair", "12", 100],
             [204, "Suresh Babu", "11", 76],
             [205, "Anitha Subramaniam", "11", 99] ]



centum = []
for student in students:
        if student[3] == 100:
            centum.append(student[0:2])

print(centum)

