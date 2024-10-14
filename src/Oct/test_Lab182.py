# Fixture - Concept in python
# You can use the ficture
# context to the test.
# Similar to Pre-Condition, Post-Condition

# Simply- Before or after making the request what we want to do, we can do by using Fixture
# For eg. --> If you want to run update test case(PUT/PATCH), we need token ID.
# test_Update_negative 1
# test_Update_positive 2

# How to create Fixture

import pytest
@pytest.fixture()
def is_married():
    return True
#injecting above in TC
def test_i_need_confirm(is_married):
    assert is_married == False

    # is_married is going to replace with True because above funstion is_married is returning True

