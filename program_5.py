# # Program #5: Course Info
# # Write a program that has the user input a bunch of course ID and course name pairs.
# # For example a course ID could be "COS 2005" and the course name could be "Python Programming."
# # Then ask the user for a subject (like "COS").
# # Finally, the program will display the ID and name of all the courses having that subject.

def main():
    courses = {}

    # Collect course info from users
    while True:
        CourseID = input("Enter course ID or 'done' to finish: ")
        if CourseID.lower() == 'done':
            break
        CourseName = input("Enter course name: ")
        Subject = input("Enter course subject: ")
        courses[CourseID] = {"Course name": CourseName, "Subject": Subject}

    SearchSubject = input("Name of subject to search: ").upper()
    found_courses = False

    for CourseID, CourseDetails in courses.items():
        if SearchSubject in CourseID.upper():
        #if CourseDetails["CourseName"].upper() == SearchSubject:
            print(f"Course ID: {CourseID}, Course Name: {CourseDetails['Course name']}")
            found_courses = True

    if not found_courses:
        print("No course found.")

if __name__ == '__main__':
    main()
