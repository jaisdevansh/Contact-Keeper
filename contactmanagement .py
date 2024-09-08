Contacts={}
while True:
    print('\nContacts APP BOOK')
    print('1.Create Contacts')
    print('2.View Contacts')
    print ('3.Update Contacts ')
    print('4.Delete Contacts')
    print('5.Search Contacts')
    print('6.Count Contacts')
    print('7.Exit')
    choice=input("Enter the choice =")
    if choice=='1':
        name=input("Enter the name contact =")
        if name in Contacts:
            print(f"Contacts is {name}is already in Contacts !")
        else:
            age=input("Enter the age")
            email=input("Enter the email")
            mobile=input("Enter the mobile number ")
            Contacts[name]={'age':int(age),'email':(email),'mobile':(mobile)}
            print(f"Contacts name{name}is successfully created ...")
    elif choice=='2':
        name=input("Enter  the  contact  name to view =")
        if name in Contacts:
            contact=Contacts[name]

            print(f"Name:{name}\n,Age:{age},\n E-mail :{email},\n Mobilenumber: {mobile}")
        else:
            print('...Contact not found...')

    elif choice =='3':
        name=input("Enter the name you want to update = ")
        if name in Contacts:
            age=input("Enter the Updated  age =")
            email=input("Enter the   Updated email =")
            mobile=input("Enter the   Updated mobile number = ")
            Contacts[name]={'age':int(age),'email':(email),'mobile':(mobile)}
            print(f"Conatct{name} successfully updated") 
        else:
            print("...Contact not found...")
    elif choice =='4':
        name=input("Enter the name you want to Delete =")
        if name in Contacts:
            del Contacts[name]
            print(f'Contact  {name} has been Deleted')
        else:
            print("...Conatct not found...") 
    elif choice=='5':
        search_name=input("Enter the Contact name ")
        found= False
        for name,contact in Contacts.items():
            if search_name.lower() in name.lower():
                print(f'found - Name{name},\nAge:{age},\nemail:{email},\nmobile number :{mobile}')
                found=True
            else:
                print("...Contact not Found...")

    elif  choice =='6':
        print(f'total number of contact in your Contact book is :{len(Contacts)}') 
    elif choice=='7':
        print("GOOD BYE....CLOSING THE PROGRAM ")
        break
    else:
        print("INVALID INPUT\nPLEASE! Enter  VALID INPUT")               