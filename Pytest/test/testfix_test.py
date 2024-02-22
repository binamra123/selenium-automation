import time



def test_example(browser):
    browser.get("https://practice.expandtesting.com/login")
    time.sleep(3)  
    assert browser.title == "Test Automation Practice: Working with Login form"

