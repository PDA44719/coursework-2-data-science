import pytest
import datetime


class TestUser:
    @pytest.mark.parametrize('input_dob,expected_age', [(None, 'Age not calculated, date of birth unknown'),
                                                        (datetime.date(1981, 2, 5), 40)])
    def test_calculate_age(self, new_user1, expected_age):
        """
        GIVEN a new user (created as a fixture)
        WHEN the user has not input a date of birth (dob is None)
        THEN calculate_age() must return "Age not calculated, date of birth unknown".
        ELSE WHEN the user has input a date of birth
        THEN calculate_age() must return an integer corresponding to the expected age.
        """
        age = new_user1.calculate_age()
        assert age == expected_age

    @pytest.mark.parametrize('input_dob', [None])
    @pytest.mark.parametrize('input_password,expected_result', [("jgordonpass", True), ("notjgordonpass", False)])
    def test_is_correct_password(self, new_user1, input_password, expected_result):
        assert new_user1.is_correct_password(input_password) is expected_result

    @pytest.mark.parametrize('input_dob', [None])
    def test_create_full_name(self, new_user1):
        assert new_user1.create_full_name() == "James Gordon"

    @pytest.mark.parametrize('email_address,expected_outcome', [("jgordon23@gmail.com", True), ("no_email", False)])
    def test_is_email_correct_format(self, new_user2, expected_outcome):
        assert new_user2.is_email_correct_format() is expected_outcome
