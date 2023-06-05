#checks the database to see if the tensor exists in the database and will then send a message to the phone and lock depending on the outcome 

import paho.mqtt.publish as publish
import communication.checkDatabase as checkDatabase
import iphone
def compareDatabase(input_tensor):
    if checkDatabase.parse_database(input_tensor):
        print("Found In Database, Will be allowed in!")
        publish.single("CoreElectronics/sender", "Open Lock", hostname="test.mosquitto.org")
        iphone.send_message("Person was recognized, and door will unlock!")


    else:
        print("Not Found In Database!")
        
        iphone.send_message("Person was not recognized!")
        question = input("Would you like to add this person to the database?")
        if question == 'yes':
            checkDatabase.append_database(input_tensor)
            print("Person was added to database")
        else:
            print("Person was not added to database")
