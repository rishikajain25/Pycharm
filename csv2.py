import csv
with open('employee.csv', 'w', newline='') as file:
    writer=csv.writer(file)
    writer.writerow(["FName", "LName", "Location", "Education", "Zip Code", "SSN"])
    writer.writerow(["Rahul", "Jain", "Florida", "MBA", 30201, 123456789])
    writer.writerow(["Jack", "Roy", "California", "MBA", 90012, 324567111])
    writer.writerow(["George", "Clay", "NYC", "Graduate", 10001, 124365789])