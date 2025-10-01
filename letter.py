import json
import os

filename = "people_list.json"
# Load names if file exists, else it will creat am emty list.
if os.path.exists(filename):
    with open(filename, "r") as f:
        people_list = json.load(f)
else:
    people_list = ["Ali", "Umar", "Faiza"]
    with open(filename, "w") as f:
        json.dump(people_list, f)

def save_people():
    """Save the updated list to file"""
    with open(filename, "w") as f:
        json.dump(people_list, f)

def send_letter(name):
    if name in people_list:
        print(f"""Dear {name},
              
I hope this message finds you well. I am writing to cordially invite you to a house party that I will be hosting at my place. It would be a great pleasure to have you join us for an evening filled with good company, laughter, and celebration.

Details of the Party:
Venue: Krachi
Date: 16th October, 1919
Time: 8:00 pm

Please feel free to bring along your good vibes and energy—we will take care of the rest! Kindly let me know if you’ll be able to make it.

Looking forward to celebrating together!

Best wishes,
Luqman.
""")              
              
              
              
              
    else:
        print(f"{name} was  not in the list. It will be added soon, so kindly come back to re check")
        people_list.append(name)  
        save_people() # save immediately after adding
        print(f"""Dear {name},
              Thank you for your patience, Kindly re enetr your name to get the letter""")     

        # Call send_letter for each person in the saved list

  


user_name = input("Please enter your name: ").strip()
send_letter(user_name)


