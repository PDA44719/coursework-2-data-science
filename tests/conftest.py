import datetime

import pytest
import user


@pytest.fixture
def new_user1(input_dob):
    created_user = user.User(first_name="James", last_name="Gordon", email="jgordon23@gmail.com",
                             password="jgordonpass", dob=input_dob)
    return created_user


@pytest.fixture
def new_user2(email_address):
    created_user = user.User(first_name="James", last_name="Gordon", email=email_address,
                             password="jgordonpass", dob=None)
    return created_user


"""
@pytest.fixture(params=['jgordon23@gmail.com', 'no_email'])
def email_address(request):
    return request.param
    
"""
