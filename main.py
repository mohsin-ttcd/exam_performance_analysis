
# Open file at complexity of O(n)  where $N$ is the total number of lines in the file
with open("Student-Data/student_data.csv", "r") as f:
    for i in f:
        print(i.strip())