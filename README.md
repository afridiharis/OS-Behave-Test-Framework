
# BDD Test Automation Framework

Overview
This project is a Behavior Driven Development (BDD) test automation framework built using Behave and Selenium WebDriver. 

Page Object Model (POM)
The framework uses the Page Object Model to maintain separation between test logic and page structure.

For outputting, logging debugs and info lines as well as screenshots are taken in case of test failures

For Reporting a tool called `behave-html-pretty-formatter` is used to generate pretty HTML reports with screenshots attached for failing tests 



## Running the Tests Manually

### **Prerequisites**

Before you start, ensure that you have the following installed:

`Python 3.x`: Download Python
`pip`: Python package manager (usually comes with Python)

**Installation Steps:**

#### Will require a vitualenv environment as a subshell is being opened to run the behave command in runner.py script

> *May have to start with `python3`*
`python -m pip install virtualenv`
`python -m virtualenv env_name`
`source env_name/bin/activate`

`pip install -r requirements.txt`

*NOTE!* A `runner.py` file is used to run the tests and execute the behave command. 

To get help using runner.py run command `python runner.py -h`

1. **Run All Tests:**

`python runner.py --test_dir=Features`

2. **Run Specific Tag:**
To run tests with a specific tag, for example @download_page:

`python runner.py --behave_options='--tags=download_page' --test_dir=Features`

3. **Run Tests with HTML report out:**
`python runner.py --behave_options='--tags=download_page' --output_html=yes --test_dir=Features`


## Details on the test reports produced by the test execution.

When running against specific tag i.e. 
`python runner.py --behave_options='--tags=download_page' --output_html=yes --test_dir=Features`

As shown in the screenshot below (local run) the scenario tagged with @download_page is run. The logs show all the elements being checked for and their locators and when they are found
![passing tagged test](test_report_details/Screenshot.png)


Running the same test in the html report generated output (console view):
![passing tagged test](test_report_details/Screenshot 2024-10-02 at 06.19.50.png)

HTML report for the passing downloads page test (web view):
![passing tagged test](test_report_details/Screenshot 2024-10-02 at 06.21.55.png)


### Failing Tests - report details:

> Can be viewed in browser directly - located in `test_report_details/behave-report-all-tests-two-fails.html`

The captured will help facilitate me in finding and diagnosing the problem with expected versus actual outputs I can easily figure out why the assertions are failing
Also more importantly by attaching the failing tests screenshots I know what happened around that time on the webpage

The below test report shows all the scenarios run in around half a minute with two scenarios failing. Also showing the duration for each scenario
![passing tagged test](test_report_details/Screenshot 2024-10-02 at 06.41.53.png)


In here the attached screenshot of failing test can be seen
![passing tagged test](test_report_details/Screenshot 2024-10-02 at 06.42.15.png)


In this screenshot the test report gives you two options to view the Error Message and the Traceback both helping to diagnose and figure out the failures. In this case it was an assertion and clearly shows the expected and actual values being different
![passing tagged test](test_report_details/Screenshot 2024-10-02 at 06.42.32.png)

Another example of screenshot captured in helping find the issue is this where the page wasnt fully loaded before running the tests:
![passing tagged test](test_report_details/Go_to_OS_Data_Homepage-element_not_visible.png)


### Passing Tests - report details:

> Can be viewed in browser directly - located in `test_report_details/behave-report-all-tests-passing.html`

Locally all the captured logs are shown so you can keep a track and keep an eye on all the elements found and displayed:
![passing tagged test](test_report_details/Screenshot 2024-10-02 at 07.07.56.png)



On the html reporting all the tests are shown to pass and has their durations next to them
![passing tagged test](test_report_details/Screenshot 2024-10-02 at 07.13.45.png)

Here is the view of the local console without the `-o` output:
![passing tagged test](test_report_details/Screenshot 2024-10-02 at 07.16.56.png)


## Running Tests Via Build Process

### Jenkins Freestyle Project
In order to setup the freestyle project I needed to setup the shell execute and parameterize the test run so tags can be passed in successfully as well as tests directory
![passing tagged test](test_report_details/Screenshot 2024-10-02 at 22.01.26.png)
![passing tagged test](test_report_details/Screenshot 2024-10-02 at 22.03.31.png)

Below can be seen a test run against a tag: @homepage being successfully run:
![passing tagged test](test_report_details/Screenshot 2024-10-02 at 22.04.56.png)



Screenshot below shows full test suite run built as a test job
![passing tagged test](test_report_details/Screenshot 2024-10-02 at 21.58.14.png)




