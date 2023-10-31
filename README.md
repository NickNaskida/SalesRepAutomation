# Sales Team Automation

## Setup
1. Clone the repository
    ```
    git clone https://github.com/NickNaskida/SalesRepAutomation.git
    ```

2. Navigate to project directory
    ```
    cd SalesRepAutomation
    ```

3. Create a virtual environment
    ```
    python3 -m venv venv
    ```

4. Activate the virtual environment
    ```
    source venv/bin/activate
    ```
   
5. Install the requirements
    ```
    pip install -r requirements.txt
    ```
   
6. Setup google service account
   - https://docs.gspread.org/en/latest/oauth2.html#for-bots-using-service-account
   - Above is the tutorial on how to setup a service account in google cloud console. (Come back to the tutorial once you download the json file with credentials)
   - Download the json file and save it in the `src` folder as `service_account.json`

7. Setup google sheet database
   - Create a google sheet with the following columns:
   - ID (A column)
   - AMOUNT (B column)
   - SALES_REP (C column)

8. Edit google sheet url in `src/config.py`. (it should look like this: https://docs.google.com/spreadsheets/d/YOUR_SHEET_ID/edit#gid=0)
```python
class DevSettings:
    """Development settings"""
    DB_SHEET_URL = "Your google sheet url"
```

9. Run the application from the root (SalesRepAutomation) folder
    ```
    python main.py
    ```

10. Enjoy! (API Swagger documentation at https://localhost:8080/docs)
