# Gym-Booker
Post-Covid, many gyms are requiring time slots to be reserved in an attempt to reduce the number of people gathering. Instead of having to worry about forgetting to book the gym, I created this bot to take care of that for me.

The program first uses Selenium and the Chromedriver to load this webpage in a new Google Chrome window.

<img width="1142" alt="Screen Shot 2021-12-08 at 8 52 44 PM" src="https://user-images.githubusercontent.com/94335877/145320188-e1930e16-4e9b-428b-915a-f8f590694add.png">

After encountering this page, the program goes through a series of clicks using Selenium to navigate the website, input user credentials, and book the desired workout slot.

# Booking
In order to book successfully, first enter your username and password into the appropriate string variable assignments at the beginning of the gym_booker.py file.

The choice of workout can be customized by finding the ID of the workout. This value lies within the xpath when inspecting the html of the desired workout. Once this value is found, simply input the ID into the workout.txt file. The result is that the same workout will be booked for every following day, as the program will increment the id every day to ensure the correct slot is chosen!

After the program runs successfully, you will receive an email on your student Outlook account confirming the booking type and time.
