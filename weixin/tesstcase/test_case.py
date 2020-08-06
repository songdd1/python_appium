import pytest
import yaml

from weixin.page.app import App

with open('../data/datas.yml') as f:
    addcon = yaml.safe_load(f)

class TestCase():


    def setup_class(self):
        self.app = App()
        self.main = self.app.start().go_to_main()

    def teardown_class(self):
        self.app.stop()

    @pytest.mark.parametrize('name,sex,phone',addcon)
    def test_case1(self, name, sex, phone):
        # name = "song4"
        # sex = "女"
        # phone = '16346634343'
        mymsg =self.main.go_to_teamlist().add_contact().\
            add_input().\
            set_name(name).\
            set_sex(sex).\
            set_phone(phone).click_save()
        text = mymsg.get_toast()
        assert '成功' in text
        self.app.bank()



    def test_case2(self):
        pass