#Smart_Metre
'''
• This is a simple smart meter program which gives the user charge to pay based on the units consumed.
• The program is designed to be user-friendly and easy to understand.
• It also sends a message to the user with the bill amount using the pywhatkit library.
• The program is designed to be run in a terminal or command prompt.
'''

from time import sleep
import pywhatkit

print("Welcome to the Smart Meter Program!")
sleep(2)

def send_message(phone_number, bill,units):
    message = (
    "📄 *Electricity Bill Notification*\n\n"
    f"🔌 Units Consumed: *{units} units*\n"
    f"💰 Total Amount: *₹{bill:.2f}*\n\n"
    "Please ensure timely payment to avoid disconnection.\n"
    "Thank you for using *Smart Meter Services*. ⚡"
)
    pywhatkit.sendwhatmsg_instantly(phone_number, message)
    print("Message sent successfully!")


def calculate_bill(units):
    """
    Calculate the bill based on the number of units consumed.
    The rates are as follows:
    - First 100 units: ₹5 per unit
    - Next 100 units: ₹10 per unit
    - Above 200 units: ₹15 per unit
    """
    if units <= 100:
        bill = units * 5
    elif units <= 200:
        bill = (100 * 5) + ((units - 100) * 10)
    else:
        bill = (100 * 5) + (100 * 10) + ((units - 200) * 15)
    
    print(f"Your bill is: ₹{bill: .2f}")
    phone = input("Enter your phone number (with country code): ")
    sleep(1)
    print("Sending message...")
    send_message(phone, bill,units)


try:
    units = float(input("Enter the number of units consumed: "))
    if units < 0:
        raise ValueError("Units cannot be negative.")
    

except ValueError as ve:
    print(f"Invalid input: {ve}")

if __name__ == "__main__":

    calculate_bill(units)

