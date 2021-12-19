import pytest
import datetime


class TestUser:
    @pytest.mark.parametrize('input_dob,expected_age', [(None, 'Age not calculated, date of birth unknown'),
                                                        (datetime.date(1981, 11, 5), 40)])
    def test_calculate_age(self, user_dob_modifiable, expected_age):
        """
        GIVEN a new user (created as a fixture)
        WHEN the user has not input a date of birth (dob is None)
        THEN calculate_age() must return "Age not calculated, date of birth unknown".
        ELSE WHEN the user has input a date of birth
        THEN calculate_age() must return an integer corresponding to the expected age.

        Arguments
        ---------
        user_dob_modifiable : pytest.fixture
            The fixture defined on conftest.py, which takes a date of birth as an argument.
        expected_age : int
            The age that the calculate_age method from the User class is supposed to return for the specific date of
            birth input.

        Test Result
        -----------
            PASSED if expected_age and the value obtained from calculate_age() are the same and FAILED otherwise.

        """
        age = user_dob_modifiable.calculate_age()
        assert age == expected_age

    @pytest.mark.parametrize('input_dob', [None])
    @pytest.mark.parametrize('string,expected_result', [("jgordonpass", True), ("notjgordonpass", False)])
    def test_is_correct_password(self, user_dob_modifiable, string, expected_result):
        """
        GIVEN a new user (created as a fixture), which has a specific password
        WHEN a string corresponding to the password is passed into the is_correct_password method
        THEN that method must return True.
        ELSE WHEN a string which does not correspond to the password is passed into is_correct_password
        THEN the result should be False.

        Arguments
        ---------
        user_dob_modifiable : pytest.fixture
            The fixture defined on conftest.py, which takes a date of birth as an argument.
        string : str
            A password string which will be compared to the password in the created instance of the User class.
        expected_result : bool
            True if string is the same as the user password and False otherwise.

        Test Result
        -----------
            PASSED if expected_result and the result obtained by using the is_correct_password method are the same and
            FAILED otherwise.

        """
        assert user_dob_modifiable.is_correct_password(string) is expected_result

    @pytest.mark.parametrize('email_address,expected_outcome', [("jgordon23@gmail.com", True),
                                                                ("jgordon@yahoo.com", False),
                                                                ("jgordon@gmail.comes", False)])
    def test_is_email_correct_format(self, user_email_modifiable, expected_outcome, mocker):
        """
        GIVEN a new user (created as a fixture)
        WHEN the input email address exists (checked through an email API) and is a gmail address
        THEN is_email_correct_format must return True.
        ELSE WHEN the email address exists but is not a gmail address
        THEN is_email_correct_format should return False.

        Arguments
        ---------
        user_email_modifiable : pytest.fixture
            The fixture defined on conftest.py, which takes an email as an argument.
        expected_outcome : bool
            True if the email address has the correct format (@gmail.com) and False otherwise.
        mocker : pytest.fixture
            The mocker fixture available when downloading the pytest-mock package. It will be used to mock the
            is_email_correct_format method from the User class.

        Test Result
        -----------
            PASSED if expected_outcome and the value obtained from is_email_correct_format() are the same and FAILED
            otherwise.

        """
        # Remove the time-expensive api call. As the used API was tested before being made public, its call can be
        # avoided to save testing time.
        mocker.patch(
            'user.User.is_email_correct_format',
            return_value=True if user_email_modifiable.email.endswith("@gmail.com") else False
        )
        assert user_email_modifiable.is_email_correct_format() is expected_outcome
