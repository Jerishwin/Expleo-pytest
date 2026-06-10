import pytest
from utilities.read_config import get_config
from Actions.loginActions import LoginActions


@pytest.mark.usefixtures("setup_teardown")
class TestLogin:

    def test_login(self):

        login = LoginActions(self.driver)

        username = get_config("login","name")

        password = get_config("login","pass")

        login.login(username,password)



        assert login.get_userName().__eq__("Welcome "+username)