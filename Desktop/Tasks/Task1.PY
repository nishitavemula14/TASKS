students = [
("Anil", 78),
("Ravi", 45),
("Meena", 88),
("Sita", 62),
("Raj", 49)
]

#create a dictionary
results ={}

pass_count = 0
fail_count = 0

for student in students:
    name, marks = student
    if marks >=50:
        results[name] = "pass"
        pass_count += 1
    else:     
        results[name] = "fail"
        fail_count += 1
print("Results:", results)
print("Number of students who passed:", pass_count)
print("Number of students who failed:", fail_count)
