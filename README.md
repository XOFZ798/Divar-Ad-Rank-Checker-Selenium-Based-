Divar Ad Rank Checker (Selenium-Based)

Description:
------------
This project is a simple Python-based web crawler designed to monitor the ranking of a specific advertisement on the Divar website (https://divar.ir). It uses Selenium WebDriver to search for the exact ad title on Divar's listing page and returns its rank. If the ad is found and its rank exceeds a defined threshold, an alarm is triggered to notify the user.

Features:
---------
- Headless Selenium automation
- Exact ad title match and normalization
- Ranking threshold alert with sound notification
- Saves HTML snapshot for debugging

Requirements:
-------------
- Python 3.10 or later
- Google Chrome (version 135 or compatible)
- pip packages listed in requirements.txt

How to Run:
-----------
1. Clone the repository:
   git clone [https://github.com/XOFZ798/Divar-Ad-Rank-Checker-Selenium-Based-]

2. Navigate to the project directory:
   cd divar-ad-rank-checker

3. Create and activate a virtual environment (optional but recommended):
   python -m venv crawler-env
   crawler-env\Scripts\activate        # Windows
   source crawler-env/bin/activate     # macOS/Linux

4. Install required packages:
   pip install -r requirements.txt

5. Run the script:
   python main.py

6. Enter the exact title of the ad when prompted.

Note:
-----
- The script saves a snapshot of the current search page as `divar_output.html` for debugging.
- Ensure your Chrome browser matches the version used by webdriver-manager.

License:
--------
This project is open-source and available under the MIT License.

Author:
-------
pouya poursafar
