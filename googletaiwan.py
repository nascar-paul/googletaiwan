from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# ... other parts of the script ...

def get_job_details(driver, url, file_path):
    driver.get(url)

    try:
        # Wait for the job listings to be loaded
        WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.CLASS_NAME, 'gc-job-list__title'))
        )
    except TimeoutException:
        print("Timed out waiting for page to load")
        return

    job_listings = driver.find_elements(By.CLASS_NAME, 'gc-job-list__title')

    with open(file_path, 'a') as file:
        for job in job_listings:
            title = job.text.strip()
            file.write(f"Title: {title}\n")

# ... rest of the script ...
