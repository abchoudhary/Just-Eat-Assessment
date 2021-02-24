from pageObjects.SearchRestaurants import SearchRestaurants
from utilities.custom_logger import LogGeneration
from utilities.read_properties import ReadConfig


class TestSearchRestaurants:
    baseURL = ReadConfig.get_application_url()
    zipcode = ReadConfig.get_zipcode()
    logger = LogGeneration.log_generation()

    def test_search_restaurants(self, setup):
        self.logger.info("************** Test_Search_Restaurants **************")
        self.logger.info("Starting search restaurant test")
        self.driver = setup
        self.driver.maximize_window()
        self.logger.info("Opening application URL")
        self.driver.get(self.baseURL)
        self.driver.implicitly_wait(10)

        # Creating an object of the SearchRestaurants class
        self.search_rest = SearchRestaurants(self.driver)
        self.logger.info("Entering zipcode and clicking on search button")
        self.search_rest.set_postcode(self.zipcode)
        self.search_rest.click_search()

        # Checking if the zipcode in the location heading matches with zipcode entered on the home page
        location = self.search_rest.validate_location()
        if self.zipcode in location:
            self.logger.info(f"{self.zipcode} is present in the location heading: {location}")
        else:
            self.logger.error("The location does not match the zipcode entered on the home page")

        # Checking if the number of open restaurants is greater than 0
        open_restaurant_count = self.search_rest.validate_result_header()
        if open_restaurant_count > 0:
            self.logger.info(f"Number of open restaurants: {open_restaurant_count}")
        else:
            self.logger.error("No restaurants are open at this time")

        # Validating if the restaurants list is displayed or not
        status = self.search_rest.validate_restaurants()
        if status:
            assert True
            self.logger.info("Restaurant list is displayed, Test Passed")
        else:
            self.logger.error("Restaurant list is not displayed, Test Failed")
            # Capturing screenshot in case of failure
            self.driver.save_screenshot("./Screenshots/test_search_restaurants.png")
            assert False
