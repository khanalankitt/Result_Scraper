from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Setup Selenium (make sure to have the correct WebDriver for your browser)
driver = webdriver.Chrome()

# List of symbol numbers to check
symbol_numbers = [
    '79011408', '79011409', '79011410', '79011412', '79011413', '79011415', '79011417', 
    '79011419', '79011420', '79011421', '79011422', '79011424', '79011425', '79011426', 
    '79011428', '79011429', '79011430', '79011431', '79011432', '79011433', '79011434',
    '79011435', '79011436', '79011437', '79011438', '79011439', '79011441', '79011442', 
    '79011443'
]

# URL of the result website
url = "http://103.175.192.30:86/Result"

# Open a file to write results
with open('result.txt', 'w') as file:
    for symbol in symbol_numbers:
        # Navigate to the result page
        driver.get(url)

        # Wait for the custom dropdown to be clickable and click to open it
        dropdown_trigger = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "ExamScheduleId_chosen"))
        )
        dropdown_trigger.click()

        # Wait for the option "B.Sc.CSIT Third Semester" to be clickable and select it
        option_bsc_csit = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//li[text()='B.Sc.CSIT Third Semester']"))
        )
        option_bsc_csit.click()

        # Enter the symbol number
        input_field = driver.find_element(By.ID, "SymbolNo")
        input_field.clear()  # Clear the field before input
        input_field.send_keys(symbol)

        # Enter a placeholder date of birth (adjust based on actual date format)
        dob_field = driver.find_element(By.ID, "DateOfBirthBS")
        dob_field.clear()  # Clear the field before input
        dob_field.send_keys(symbol)  # Adjust to a real date of birth if necessary

        # Submit the form
        submit_button = driver.find_element(By.CLASS_NAME, "btn")
        submit_button.click()

        # Wait for the result to load (if necessary)
        driver.implicitly_wait(10)

        # Extract the result
        try:
            # Locate the specific span inside the structure you described
            name = driver.find_element(By.XPATH, "//table/tbody/tr[1]/th[1]/span").text
            result_span = driver.find_element(By.XPATH, "//table/tfoot/tr[2]/td[3]/span").text

            # Write the result to the file in the specified format
            file.write(f'Name : {name} Symbol No : {symbol} GPA : {result_span}\n')
            print(f'Name: {name}, Symbol: {symbol}, Result: {result_span}')
        except Exception as e:
            print(f'Error retrieving result for symbol {symbol}: {e}')

# Close the browser after finishing
driver.quit()
