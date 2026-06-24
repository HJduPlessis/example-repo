"""
Starting template for creating an email simulator program using
classes, methods, and functions.

This template provides a foundational structure to develop your own
email simulator. It includes placeholder functions and conditional statements
with 'pass' statements to prevent crashes due to missing logic.
Replace these 'pass' statements with your implementation once you've added
the required functionality to each conditional statement and function.

Note: Throughout the code, update comments to reflect the changes and logic
you implement for each function and method.
"""

# --- OOP Email Simulator --- #

# --- Email Class --- #
# Create the class, constructor and methods to create a new Email object.

# Initialise the instance variables for each email.

# Create the 'mark_as_read()' method to change the 'has_been_read'
# instance variable for a specific object from False to True.


# --- Functions --- #
# Build out the required functions for your program.

class Email: #Created email class

    def __init__(self,email_address,Subject_line,email_content): #created constructor with required instant variables
        self.email_address=email_address;
        self.subject_line=Subject_line;
        self.email_content=email_content;
        self.has_been_read=False;

    def mark_as_read(self): #created mark as read method
        self.has_been_read=True;
     
def populate_inbox():
    # Create 3 sample emails and add them to the inbox list.
    email1=Email('123@gmail.com','New Subject','jchbhvudfbfj');
    inbox.append(email1);
    email2=Email('456@gmail.com','Newer Subject','jchbhgfgdfshsvudfbfj');
    inbox.append(email2);
    email3=Email('789@gmail.com','Newest Subject','jchbhvfgefghdfhtehtehtehetudfbfj');
    inbox.append(email3);


def list_emails():
    # Create a function that prints each email's subject line
    # alongside its corresponding index number,
    # regardless of whether the email has been read.
    for index,email in enumerate(inbox):
        print(f'{index} {email.subject_line}');


def read_email(index):
    # Create a function that displays the email_address, subject_line,
    # and email_content attributes for the selected email.
    # After displaying these details, use the 'mark_as_read()' method
    # to set its 'has_been_read' instance variable to True.
    email=inbox[index];
    print(f'Email address: {email.email_address}\nSubject line: {email.subject_line}\nEmail content: {email.email_content}');
    email.mark_as_read();
    print(f"Email from {email.email_address} has been marked as read.");


def view_unread_emails():
    # Create a function that displays all unread Email object subject lines
    # along with their corresponding index numbers.
    # The list of displayed emails should update as emails are read.
    for index, email in enumerate(inbox):
        if not email.has_been_read:
            print(f'{index} {email.subject_line}');


# --- Lists --- #
# Initialise an empty list outside the class to store the email objects.
inbox=[];
# --- Email Program --- #

# Call the function to populate the inbox for further use in your program.
populate_inbox();
# Fill in the logic for the various menu operations.

# Display the menu options for each iteration of the loop.
while True:
    user_choice = int(
        input(
            """\nWould you like to:
    1. Read an email
    2. View unread emails
    3. Quit application

    Enter selection: """
        )
    )

    if user_choice == 1:
        # Add logic here to read an email
        list_emails();
        index = int(input("Enter the index of the email you want to read: "));
        read_email(index)

    elif user_choice == 2:
        # Add logic here to view unread emails
        view_unread_emails()

    elif user_choice == 3:
        # Add logic here to quit application.
        print("Quitting application.")
        break

    else:
        print("Oops - incorrect input.")