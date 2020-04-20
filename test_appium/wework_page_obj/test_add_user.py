import time

import pytest

from .page.app import App


class TestAddContact:
    def setup_class(self):
        self.main = App().start().main()

    @pytest.mark.parametrize('username, gender, tel', [('test1', '男', '12312312312'), ])
    def test_add_user(self, username, gender, tel):
        invite_user_page = self.main.click_address_list(). \
            click_add_user().click_manual_add(). \
            input_name(username).set_gender(gender).input_phone(tel). \
            click_save()
        time.sleep(2)
        _, toast_el = invite_user_page.get_verify_toast()
        assert '添加成功' in toast_el.text
        invite_user_page.click_back()
