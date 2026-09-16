# Student Skill Analyzer
students = [
    {
        "name": "Abhinav",
        "skills": {"Python", "HTML", "CSS"}
    },
    {
        "name": "Rahul",
        "skills": {"Python", "Java", "HTML"}
    },
    {
        "name": "Aman",
        "skills": {"Python", "CSS", "JavaScript"}
    }
]
def show_students(students):
    print("====STUDENTS====")
    for student in students:
        print("Name: ", student["name"])
        print("Skills: ", student["skills"])
        print()
show_students(students)
def find_common_skills(students):
    print("===== COMMON SKILLS =====")
    common = students[0]["skills"]
    for student in students:
        common = common & student["skills"]
    print(common)
find_common_skills(students)
def find_all_skills(students):
    print("==== ALL SKILLS ====")
    union = set()
    for student in students:
        union = union | student["skills"]
    print(union)
find_all_skills(students)



  
    


    

