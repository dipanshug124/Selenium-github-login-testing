class LoginPage():

    def __init__(self,driver):
        self.driver = driver

        self.username_textbox_id = "login_field"
        self.password_textbox_id = "password"
        self.login_button_class_name = "js-sign-in-button"
        self.invalidUsername_message_class_name = "//div[contains(@class, 'container-lg px-2')]"


    def username(self,username):
        self.driver.find_element_by_id(self.username_textbox_id).clear()
        self.driver.find_element_by_id(self.username_textbox_id).send_keys(username)

    def password(self, password):
        self.driver.find_element_by_id(self.password_textbox_id).clear()
        self.driver.find_element_by_id(self.password_textbox_id).send_keys(password)

    def login(self):
        self.driver.find_element_by_class_name(self.login_button_class_name).click()

    def check_if_invalid(self):
        msg = self.driver.find_element_by_xpath(self.invalidUsername_message_class_name).text
        #msg = self.driver.find_element_by_class_name(self.invalidUsername_message_class_name).text
        return msg
