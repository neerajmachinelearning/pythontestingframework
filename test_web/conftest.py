import allure
import pytest
from delayed_assert import delayed_assert
from pyjavaproperties import Properties
from pages.base import Base
from resource import constants

prop = Properties()
# env = Properties()

obj_list = []
obj_list1 = []
@pytest.fixture(scope='function', autouse=True)
def base_fixture():
    with allure.step("Base Fixture Setup"):
        try:
            prop_path = open(constants.PROPERTYPATH)
            prop.load(prop_path)
            baseobject = Base()
            obj_list.append(baseobject)
        except Exception:
            pass
        # try:
        #     env_path = open(constants.ENVIRONMENTPATH)
        #     env.load(env_path)
        # except Exception:
        #     pass
    with allure.step("Finishing up"):
        yield locals()
        baseobject.quit_driver()

