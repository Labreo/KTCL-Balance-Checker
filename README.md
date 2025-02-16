# KTCL-Balance-Checker
-Script to automatically send whatsapp message if Kadama bus transport card is low on balance.
This Python script checks your KTCL smart card balance and sends a WhatsApp notification if the balance is below a certain threshold.

## Features
- Scrapes KTCL website for card balance
- Sends an automatic WhatsApp message if balance is low
- Uses WhatsApp Web for messaging (requires login)

## Requirements
- Python 3.x
- Web browser installed (for WhatsApp Web automation)
- Required Python libraries (install using `requirements.txt`)
- Configure own whatsapp number and details in the script.
  
## Installation
1. Clone or download this repository.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage
1. Run the script:
   ```bash
   python ktc.py
   ```
2. Enter your KTCL card number and WhatsApp phone number when prompted.
3. The script will fetch your balance and send a WhatsApp message if the balance is low.

## Automating on Windows Task Scheduler
1. Open **Task Scheduler** (`taskschd.msc` via Run dialog `Win + R`).
2. Click **Create Basic Task** and name it appropriately.
3. Choose **Daily** or your preferred schedule.
4. Select **Start a Program**, then browse for `python.exe`.
5. Add arguments: `path\to\ktc.py`.
6. Click **Finish** to schedule the task.

## Automating on Linux (Cron Job)
1. Open Terminal and type:
   ```bash
   crontab -e
   ```
2. Add the following line to schedule it daily at 9 AM:
   ```bash
   0 9 * * * /usr/bin/python3 /path/to/ktc.py
   ```
3. Save and exit. Use `crontab -l` to verify the scheduled job.

## Notes
- WhatsApp Web must be logged in.
- This script relies on web scraping, so any changes to the KTCL website may break functionality.

## Disclaimer
This project is for educational purposes only. Use at your own risk.
```

