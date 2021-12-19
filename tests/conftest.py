import pytest
import user


@pytest.fixture
def user_dob_modifiable(input_dob):
    """
    Create a user (from the User class defined in user.py).

    Arguments
    ---------
    input_dob : datetime.date
        The date of birth of the user.

    Returns
    -------
    user.User
        The created instance of the User class.

    """
    created_user = user.User(first_name="James", last_name="Gordon", email="jgordon23@gmail.com",
                             password="jgordonpass", dob=input_dob)
    return created_user


@pytest.fixture
def user_email_modifiable(email_address):
    """
    Create a user (from the User class defined in user.py).

    Arguments
    ---------
    email_address : str
        The email address of the user.

    Returns
    -------
    user.User
        The created instance of the User class.

    """
    created_user = user.User(first_name="James", last_name="Gordon", email=email_address,
                             password="jgordonpass", dob=None)
    return created_user
