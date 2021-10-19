class HomePage():

    def __init__(self,driver):
        self.driver = driver

        self.welcome_class_name = "js-feature-preview-indicator-container"
        self.logout_class_name = "dropdown-signout"

    #welcome_class_name
    def welcome(self):
        self.driver.find_element_by_class_name(self.welcome_class_name).click()

    def logout(self):
        self.driver.find_element_by_class_name(self.logout_class_name).click()