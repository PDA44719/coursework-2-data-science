from datetime import date
import time
import bcrypt


class User(object):
    """
    A user who will use the dashboard and web application.

    Args:
        first_name (str): The first name of the person, required
        last_name (str): The last or family name of the person, required
        email (str): Email address, required
        password (str): Password, required
        dob (date): Date of birth, optional with default None if value isn't provided.

    Attributes:
        first_name (str): The first name of the person
        last_name (str): The last or family name of the person
        email (str): Email address
        hashed_password (bytes): Hash value of the password string
        dob (date): Date of birth

    Methods:
        create_full_name: Creates the full names by concatenating the first names and last name
        calculate_age: Calculates the age from the date of birth
        hash_password: Create a hashed value of the string password
        is_correct_password: Checks if the string password matches the hashed password
        is_email_correct_format: Checks if the input email exists and has a gmail domain

    """

    def __init__(self, first_name: str, last_name: str, email: str, password: str, dob: date = None):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.hashed_password = self.hash_password(password)
        self.dob = dob

    def __repr__(self):
        """ String representation of a user object """
        return f" {self.first_name} {self.last_name} {self.email} {self.dob}"

    def create_full_name(self):
        """
        Create the full name by combining first_name and last_name.

        Returns
        -------
        str
            The full name of the user.

        """
        return f'{self.first_name} {self.last_name}'

    def calculate_age(self):
        """
        Calculate age based on the current date and the date of birth.

        Returns
        -------
        int or str
            The age based on the dob and today's date (int), or a message if the date of birth has not been set (str).

        """
        if self.dob is None:
            return "Age not calculated, date of birth unknown"
        else:
            today = date.today()
            age = today.year - self.dob.year - ((today.month, today.day) < (self.dob.month, self.dob.day))
            return age

    def hash_password(self, password):
        """
        Create a hashed password from the string.
        The bcrypt.hashpw() function takes a byte encoded arg, the password string therefore needs to be encoded.

        Arguments
        ---------
        password : str
            Password in string.

        Returns
        -------
        bytes
            The value of the hashed password.

        """
        salt = bcrypt.gensalt()
        self.hashed_password = bcrypt.hashpw(password.encode('utf8'), salt)
        return self.hashed_password

    def is_correct_password(self, password):
        """
        Check whether the provided password string matches the hashed password.
        The bcrypt.checkpw() function takes byte encoded args, the password string needs to be encoded.

        Arguments
        ---------
        password : str
            The string value of the password as input by the user.

        Returns
        -------
        bool
            True if there is a match and False if not.

        """
        if bcrypt.checkpw(password.encode('utf-8'), self.hashed_password):
            return True
        else:
            return False

    def is_email_correct_format(self):
        """
        Check if the input email address exists (through the use of an email API) and if that email has a gmail
        domain.
        The time.sleep(10) line simulates the 10-second API call. It is assumed that the email address exists.

        Returns
        -------
        bool
            True if the user provided an existing gmail address and False otherwise.

        """
        time.sleep(10)  # API call
        if self.email.endswith("@gmail.com"):
            return True
        else:
            return False
