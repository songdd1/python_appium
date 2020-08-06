from time import sleep

from xueqiu.page.app import App


class TestCase():

    def setup(self):
        self.app = App()
        self.app.stat()

    def teardown(self):
        self.app.stop()

    def test_case1(self):
        self.app.go_to_main().go_to_market().search_content().iuput_content()
        sleep(5)
            #.select_content().search_result()


