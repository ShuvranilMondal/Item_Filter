import pyttsx3


def speech(n):
    myvoice = pyttsx3.init()
    voices = myvoice.getProperty('voices')
    for voice in voices:
        myvoice.setProperty('voice',voice.id)
    voice_rate = 150
    myvoice.setProperty('rate',voice_rate)
    myvoice.say(n)
    myvoice.runAndWait()
    return n



class Laptop:
    discount = 0
    total = 0
    def __init__(self , name , ram , HDD , SSD , GPU , price , cpu):
        Laptop.total += 1
        self.name = name
        self.ram = ram 
        self.HDD = HDD
        self.SSD = SSD
        self.GPU = GPU
        self.price = price

    def gameing(self):
        if self.GPU == 'none':
            return ('you can not run high end game ')
        elif self.GPU == "gtx-130":
            return ('you can gameing with vwry low setting')
        else:
            return ("you can gameing with hing fps")

    def offer(self):
        off = (self.price//100)*self.discount
        return(self.price - off) 
        
    
l1 = Laptop('hp','4','500-GB','none','none',25000,'i3-4gen')
l1.discount = 5
l2 = Laptop('dell','4','1-TB','none','none',35000,'i5-8gen')
l2.discount = 2
l3 = Laptop('lenovo','4','1-TB','none','none',26000,'i3-4gen')
l3.discount = 0
l4 = Laptop('hp(gameing)','8','1-TB','none','gtx-130',45000,'i5-4gen')
l4.discount = 15
l5 = Laptop('dell(gameing)','8','1-TB','none','gtx-1050ti',55000,'i5-4gen')
l5.discount = 10
l6 = Laptop('lenovo(gameing)','8','none','500gb','gtx-1650',59000,'i5-4gen')
l6.discount = 5
l7 = Laptop('asus(gameing)','16','1-TB','256gb','gtx-2080',75000,'i7-4gen')
l7.discount = 20

print(speech('WELCOM TO LAPI.PY'))
print(speech(F'number of laptop is {Laptop.total}'))
def main_menu():
    temp = " "
    print(speech("for all laptops please select - 1"))
    print(speech("for gameing laptop please select - 2"))
    print(speech("for office laptop please select - 3"))
    return temp

print(main_menu())
number = int(input("select your opction : "))

def last():
    print(speech("back to the main menu please press - 0\n if you want to comfirm your oder please press - 1"))
    g = int(input("Enter : "))
    number = 1 
    if g == 0:
        # print(main_menu())
        return (select_laptop(number))
    else:
        return (speech('thank you have a good day'))



def select_laptop(num):
    temp = ""
    if number == 1:
        print(F"1->{l1.name}\n2->{l2.name}\n3->{l3.name}\n4->{l4.name}\n5->{l5.name}\n6->{l6.name}\n->{l7.name}")
        print(speech("please select your laptop number"))
        char = int(input("Enter your number : "))
        if char == 1:
            print(speech(f"your laptop specification - {l1.__dict__}"))
            print(speech(f"actual price rupees-{l1.price}\nwith discount price rupees-{l1.offer()}"))
            return last()

            
        
        elif char == 2:
            print(speech(f"your laptop specification - {l2.__dict__}"))
            print(speech(f"actual price rupees-{l2.price}\nwith discount price rupees-{l2.offer()}"))
            return last()

        elif char == 3:
            print(speech(f"your laptop specification - {l3.__dict__}"))
            print(speech(f"actual price rupees-{l3.price}\nwith discount price rupees-{l3.offer()}"))
            return last()

        elif char == 4:
            print(speech(f"your laptop specification - {l4.__dict__}"))
            print(speech(f"actual price rupees-{l4.price}\nwith discount price rupees-{l4.offer()}"))
            return last()

        elif char == 5:
            print(speech(f"your laptop specification - {l5.__dict__}"))
            print(speech(f"actual price rupees-{l5.price}\nwith discount price rupees-{l5.offer()}"))
            return last()

        elif char == 6:
            print(speech(f"your laptop specification - {l6.__dict__}"))
            print(speech(f"actual price rupees-{l6.price}\nwith discount price rupees-{l6.offer()}"))
            return last()

        elif char == 7:
            print(speech(f"your laptop specification - {l7.__dict__}"))
            print(speech(f"actual price rupees-{l7.price}\nwith discount price rupees-{l7.offer()}"))
            return last()

             
            
    elif number == 2:
        print(F'1->{l4.name}\n2->{l5.name}\n3->{l6.name}\n4->{l7.name}')
        print(speech("please select your laptop number"))
        c = int(input("Enter your number : "))
        if c == 1:
            print(speech(f"your laptop specification - {l4.__dict__}"))
            print(speech(f"actual price rupees-{l4.price}\nwith discount price rupees-{l4.offer()}"))
            return last()

        elif c == 2:
            print(speech(f"your laptop specification - {l5.__dict__}"))
            print(speech(f"actual price rupees-{l5.price}\nwith discount price rupees-{l5.offer()}"))
            return last()

        elif c == 3:
            print(speech(f"your laptop specification - {l6.__dict__}"))
            print(speech(f"actual price rupees-{l6.price}\nwith discount price rupees-{l6.offer()}"))
            return last()

        elif c == 4:
            print(speech(f"your laptop specification - {l7.__dict__}"))
            print(speech(f"actual price rupees-{l7.price}\nwith discount price rupees-{l7.offer()}"))
            return last()

    else:
        print(f'1->{l1.name}\n2->{l2.name}')
        print(speech("please select your laptop number"))
        char = int(input("Enter your number : "))
        if char == 1:
            print(speech(f"your laptop specification - {l1.__dict__}"))
            print(speech(f"actual price rupees-{l1.price}\nwith discount price rupees-{l1.offer()}"))
            return last()
        elif char == 2 :
            print(speech(f"your laptop specification - {l2.__dict__}"))
            print(speech(f"actual price rupees-{l2.price}\nwith discount price rupees-{l2.offer()}"))
            return last()
    return temp




print(select_laptop(number))
        