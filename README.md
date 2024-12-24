# UI_Project_Selenium
This project automates UI tests using Selenium and is integrated with GitHub Actions.

Selenium docs - https://www.selenium.dev/documentation/

## Setup

1. Create a virtual environment (optional):
   ```bash
   python -m venv venv
   ```
   a. Activate the virtual environment:
      - For Linux/macOS:
         ```bash
         source venv/bin/activate
      - For Windows:
         ```bash
         venv\Scripts\activate
2. Install the dependencies:
   ```bash
   pip install -r requirements.txt

3. Run tests:
    ```bash
    pytest

## Running Tests via GitHub Actions

1. Go to the **Actions** tab in this GitHub repository.
2. In the left menu, select **Python-Selenium autotests**.
3. To run the workflow:
   - Choose the test set:
     - `smoke`
     - `regression`
     - `extended`
     - `all`
4. To view the Allure Report:
   - Go to **Settings** > **Pages**.
   - Visit the site to view the report.