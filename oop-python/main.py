# class AI_bot:
#     def __init__(self, name, color):
#         self.name = name
#         self.color = color

#     def speak(self, voice):
#         self.voice = voice
#         print(f"I am {self.name} and I am {self.voice}")

# bot1 = AI_bot("Javis", "purple") 
# bot1.speak("happy to be here")
# print("****************************************************************")

# create a class
class Bank:
    # class attributes
    bank_name = "CRDB Bank"
    bank_HQ = "Dar es Salaam"
    bank_owner = "CRDB PLC"

    # contructor
    def __init__(self, client_name, acc_name, acc_num):
        self.client_name = client_name
        self.acc_name = acc_name
        self.acc_num = acc_num

    # object/instance method
    def client_info(self):
        print(f'This client is called "{self.client_name}" with acount name "{self.acc_name}" and account number "{self.acc_num}".')
        print(f'This is the client of "{Bank.bank_name}" bank.')

    # class method
    @classmethod
    def bank_info(cls):
        print(f'The bank is called "{cls.bank_name}, owned by "{cls.bank_owner}" and located in "{cls.bank_HQ}".')

    # static method
    @staticmethod
    def my_staticmethod():
        print("This is static method")

# use classmethod
Bank.bank_info()

# create object
client_1 = Bank("Emanuel", "Emanuel Nnko", "01J234567300")
# use object/instance method
client_1.client_info()
