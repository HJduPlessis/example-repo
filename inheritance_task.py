class Course:
    # Class attribute for the course name
    name = "Fundamentals of Computer Science"

    # Class attribute for the contact website
    contact_website = "www.hyperiondev.com"

    # Method to display contact details
    def contact_details(self):
        print("Please contact us by visiting", self.contact_website)
    
    def head_office_location(self):
        print("Our head office is located in Cape Town, South Africa.");

class OOPCourse(Course):
    
    def __init__(self,description,trainer):
        super().__init__();
        self.description = description;
        self.trainer = trainer;

    def trainer_details(self):
        print("Course description:", self.description);
        print("The trainer for this course is", self.trainer);

    def show_course_id(self):
        print("Course ID: #12345");
       

# Create an instance of the OOPCourse class
course1 = OOPCourse("This course covers the basics of Object-Oriented Programming.", "John Doe");
# Call the contact_details method inherited from the Course class to display contact information
course1.contact_details();
# Call the trainer_details method to display course description and trainer information
course1.trainer_details();
# Call the show_course_id method to display the course ID
course1.show_course_id();
