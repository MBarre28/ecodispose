print("loading completed")
# welcome page
print("Welcome to the eco-dispose recycling check")

# guideline check through.
print("Read through the recycling policy below:")
 
print("eco-dispose privacy policy")
print("\n")
print("We collect the following data for the purpose of providing tailored recycling recommendations:")
print("- Your name: This is only used for personalisation purposes during this session.")
print("-Location: This is a british website for recycling and donating, if you live any of these areas: E.g, -'London', 'Manchester', 'Birmingham', 'Cardiff' etc.")
print("- The item you wish to recycle: This helps us guide you through the appropriate disposal or recycling process.")
print("- The condition of the item: Used to give more specific advice on whether to donate, sell, or recycle.")
print("- Your location: We use this to provide local council guidelines for recycling and disposal.")
print("-We do not store or share your personal data with third parties.")
print("-Your data is only used during this session and will not be retained after the session ends.")
print("-For any questions about data protection, please contact us at support@greentechsolutions.com.")
print("\nBy proceeding, you agree to this privacy policy.\n")

# agreeing the privacy policy's terms and conditions
print("Privacy Policy:")
agree_policy = input("Do you acknowledge the privacy policy? (yes/no)").lower()

if agree_policy == "yes":
    print("Awsome, thank you!")

else:
    print("You must agree to continue or the program will end. Thank you for your time")
    exit()
    

# Asking a user if they have an account or not
account = input("Do you have an account? (yes/no)")

if account == "yes":
    print(input("Enter your full name:").lower())
    print(input("Enter your email address:").lower())

# user's info details
elif account == "no":
    print("Register your account")
    full_name = input(("What is your full-name:").lower())
    print("Thank you", full_name)
    email_address = input("Email address:").lower()
    DOB = input("Enter your date of birth (dd/mm/yyyy):")

# account has sucessfully created
print("Account Successfully Created")

# asking if the user is part of a company or individual
user = input("Are you an individual or part of a company? (individual/company)")

if user == "individual":
    print(input("Thank you, you're an individual"))

elif user == "company":
    business = input("Enter business name:")
    print("Thank you, you are with", business)

# asking the user to four devices to choose from
full_device = ("what is your device type:")
print(full_device)
device_list = input("(phone" " - desktop " "- laptop" " - tablet)").lower()
full_device = device_list


# checking the user if their device has personal storage
device_backup = input("Before donating or recycling, is your personal data stored in cloud storage?")

if device_backup == "yes":
    print("your data will reset")

# if not then it will exit the program until your phone must be stored. 

elif device_backup == "no":
    print("ensure you backup data before you donate or recycle")
    exit()

# checking if the user's device is to be recycled or donated
device = input("Do you choose to recycle or donate with your device? (donate/recycle)")

# if yes asking if the user would like to donate or recycle
if device == "donate":
    charity = input("choose a company to donate to charity:" \
    "- Oxfam , British Heart Foundation, WEEECharity, Little Lives UK")
    if charity == "Oxfam":
        print("Link to Oxfam: https://www.oxfam.org.uk/donate/")
    elif charity == "Britsh Heart Foundation":
        print("Link to Britsh Heart Foundation:" "https://www.bhf.org.uk/shop/donating-goods")
    elif charity == "WEEECharity":
        print("Link to WEEECharity: https://www.weeecharity.com")
    elif charity == "Little Lives UK":
        print("Link to Little Lives UK: https://www.littlelives.org.uk/charity-shop/fulham-broadway/")
        print("Note: This charity area is located in South West London, Fulham Broadway")
    print("Thank you")

# if no, asking if the user needs to recycle and the location
elif device == "recycle":
    location = input("Choose a location from the following lists /n: (London, Birmingham, Cardiff, Manchester)").lower()
    location_list = ("London, Birmingham, Cardiff, Manchester")

    if location == "London".lower():
        print("Link to London recycling: https://ecogreenitrecycling.co.uk/computer-recycling-london/")
    elif location is "Birmingham".lower():
        print("Link to Birmingham recycling: https://ecogreenitrecycling.co.uk/computer-recycling-birmingham/")
    elif location is "Cardiff".lower():
        print("Link to Cardiff recycling: https://www.weeecollection.co.uk/weee-waste-cardiff")
    elif location is "Manchester".lower():
        print("Link to Manchester recycling: https://www.weeecollection.co.uk/weee-waste-manchester.html")

# end program
print("Any information and queries, email through support@greentechsolutions.com")
print("Thank you for choosing ecodispose and completing the form")
exit()


