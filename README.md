# Gym-Booker

Automate your gym bookings post-Covid with the Gym-Booker bot. With the McGill Gym implementing time slot reservations to ensure safety during COVID, this bot ensures you never miss your workout schedule.

## Overview

Gym-Booker is a bot designed to automate the reservation of gym slots. It uses Selenium to navigate the gym booking platform, input user credentials, and reserve the desired workout slot.

![Gym-Booking Interface](https://user-images.githubusercontent.com/94335877/145320188-e1930e16-4e9b-428b-915a-f8f590694add.png)

## Features

- **Automated Navigation:** After loading the gym booking page, the bot navigates through the website, clicking the necessary buttons to reach the reservation page.
- **User Authentication:** The bot can input user credentials to access the booking section.
- **Dynamic Workout Slot Booking:** It not only books the slot for the day but adjusts the booking ID for subsequent days to ensure your favorite slot is reserved every day.

## Setup & Usage

### Prerequisites:
- Python environment with Selenium installed.
- Google Chrome browser.

### Steps:

1. **User Credentials:** 
   - Open `gym_booker.py`.
   - Input your username and password into the appropriate string variables at the top.

2. **Choosing a Workout:** 
   - Navigate to the gym booking platform and inspect the HTML of the desired workout to find its ID (within the xpath).
   - Input this ID into the `workout.txt` file. The bot will adjust this ID for subsequent days to ensure the correct slot booking.

3. **Confirmation:** 
   - Once the bot successfully books a slot, you'll receive a confirmation email on your student Outlook account, detailing the booking type and time.

4. **Automation:** 
   - For daily automated bookings, add the execution of the `gym_booker.py` program to a crontab file. This will ensure the bot runs at your specified time every day.

## Note
Make sure your system's Google Chrome version is compatible with the ChromeDriver used by Selenium. Update ChromeDriver if necessary.
