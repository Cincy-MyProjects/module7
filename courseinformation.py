r_numbers = {
    'CSC101': '3004',
    'CSC102': '4501',
    'CSC103': '6755',
    'NET110': '1244',
    'COM241': '1411'
}
instructors = {
    'CSC101': 'Haynes',
    'CSC102': 'Alvarado',
    'CSC103': 'Rich',
    'NET110': 'Burke',
    'COM241': 'Lee'
}
m_times = {
    'CSC101': '8:00 am',
    'CSC102': '9:00 am',
    'CSC103': '10:00 am',
    'NET110': '11:00 am',
    'COM241': '1:00 pm'
}

course_number = input("Enter course number: ").strip().upper()

if course_number in r_numbers:
    print(f"The course number is : {course_number}")
    print(f"Course's room number is : {r_numbers[course_number]}")
    print(f"Course's instructor is : {instructors[course_number]}")
    print(f"Course's meeting time is : {m_times[course_number]}")
else:
    print("Invalid course number. Please try again.")