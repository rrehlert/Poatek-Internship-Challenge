INPUT_LIST = [["Bruno", 170, 14], ["Leonardo", 174, 21], ["Juan", 156, 12], ["Juliana", 166, 13], ["Wagner",184, 17], ["Micaela", 172, 18], ["Bento", 150, 14], ["Lucia", 162, 13], ["Pedro", 169, 14], ["Carla",158, 16]]
INPUT_AGE = 13                                        #Age of students that are shorter than the average

def calculate_average_height(students):
    heights = []
    for student in students:
        heights.append(student[1])                #Get student height
    average_height = sum(heights) / len(heights)
    return average_height

def calculate_students_over_the_age(students):
    students_over_the_age = []
    for student in students:
        if student[2] >= INPUT_AGE:               #Check Student Age
            students_over_the_age.append(student)
    return students_over_the_age

def calculate_shorter_students(students, average_height):
    shorter_students = []
    for student in students:
        if student[2] < average_height:
            shorter_students.append(student)
    return shorter_students

def shorter_students_over_the_age(students):
    if not students:                                  #IF Given List is empty
        print("List of students is empty")
        return 0
    students_over_the_age = calculate_students_over_the_age(students)
    average_height = calculate_average_height(students)
    shorter_students = calculate_shorter_students(students_over_the_age, average_height)
    return shorter_students

if __name__ == '__main__':
    students = shorter_students_over_the_age(INPUT_LIST)
    print(f"There are {len(students)} students over the age of {INPUT_AGE} shorter than the average height: ")
    for student in students:
        print(f"Name: {student[0]}   Height: {student[1]}cm     Age: {student[2]} ")


