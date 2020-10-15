from pages.dashboad_page import DashboardPage

class TestDashboardPage():
    def test_is_it_dashboard(self, browser):
        self.link = "https://test.banksend.com/admin/dashboard"
        page = DashboardPage(browser, self.link)
        page.user_log_in()
        page.should_be_dashboard_page()
        page.shoud_be_dashboard_in_url()


