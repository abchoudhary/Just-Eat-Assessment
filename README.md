# Just Eat Assessment 
### Selenium with Python in Hybrid Framework using pytest

**Pre-requisite:**
Python should be pre-installed in your system.

**Setup:**
1. Download the zip file in your computer at any desired location.
2. Extract the zip file to a folder.
3. Goto your project directory via command prompt and install below mentioned packages:
    * selenium
      ```
      pip install selenium
      ```
    * pytest
      ```
       pip install pytest
      ```
    * pytest-html (for reporting)
      ```
      pip install pytest-html
      ```
    * *Note:* pip is included by default with the Python binary installers above version 3.4
   

4. Download Chrome and Firefox browser drivers from below mentioned links, extract the zip files and provide the absolute path of .exe file in 'setup' method of 'conftest.py' file under testCases folder.
    * [chrome driver](https://chromedriver.storage.googleapis.com/88.0.4324.96/chromedriver_win32.zip)
    * [firefox/gecko driver](https://github.com/mozilla/geckodriver/releases/download/v0.29.0/geckodriver-v0.29.0-win64.zip)
    
* *Note:* For the ease of execution, I have placed the required drivers in the project directory under drivers folder and passed the relative path in 'setup' method of 'conftest.py' file, so you can ignore Step 4.
  
**Execution:**
* Using command prompt, goto your project directory and run the 'Run.bat' file. The batch file contains pytest commands to execute the test cases.
  ```directory_path>Run.bat```

**Results:**
* Test cases should execute successfully on both chrome and firefox browser one after another.
   * automation logs will be generated in Logs folder.
   * html reports will be generated in Reports folder.
   
**Comments:**
1. Currently, I have absolute path of chrome and firefox drivers in 'conftest.py' file as I kept the drivers on my desktop while testing.
2. To avoid passing the executable path in 'setup' method of 'conftest.py' file, keep the .exe files of browser drivers in 'Scripts' folder at a location where python is installed and add the path of both 'Scripts' folder and 'Python' folder to 'Path' system variable in environment variables.
    
**Folder Structure:**
```
Project
├── Configurations
│   ├── config.ini (to store common info like application URL)
|
├── pageObjects
|   ├── page_object_file.py (contains webelements, getter and setter methods)
|
├── testCases
|   ├── conftest.py (contains pytest fixtures for browser and reports etc.)
|   ├── pytest.ini (to store custom pytest markers)
|   ├── test_filename.py (contains test methods)
|    
├── utilities
|   ├── custom_logger.py (contains logging setup)
|   ├── read_properties.py (to read data from config.ini by using configparser) 
|
├── Logs
├── Reports
├── Screenshots
├── TestData
├── README.md
└── Run.bat (To execute test cases)
```
