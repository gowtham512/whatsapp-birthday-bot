# whatsapp-birthday-bot
It is common social practise to send birthday greetings to friends, family, colleagues, and acquaintances. However, keeping track of multiple birthdays and remembering to send birthday wishes on time can be difficult. This problem is addressed by the Birthday Bot, which automates the entire process, making it more efficient and convenient.

Code explanation:
It imports the necessary libraries: pywhatkit for sending WhatsApp messages, pandas for working with CSV files, time for introducing delays, datetime for getting the current date and time, and random for generating random numbers.

It gets the current date and formats it as "day-month" using the datetime.today().strftime("%d-%m") method.

It reads a CSV file named 'contacts.csv' using pd.read_csv() and stores the data in a pandas DataFrame called df. This file should contain columns named 'Date' and 'Phone' for storing the date and phone number of each contact.

It iterates through each row of the DataFrame using df.iterrows().

For each row, it retrieves the date and phone number from the 'Date' and 'Phone' columns, respectively.

If the date from the CSV matches the current date, it proceeds with sending a WhatsApp message.

It gets the current time (hour, minutes, seconds) using datetime.now().

If the current time is within the first 50 seconds of a minute, it selects a random image (either 1 or 2) from the 'birthday_images' folder and sends it as a WhatsApp message using pywhatkit.sendwhats_image(). It also introduces a delay of 30 seconds using time.sleep() to avoid message sending issues.

If the current time is after the 50th second, it directly sends a random image from the 'birthday_images' folder and introduces a delay of 30 seconds.

After sending the message, it prints "Successfully Sent!".
