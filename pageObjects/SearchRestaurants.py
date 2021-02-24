class SearchRestaurants:
    # capturing web elements
    textbox_postcode_name = "postcode"
    button_search_xpath = "//button[@aria-label='Search']"
    h1_location_class = "c-locationHeader-title"
    h1_result_header_xpath = "//h1[@class='c-resultHeader-title']/span"
    section_restaurants_xpath = "//div[contains(@class,'c-listing-loader')]/div/section/a"

    # Instantiating driver object for SearchRestaurants class
    def __init__(self, driver):
        self.driver = driver

    # Entering zipcode value on homepage
    def set_postcode(self, zipcode):
        self.driver.find_element_by_name(self.textbox_postcode_name).send_keys(zipcode)

    # Clicking on search button
    def click_search(self):
        self.driver.find_element_by_xpath(self.button_search_xpath).click()

    # Get the value of location heading field
    def validate_location(self):
        location = self.driver.find_element_by_class_name(self.h1_location_class).text
        return location

    # Get the count of open restaurants by capturing the header string and splitting it by space
    def validate_result_header(self):
        result_header = self.driver.find_element_by_xpath(self.h1_result_header_xpath).text
        result_header_list = result_header.split(' ')
        open_restaurant_count = int(result_header_list[0])
        return open_restaurant_count

    # WebElement list will capture the number of elements displayed on the page prior to any scrolling (20 in this case)
    def validate_restaurants(self):
        flag = False
        restaurants_list_section = self.driver.find_elements_by_xpath(self.section_restaurants_xpath)
        for restaurant in restaurants_list_section:
            if restaurant.is_displayed():
                flag = True
            else:
                return False
        return flag
