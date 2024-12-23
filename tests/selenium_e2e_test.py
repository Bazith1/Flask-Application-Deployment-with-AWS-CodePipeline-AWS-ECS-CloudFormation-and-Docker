import argparse
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

def test_service_dns(service_dns):
    # Set up Chrome options
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    # Initialize the WebDriver
    service = Service('/usr/local/bin/chromedriver')
    driver = webdriver.Chrome(service=service, options=chrome_options)

    # Navigate to the service's DNS
    driver.get(f"http://{service_dns}")
    assert "Expected Title" in driver.title  # Update with the expected page title

    print("E2E Test Passed!")
    driver.quit()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run Selenium E2E test")
    parser.add_argument("--service_dns", required=True, help="Service DNS or IP address")
    args = parser.parse_args()

    test_service_dns(args.service_dns)
