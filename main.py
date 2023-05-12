import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk, ImageDraw, ImageOps
import matplotlib

matplotlib.use('Agg')
root = tk.Tk()


class MainScreen:
    
    def signup_button(self, mainRoot):
        SignUpScreen(mainRoot, self.imagelogo)
      
    def login_button(self, mainRoot, username, password, userEntry, passEntry):
        database = self.getDatabase()
        login = False
        for i in range(0, len(database)):
            if username.lower() == database[i][4].lower() and password == database[i][9]:
                mainRoot.withdraw()
                login = True
                MenuScreen(self.imagelogo, database[i][0], mainRoot, userEntry, passEntry)
        if login == False:
            popup = tk.Toplevel(bg="white")
            popup.title("Error")
            label = tk.Label(popup, text="Invalid Login", bg="white", fg="red")
            label.pack(padx=10, pady=10)
            popup.after(5000, popup.destroy)

    def clearEntrys(userEntry, passEntry):
        userEntry.delete(0, tk.END)
        passEntry.delete(0, tk.END)

    def __init__(self, mainRoot):
        mainRoot.geometry("475x375")
        mainRoot.configure(bg="white")
        mainRoot.title("Georges")
        self.imagelogo = Image.open("fishysunak.jpg")
        self.imagelogo = self.imagelogo.resize((100, 100))
        self.imagelogo = ImageOps.expand(self.imagelogo, border=-20)
        self.photo = ImageTk.PhotoImage(self.imagelogo)
        self.labellogo = tk.Label(image=self.photo)
        self.labellogo.pack(side="top")
        self.homeLabel = tk.Label(mainRoot, text="Home", bg="white", font=('Helvetica', 15), fg="black")
        self.homeLabel.pack(side="top")
        self.userLabel = tk.Label(mainRoot, text="Username:", bg="white", font=('Helvetica', 15), fg="black")
        self.userLabel.pack(pady=15)
        self.username = tk.Entry(mainRoot, width=20, font=('Helvetica', 15), fg="white")
        self.username.pack(pady=5)
        self.PassLabel = tk.Label(mainRoot, text="Password:",bg="white", font=('Helvetica', 15), fg="black",pady=5)
        self.PassLabel.pack(pady=15)
        self.password = tk.Entry(mainRoot, width=20, font=('Helvetica', 15), fg="white", show="*")
        self.password.pack()
        self.loginButton = tk.Button(mainRoot, bg="white", text="Login", font=('Helvetica', 15), fg="black", command=lambda: self.login_button(mainRoot, self.username.get(), self.password.get(),self.username, self.password),width=5)
        self.loginButton.pack(side="left",padx=75)
        self.signUpButton = tk.Button(mainRoot, bg="white", text="Sign Up", font=('Helvetica', 15), fg="black", command=lambda: self.signup_button(mainRoot), width=5)
        self.signUpButton.pack(side="right",padx=75)
    def getDatabase(self):
        list = []
        with open("database.txt", "r") as f:
            eof = False
            while not eof:
                customerID = f.readline().strip()
                firstN = f.readline().strip()
                lastN = f.readline().strip()
                dob = f.readline().strip()
                userN = f.readline().strip()
                email = f.readline().strip()
                phoneN = f.readline().strip()
                address = f.readline().strip()
                postcode = f.readline().strip()
                passW = f.readline().strip()
                list.append([customerID, firstN, lastN, dob, userN, email, phoneN, address, postcode, passW])
                if customerID == "":
                 eof = True
            list.pop()
        return list

class SignUpScreen(MainScreen):      
  
    def UserObject(self, fNameVal, lNameVal, dobVal, userVal, emailVal, phoneVal, addressVal, postcodeVal, password1Val, password2Val, mainRoot):
        dobcheck1 = False
        dobcheck2 = False
        dobcheck3 = False
        usernameCheck = False
        emailCheck1 = False
        emailCheck2 = False
        postcodecheck = False
        presencecheck = False
        if fNameVal != "" and lNameVal != "" and dobVal != "" and userVal != "" and emailVal != "" and phoneVal != "" and addressVal != "" and postcodeVal != "" and password1Val != "" and password2Val != "":
            presencecheck = True
        if len(postcodeVal) == 7:
            if (postcodeVal[0].isalpha() == True and postcodeVal[1].isalpha()== True and postcodeVal[2].isnumeric() == True and postcodeVal[3].isnumeric() == True and postcodeVal[4] == " " and postcodeVal[5].isnumeric() == True and postcodeVal[6].isalpha() == True and postcodeVal[7].isalpha() == True and len(postcodeVal) == 8) or (postcodeVal[0].isalpha() == True and postcodeVal[1].isalpha()== True and  postcodeVal[2].isnumeric() == True and postcodeVal[3] == " " and postcodeVal[4].isnumeric() == True and postcodeVal[5].isalpha() == True and postcodeVal[6].isalpha() == True):  
                postcodecheck = True
            elif (postcodeVal[0].isalpha() == True and postcodeVal[1].isalpha() == True and postcodeVal[2].isnumeric() == True and postcodeVal[3].isnumeric() == True and postcodeVal[4].isnumeric() == True and postcodeVal[5].isalpha() == True and postcodeVal[6].isalpha() == True):
                postcodecheck = True
                postcodeVal = postcodeVal[0:4] + " "+ postcodeVal[4:7]
        elif len(postcodeVal) == 6:
            if (postcodeVal[0].isalpha() == True and postcodeVal[1].isalpha() == True and postcodeVal[2].isnumeric() == True and postcodeVal[3].isnumeric() == True and postcodeVal[4].isalpha() == True and postcodeVal[5].isalpha() == True):
                postcodecheck = True
                postcodeVal = postcodeVal[0:3] + " "+ postcodeVal[3:6]
        if len(dobVal) == 10:
            if dobVal[0].isnumeric() == True and dobVal[1].isnumeric() == True and dobVal[2] == "/" and dobVal[3].isnumeric() == True and dobVal[4].isnumeric() == True and dobVal[5] == "/" and dobVal[6].isnumeric() == True and dobVal[7].isnumeric() == True and dobVal[8].isnumeric() == True and dobVal[9].isnumeric() == True and len(dobVal) == 10 and int(dobVal[0:2]) < 32 and int(dobVal[3:5]) < 13:
                dobcheck1 = True
        if dobVal != "" and dobVal[6:10].isnumeric() == True:
            if int(dobVal[6:10]) < 2006:
                dobcheck2 = True
            if int(dobVal[6:10]) > 1923:
                dobcheck3 = True
        database = MainScreen.getDatabase(self)
        if "@" in emailVal:
            emailCheck1 = True
        if ".co.uk" in emailVal or ".com" in emailVal:
            emailCheck2 = True
        for i in range(0, len(database)):
            if userVal.lower() == database[i][3].lower():
                usernameCheck = True
        if password1Val == password2Val and usernameCheck == False and len(password1Val)>7 and phoneVal[0:2] == "07" and len(phoneVal) == 11 and phoneVal.isnumeric() == True and fNameVal.isalpha() == True and lNameVal.isalpha() == True and emailCheck1 == True and emailCheck2 == True and len(fNameVal) > 0 and len(lNameVal) > 0 and len(userVal) > 0 and len(emailVal) > 0 and len(phoneVal) > 0 and len(addressVal) > 0 and len(postcodeVal) > 0 and dobcheck1 == True and dobcheck2 == True and dobcheck3 == True and postcodecheck == True and presencecheck == True:
            if len(database) == 0:
                customerID = 1
            else:
                customerID = int((database[(len(database)-1)][0])[2:3]) + 1
            with open("database.txt", "a") as y:
                y.write("C-"+ str(customerID) + "\n")
                y.write(fNameVal + "\n")
                y.write(lNameVal + "\n")
                y.write(dobVal + "\n")
                y.write(userVal + "\n")
                y.write(emailVal + "\n")
                y.write(phoneVal + "\n")
                y.write(addressVal + "\n")
                y.write(postcodeVal + "\n")
                y.write(password1Val + "\n")
            popup = tk.Toplevel(bg="white")
            popup.title("Success!")
            label = tk.Label(popup, text="You've successfully created an account.", bg="white", fg="green")
            label.pack(padx=10, pady=10)
            popup.after(5000, popup.destroy)
            self.master.destroy()
            mainRoot.deiconify()
        elif presencecheck == False:
            print(1)
            popup = tk.Toplevel(bg="white")
            popup.title("Error")
            label = tk.Label(popup, text="Fill in all fields", bg="white", fg="red")
            label.pack(padx=10, pady=10)
            popup.after(5000, popup.destroy)
        elif  usernameCheck == True:
            popup = tk.Toplevel(bg="white")
            popup.title("Error")
            label = tk.Label(popup, text="Username already exists", bg="white", fg="red")
            label.pack(padx=10, pady=10)
            popup.after(5000, popup.destroy)
        elif  password1Val != password2Val:
            popup = tk.Toplevel(bg="white")
            popup.title("Error")
            label = tk.Label(popup, text="Passwords do not match.", bg="white", fg="red")
            label.pack(padx=10, pady=10)
            popup.after(5000, popup.destroy)
        elif  len(password1Val)<8:
            popup = tk.Toplevel(bg="white")
            popup.title("Error")
            label = tk.Label(popup, text="Invalid Password", bg="white", fg="red")
            label.pack(padx=10, pady=10)
            popup.after(5000, popup.destroy)
        elif  phoneVal.isnumeric() == False or len(phoneVal) != 11 or phoneVal[0:2] != "07":
            popup = tk.Toplevel(bg="white")
            popup.title("Error")
            label = tk.Label(popup, text="Phone number invalid", bg="white", fg="red")
            label.pack(padx=10, pady=10)
            popup.after(5000, popup.destroy)
        elif  fNameVal.isalpha() == False:
            popup = tk.Toplevel(bg="white")
            popup.title("Error")
            label = tk.Label(popup, text="Invalid First Name", bg="white", fg="red")
            label.pack(padx=10, pady=10)
            popup.after(5000, popup.destroy)
        elif lNameVal.isalpha() == False:
            popup = tk.Toplevel(bg="white")
            popup.title("Error")
            label = tk.Label(popup, text="Invalid Last Name", bg="white", fg="red")
            label.pack(padx=10, pady=10)
            popup.after(5000, popup.destroy)
        elif emailCheck1 == False or emailCheck2 == False:
            popup = tk.Toplevel(bg="white")
            popup.title("Error")
            label = tk.Label(popup, text="Invalid Email", bg="white", fg="red")
            label.pack(padx=10, pady=10)
            popup.after(5000, popup.destroy)
        elif  postcodecheck == False:
            popup = tk.Toplevel(bg="white")
            popup.title("Error")
            label = tk.Label(popup, text="Incorrect postcode", bg="white", fg="red")
            label.pack(padx=10, pady=10)
            popup.after(5000, popup.destroy)
        elif dobcheck1 == False:
            popup = tk.Toplevel(bg="white")
            popup.title("Error")
            label = tk.Label(popup, text="Incorrect date of birth format (dd/mm/yyyy)", bg="white", fg="red")
            label.pack(padx=10, pady=10)
            popup.after(5000, popup.destroy)
        elif dobcheck2 == False:
            popup = tk.Toplevel(bg="white")
            popup.title("Error")
            label = tk.Label(popup, text="Must be 18 or older to register", bg="white", fg="red")
            label.pack(padx=10, pady=10)
            popup.after(5000, popup.destroy)
        else:
            popup = tk.Toplevel(bg="white")
            popup.title("Error")
            label = tk.Label(popup, text="Incorrect age", bg="white", fg="red")
            label.pack(padx=10, pady=10)
            popup.after(5000, popup.destroy)
    def goBack(self, root):
      self.master.destroy()
      root.deiconify()
    def __init__(self, mainRoot, imagelogo):
        mainRoot.withdraw()
        self.master = tk.Toplevel()
        self.master.geometry("475x375")
        self.master.configure(bg="white")

        wrapper = tk.LabelFrame(self.master, bg="white")
        wrapper.pack(fill="both", expand="yes")
        myCanvas = tk.Canvas(wrapper, bg="white", height=600)
        myCanvas.pack(side=tk.LEFT, fill="both", expand="yes")
        
        yscrollbar = ttk.Scrollbar(wrapper, orient="vertical", command=myCanvas.yview)
        yscrollbar.pack(side=tk.RIGHT, fill="y")
      
        myframe = tk.Frame(myCanvas, bg="white")   
        myCanvas.configure(yscrollcommand=yscrollbar.set, bg="white")
        myCanvas.bind("<Configure>", lambda e: myCanvas.configure(scrollregion=myCanvas.bbox("all")))
      
        myCanvas.create_window((0,0), window=myframe, anchor="nw")
  
        self.imagelogo = imagelogo
        self.photo = ImageTk.PhotoImage(self.imagelogo)
        self.labellogo = tk.Label(myframe, image=self.photo)
        self.labellogo.image = self.photo
        self.labellogo.grid(row=0, column=1)
        self.label1 = tk.Label(myframe, text="Sign Up", bg="white", font=('Helvetica', 15), fg="black")
        self.label1.grid(row=0, column=0, padx=0)
        self.fNameLabel = tk.Label(myframe, text="First Name:",bg="white", font=('Helvetica', 15), fg="black").grid(row=1, column=0,columnspan=2, pady=5)
        self.fName = tk.Entry(myframe, width=20, font=('Helvetica', 15))
        self.fName.grid(row=2, column=0,columnspan=2, pady=5)
        self.lNameLabel = tk.Label(myframe, text="Last Name:",bg="white", font=('Helvetica', 15), fg="black").grid(row=3, column=0,columnspan=2, padx=175, pady=5)
        self.lName = tk.Entry(myframe, width=20, font=('Helvetica', 15))
        self.lName.grid(row=4, column=0,columnspan=2, pady=5)
        self.dobLabel = tk.Label(myframe, text="Date of Birth:",bg="white", font=('Helvetica', 15), fg="black").grid(row=5, column=0,columnspan=2, padx=175, pady=5)
        self.dob = tk.Entry(myframe, width=20, font=('Helvetica', 15))
        self.dob.grid(row=6, column=0,columnspan=2, pady=5)
        self.userLabel = tk.Label(myframe, text="Username:",bg="white", font=('Helvetica', 15), fg="black").grid(row=7, column=0,columnspan=2, padx=175, pady=5)
        self.user = tk.Entry(myframe, width=20, font=('Helvetica', 15))
        self.user.grid(row=8, column=0,columnspan=2, pady=5)
        self.emailLabel = tk.Label(myframe, text="Email:",bg="white", font=('Helvetica', 15), fg="black").grid(row=9, column=0,columnspan=2, pady=5)
        self.email = tk.Entry(myframe, width=20, font=('Helvetica', 15))
        self.email.grid(row=10, column=0,columnspan=2, pady=5)
        self.phoneLabel = tk.Label(myframe, text="Phone Number:",bg="white", font=('Helvetica', 15), fg="black").grid(row=11, column=0,columnspan=2, pady=5)
        self.phone = tk.Entry(myframe, width=20, font=('Helvetica', 15))
        self.phone.grid(row=12, column=0,columnspan=2, pady=5)
        self.addressLabel = tk.Label(myframe, text="Address:",bg="white", font=('Helvetica', 15), fg="black").grid(row=13, column=0,columnspan=2, pady=5)
        self.address = tk.Entry(myframe, width=20, font=('Helvetica', 15))
        self.address.grid(row=14, column=0,columnspan=2, pady=5)
        self.postcodeLabel = tk.Label(myframe, text="Postcode:",bg="white", font=('Helvetica', 15), fg="black").grid(row=15, column=0,columnspan=2, pady=5)
        self.postcode = tk.Entry(myframe, width=20, font=('Helvetica', 15))
        self.postcode.grid(row=16, column=0,columnspan=2, pady=5)
        self.passwordLabel1 = tk.Label(myframe, text="Password:",bg="white", font=('Helvetica', 15), fg="black").grid(row=17, column=0,columnspan=2, pady=5)
        self.password1 = tk.Entry(myframe, width=20, font=('Helvetica', 15), show="*")
        self.password1.grid(row=18, column=0,columnspan=2, pady=5)
        self.passwordLabel2 = tk.Label(myframe, text="Confirm Password:",bg="white", font=('Helvetica', 15), fg="black").grid(row=19, column=0,columnspan=2, pady=5)
        self.password2 = tk.Entry(myframe, width=20, font=('Helvetica', 15), show="*")
        self.password2.grid(row=20, column=0,columnspan=2, pady=5)
        self.signUpButton = tk.Button(myframe, bg="white", text="Sign Up", font=('Helvetica', 15), width=5, command=lambda: SignUpScreen.UserObject(self, self.fName.get(), self.lName.get(),self.dob.get(), self.user.get(), self.email.get(), self.phone.get(), self.address.get(), self.postcode.get(), self.password1.get(), self.password2.get(), mainRoot))
        self.signUpButton.grid(row=21, column=0, columnspan=2, pady=5)
        self.image2 = Image.open("backarrow.png")
        self.image2 = self.image2.resize((30, 30))
        self.photo2 = ImageTk.PhotoImage(self.image2)
        self.backButton = tk.Button(myframe, image=self.photo2, bg="white", command=lambda: self.goBack(root))
        self.backButton.grid(row=21,column=0,pady=5)
        self.backButton.image = self.photo2
      
class MenuScreen():
    def addToBasket(self, itemref, fncCount, burgerCount, ribsCount, sweetnsourCount, wontonCount, hoisinCount, prawnCount, riceCount, noodleCount, chipCount, pmaxCount, fantaCount, spriteCount, pepperCount):
        if itemref == 0 and self.fncCount < 9:
            self.fncCount += 1
            self.fncnumber.config(text=self.fncCount)
        elif itemref == 1 and self.burgerCount < 9:
            self.burgerCount += 1
            self.burgernumber.config(text=self.burgerCount)
        elif itemref == 2 and self.ribsCount < 9:
            self.ribsCount += 1
            self.ribsnumber.config(text=self.ribsCount)
        elif itemref == 3 and self.sweetnsourCount < 9:
            self.sweetnsourCount += 1
            self.sweetnsournumber.config(text=self.sweetnsourCount)
        elif itemref == 4 and self.wontonCount < 9:
            self.wontonCount += 1
            self.wontonnumber.config(text=self.wontonCount)
        elif itemref == 5 and self.hoisinCount < 9:
            self.hoisinCount += 1
            self.hoisinnumber.config(text=self.hoisinCount)
        elif itemref == 6 and self.prawnCount < 9:
            self.prawnCount += 1
            self.prawnnumber.config(text=self.prawnCount)
        elif itemref == 7 and self.riceCount < 9:
            self.riceCount += 1
            self.ricenumber.config(text=self.riceCount)
        elif itemref == 8 and self.noodleCount < 9:
            self.noodleCount += 1
            self.noodlenumber.config(text=self.noodleCount)
        elif itemref == 9 and self.chipCount < 9:
            self.chipCount += 1
            self.chipnumber.config(text=self.chipCount)
        elif itemref == 10 and self.pmaxCount < 9:
            self.pmaxCount += 1
            self.pmaxnumber.config(text=self.pmaxCount)
        elif itemref == 11 and self.fantaCount < 9:
            self.fantaCount += 1
            self.fantanumber.config(text=self.fantaCount)
        elif itemref == 12 and self.spriteCount < 9:
            self.spriteCount += 1
            self.spritenumber.config(text=self.spriteCount)
        elif itemref == 13 and self.pepperCount < 9:
            self.pepperCount += 1
            self.peppernumber.config(text=self.pepperCount)
        else:
            popup = tk.Toplevel(bg="white")
            popup.title("Error!")
            label = tk.Label(popup, text="You have added the max of that particular item.", bg="white", fg="red")
            label.pack(padx=10, pady=10)
            popup.after(5000, popup.destroy)
        self.basket = [self.fncCount, self.burgerCount, self.ribsCount, self.sweetnsourCount, self.wontonCount, self.hoisinCount, self.prawnCount, self.riceCount, self.noodleCount, self.chipCount, self.pmaxCount, self.fantaCount, self.spriteCount, self.pepperCount]
        return self.basket

    def removeFromBasket(self, itemref, fncCount, burgerCount, ribsCount, sweetnsourCount, wontonCount, hoisinCount, prawnCount, riceCount, noodleCount, chipCount, pmaxCount, fantaCount, spriteCount, pepperCount):
        if itemref == 0 and self.fncCount > 0:
            self.fncCount -= 1
            self.fncnumber.config(text=self.fncCount)
        elif itemref == 1 and self.burgerCount > 0:
            self.burgerCount -= 1
            self.burgernumber.config(text=self.burgerCount)
        elif itemref == 2 and self.ribsCount > 0:
            self.ribsCount -= 1
            self.ribsnumber.config(text=self.ribsCount)
        elif itemref == 3 and self.sweetnsourCount > 0:
            self.sweetnsourCount -= 1
            self.sweetnsournumber.config(text=self.sweetnsourCount)
        elif itemref == 4 and self.wontonCount > 0:
            self.wontonCount -= 1
            self.wontonnumber.config(text=self.wontonCount)
        elif itemref == 5 and self.hoisinCount > 0:
            self.hoisinCount -= 1
            self.hoisinnumber.config(text=self.hoisinCount)
        elif itemref == 6 and self.prawnCount > 0:
            self.prawnCount -= 1
            self.prawnnumber.config(text=self.prawnCount)
        elif itemref == 7 and self.riceCount > 0:
            self.riceCount -= 1
            self.ricenumber.config(text=self.riceCount)
        elif itemref == 8 and self.noodleCount > 0:
            self.noodleCount -= 1
            self.noodlenumber.config(text=self.noodleCount)
        elif itemref == 9 and self.chipCount > 0:
            self.chipCount -= 1
            self.chipnumber.config(text=self.chipCount)
        elif itemref == 10 and self.pmaxCount > 0:
            self.pmaxCount -= 1
            self.pmaxnumber.config(text=self.pmaxCount)
        elif itemref == 11 and self.fantaCount > 0:
            self.fantaCount -= 1
            self.fantanumber.config(text=self.fantaCount)
        elif itemref == 12 and self.spriteCount > 0:
            self.spriteCount -= 1
            self.spritenumber.config(text=self.spriteCount)
        elif itemref == 13 and self.pepperCount > 0:
            self.pepperCount -= 1
            self.peppernumber.config(text=self.pepperCount)
        else:
            popup = tk.Toplevel(bg="white")
            popup.title("Error!")
            label = tk.Label(popup, text="You can't have less than zero of a particular item.", bg="white", fg="red")
            label.pack(padx=10, pady=10)
            popup.after(5000, popup.destroy)
        self.basket = [self.fncCount, self.burgerCount,   self.ribsCount, self.sweetnsourCount, self.wontonCount, self.hoisinCount, self.prawnCount, self.riceCount, self.noodleCount, self.chipCount, self.pmaxCount, self.fantaCount, self.spriteCount, self.pepperCount]
        return self.basket
    def goBack(self, myframe, mainRoot, userEntry, passEntry):
        mainRoot.deiconify()
        MainScreen.clearEntrys(userEntry, passEntry)
        myframe.destroy()
        
    def __init__(self, imagelogo, customerID, mainRoot, userEntry, passEntry):
        master = tk.Toplevel()
        master.geometry("475x375")
        master.configure(bg="white")   
        wrapper = tk.LabelFrame(master, bg="white")
        wrapper.pack(fill="both", expand="yes")
        myCanvas = tk.Canvas(wrapper, bg="white", height=600)
        myCanvas.pack(side=tk.LEFT, fill="both", expand="yes")
        self.basket = [0] * 14
        yscrollbar = ttk.Scrollbar(wrapper, orient="vertical", command=myCanvas.yview)
        yscrollbar.pack(side=tk.RIGHT, fill="y")
      
        myframe = tk.Frame(myCanvas, bg="white")   
        myCanvas.configure(yscrollcommand=yscrollbar.set, bg="white")
        myCanvas.bind("<Configure>", lambda e: myCanvas.configure(scrollregion=myCanvas.bbox("all")))
      
        myCanvas.create_window((0,0), window=myframe, anchor="nw")
        self.fncCount = 0
        self.burgerCount = 0
        self.ribsCount = 0
        self.sweetnsourCount = 0
        self.wontonCount = 0
        self.hoisinCount = 0
        self.prawnCount = 0
        self.riceCount = 0
        self.noodleCount = 0
        self.chipCount = 0
        self.pmaxCount = 0
        self.fantaCount = 0
        self.spriteCount = 0
        self.pepperCount = 0
      
        self.imagelogo = Image.open("fishysunak.jpg")
        self.imagelogo = self.imagelogo.resize((100, 100))
        self.imagelogo = ImageOps.expand(self.imagelogo, border=-20)
        self.photo = ImageTk.PhotoImage(self.imagelogo)
        self.labellogo = tk.Label(myframe, image=self.photo)
        self.labellogo.image = self.photo
        self.labellogo.grid(row=0, column=7)

        myCanvas.create_window((0,0), window=myframe, anchor="nw")
        self.menu = tk.Label(myframe, text="Menu", bg="white", font=('Helvetica', 15))
        self.menu.grid(row=0, column=0,columnspan=2, padx=0,pady=5)
        self.formatlabel = tk.Label(myframe, text="Mains", bg="white", font=('Helvetica', 15)).grid(row=1,column=7, pady=20)
        self.fnclabel = tk.Label(myframe, text="Fish & Chips", bg="white", font=('Helvetica', 15))
        self.fnclabel.grid(row=2, column=3, columnspan=4)
        self.fishandchips = Image.open('fishandchips.png')
        self.fishandchips = self.fishandchips.resize((142, 142), resample=Image.BILINEAR)
        self.photo2 = ImageTk.PhotoImage(self.fishandchips)
        self.label2 = tk.Label(myframe, image=self.photo2)
        self.label2.fishandchips = self.photo2
        self.label2.grid(row=3,column=3,columnspan=4)
        self.fncnegative = tk.Button(myframe, text="-", bg="white", font=('Helvetica', 10), fg="black", command=lambda: MenuScreen.removeFromBasket(self, 0, self.fncCount, self.burgerCount, self.ribsCount, self.sweetnsourCount, self.wontonCount, self.hoisinCount, self.prawnCount, self.riceCount, self.noodleCount, self.chipCount, self.pmaxCount, self.fantaCount, self.spriteCount, self.pepperCount))
        self.fncnegative.grid(row=4, column=3)
        self.fncnumber = tk.Label(myframe, text="0", bg="white", font=('Helvetica', 10), fg="black", relief="raised",padx=6,pady=5)
        self.fncnumber.grid(row=4, column=4)
        self.fncprice = tk.Label(myframe, text="£8.99", bg="white", font=('Helvetica', 10), fg="black", relief="raised",padx=6,pady=5)
        self.fncprice.grid(row=4, column=5)
        self.fncpositive = tk.Button(myframe, text="+", bg="white", font=('Helvetica', 10), fg="black", command=lambda: MenuScreen.addToBasket(self, 0, self.fncCount, self.burgerCount, self.ribsCount, self.sweetnsourCount, self.wontonCount, self.hoisinCount, self.prawnCount, self.riceCount, self.noodleCount, self.chipCount, self.pmaxCount, self.fantaCount, self.spriteCount, self.pepperCount))
        self.fncpositive.grid(row=4, column=6)
      
        self.burgerlabel = tk.Label(myframe, text="Burger", bg="white", font=('Helvetica', 15))
        self.burgerlabel.grid(row=2, column=8, columnspan=4)
        self.burger = Image.open('burger.png')
        self.burger = self.burger.resize((142, 142), resample=Image.BILINEAR)
        self.photo3 = ImageTk.PhotoImage(self.burger)
        self.label3 = tk.Label(myframe, image=self.photo3)
        self.label3.burger = self.photo3
        self.label3.grid(row=3,column=8,columnspan=4)
        self.burgernegative = tk.Button(myframe, text="-", bg="white", font=('Helvetica', 10), fg="black", command=lambda: MenuScreen.removeFromBasket(self, 1, self.fncCount, self.burgerCount, self.ribsCount, self.sweetnsourCount, self.wontonCount, self.hoisinCount, self.prawnCount, self.riceCount, self.noodleCount, self.chipCount, self.pmaxCount, self.fantaCount, self.spriteCount, self.pepperCount))
        self.burgernegative.grid(row=4, column=8)
        self.burgernumber = tk.Label(myframe, text="0", bg="white", font=('Helvetica', 10), fg="black", relief="raised",padx=6,pady=5)
        self.burgernumber.grid(row=4, column=9)
        self.burgerprice = tk.Label(myframe, text="£7.99", bg="white", font=('Helvetica', 10), fg="black", relief="raised",padx=6,pady=5)
        self.burgerprice.grid(row=4, column=10)
        self.burgerpositive = tk.Button(myframe, text="+", bg="white", font=('Helvetica', 10), fg="black", command=lambda: MenuScreen.addToBasket(self, 1, self.fncCount, self.burgerCount, self.ribsCount, self.sweetnsourCount, self.wontonCount, self.hoisinCount, self.prawnCount, self.riceCount, self.noodleCount, self.chipCount, self.pmaxCount, self.fantaCount, self.spriteCount, self.pepperCount))
        self.burgerpositive.grid(row=4, column=11)
        self.formatlabel2 = tk.Label(myframe, text="", bg="white", font=('Helvetica', 15), fg="black").grid(row=5)

        self.ribslabel = tk.Label(myframe, text="Ribs", bg="white", font=('Helvetica', 15), fg="black")
        self.ribslabel.grid(row=6, column=3, columnspan=4)
        self.ribs = Image.open('ribs.png')
        self.ribs = self.ribs.resize((142, 142), resample=Image.BILINEAR)
        self.photo4 = ImageTk.PhotoImage(self.ribs)
        self.label4 = tk.Label(myframe, image=self.photo4)
        self.label4.ribs = self.photo4
        self.label4.grid(row=7,column=3,columnspan=4)
        self.ribsnegative = tk.Button(myframe, text="-", bg="white", font=('Helvetica', 10), fg="black", command=lambda: MenuScreen.removeFromBasket(self, 2, self.fncCount, self.burgerCount, self.ribsCount, self.sweetnsourCount, self.wontonCount, self.hoisinCount, self.prawnCount, self.riceCount, self.noodleCount, self.chipCount, self.pmaxCount, self.fantaCount, self.spriteCount, self.pepperCount))
        self.ribsnegative.grid(row=8, column=3)
        self.ribsnumber = tk.Label(myframe, text="0", bg="white", font=('Helvetica', 10), fg="black", relief="raised",padx=6,pady=5)
        self.ribsnumber.grid(row=8, column=4)
        self.ribsprice = tk.Label(myframe, text="£9.99", bg="white", font=('Helvetica', 10), fg="black", relief="raised",padx=6,pady=5)
        self.ribsprice.grid(row=8, column=5)
        self.ribspositive = tk.Button(myframe, text="+", bg="white", font=('Helvetica', 10), fg="black", command=lambda: MenuScreen.addToBasket(self, 2, self.fncCount, self.burgerCount, self.ribsCount, self.sweetnsourCount, self.wontonCount, self.hoisinCount, self.prawnCount, self.riceCount, self.noodleCount, self.chipCount, self.pmaxCount, self.fantaCount, self.spriteCount, self.pepperCount))
        self.ribspositive.grid(row=8, column=6)
        
        self.sweetnsourlabel = tk.Label(myframe, text="Sweet & Sour", bg="white", font=('Helvetica', 15))
        self.sweetnsourlabel.grid(row=6, column=8, columnspan=4)
        self.sweetnsour = Image.open('sweetnsour.png')
        self.sweetnsour = self.sweetnsour.resize((142, 142), resample=Image.BILINEAR)
        self.photo5 = ImageTk.PhotoImage(self.sweetnsour)
        self.label5 = tk.Label(myframe, image=self.photo5)
        self.label5.sweetnsour = self.photo5
        self.label5.grid(row=7,column=8,columnspan=4)
        self.sweetnsournegative = tk.Button(myframe, text="-", bg="white", font=('Helvetica', 10), fg="black", command=lambda: MenuScreen.removeFromBasket(self, 3, self.fncCount, self.burgerCount, self.ribsCount, self.sweetnsourCount, self.wontonCount, self.hoisinCount, self.prawnCount, self.riceCount, self.noodleCount, self.chipCount, self.pmaxCount, self.fantaCount, self.spriteCount, self.pepperCount))
        self.sweetnsournegative.grid(row=8, column=8)
        self.sweetnsournumber = tk.Label(myframe, text="0", bg="white", font=('Helvetica', 10), fg="black", relief="raised",padx=6,pady=5)
        self.sweetnsournumber.grid(row=8, column=9)
        self.sweetnsourprice = tk.Label(myframe, text="£6.99", bg="white", font=('Helvetica', 10), fg="black", relief="raised",padx=6,pady=5)
        self.sweetnsourprice.grid(row=8, column=10)
        self.sweetnsourpositive = tk.Button(myframe, text="+", bg="white", font=('Helvetica', 10), fg="black", command=lambda: MenuScreen.addToBasket(self, 3, self.fncCount, self.burgerCount, self.ribsCount, self.sweetnsourCount, self.wontonCount, self.hoisinCount, self.prawnCount, self.riceCount, self.noodleCount, self.chipCount, self.pmaxCount, self.fantaCount, self.spriteCount, self.pepperCount))
        self.sweetnsourpositive.grid(row=8, column=11)
        self.formatlabel2 = tk.Label(myframe, text="", bg="white", font=('Helvetica', 15), fg="black").grid(row=9)

        self.wontonlabel = tk.Label(myframe, text="Wonton Soup", bg="white", font=('Helvetica', 15), fg="black")
        self.wontonlabel.grid(row=10, column=3, columnspan=4)
        self.wonton = Image.open('wontonsoup.png')
        self.wonton = self.wonton.resize((142, 142), resample=Image.BILINEAR)
        self.photo6 = ImageTk.PhotoImage(self.wonton)
        self.label6 = tk.Label(myframe, image=self.photo6)
        self.label6.wonton = self.photo6
        self.label6.grid(row=11,column=3,columnspan=4)
        self.wontonnegative = tk.Button(myframe, text="-", bg="white", font=('Helvetica', 10), fg="black", command=lambda: MenuScreen.removeFromBasket(self, 4, self.fncCount, self.burgerCount, self.ribsCount, self.sweetnsourCount, self.wontonCount, self.hoisinCount, self.prawnCount, self.riceCount, self.noodleCount, self.chipCount, self.pmaxCount, self.fantaCount, self.spriteCount, self.pepperCount))
        self.wontonnegative.grid(row=12, column=3)
        self.wontonnumber = tk.Label(myframe, text="0", bg="white", font=('Helvetica', 10), fg="black", relief="raised",padx=6,pady=5)
        self.wontonnumber.grid(row=12, column=4)
        self.wontonprice = tk.Label(myframe, text="£4.99", bg="white", font=('Helvetica', 10), fg="black", relief="raised",padx=6,pady=5)
        self.wontonprice.grid(row=12, column=5)
        self.wontonpositive = tk.Button(myframe, text="+", bg="white", font=('Helvetica', 10), fg="black", command=lambda: MenuScreen.addToBasket(self, 4, self.fncCount, self.burgerCount, self.ribsCount, self.sweetnsourCount, self.wontonCount, self.hoisinCount, self.prawnCount, self.riceCount, self.noodleCount, self.chipCount, self.pmaxCount, self.fantaCount, self.spriteCount, self.pepperCount))
        self.wontonpositive.grid(row=12, column=6)

        self.hoisinlabel = tk.Label(myframe, text="Hoisin Wings", bg="white", font=('Helvetica', 15), fg="black")
        self.hoisinlabel.grid(row=10, column=8, columnspan=4)
        self.hoisin = Image.open('hoisin.png')
        self.hoisin = self.hoisin.resize((142, 142), resample=Image.BILINEAR)
        self.photo7 = ImageTk.PhotoImage(self.hoisin)
        self.label7 = tk.Label(myframe, image=self.photo7)
        self.label7.wonton = self.photo7
        self.label7.grid(row=11,column=8,columnspan=4)
        self.hoisinnegative = tk.Button(myframe, text="-", bg="white", font=('Helvetica', 10), fg="black", command=lambda: MenuScreen.removeFromBasket(self, 5, self.fncCount, self.burgerCount, self.ribsCount, self.sweetnsourCount, self.wontonCount, self.hoisinCount, self.prawnCount, self.riceCount, self.noodleCount, self.chipCount, self.pmaxCount, self.fantaCount, self.spriteCount, self.pepperCount))
        self.hoisinnegative.grid(row=12, column=8)
        self.hoisinnumber = tk.Label(myframe, text="0", bg="white", font=('Helvetica', 10), fg="black", relief="raised",padx=6,pady=5)
        self.hoisinnumber.grid(row=12, column=9)
        self.hoisinprice = tk.Label(myframe, text="£7.99", bg="white", font=('Helvetica', 10), fg="black", relief="raised",padx=6,pady=5)
        self.hoisinprice.grid(row=12, column=10)
        self.hoisinpositive = tk.Button(myframe, text="+", bg="white", font=('Helvetica', 10), fg="black", command=lambda: MenuScreen.addToBasket(self, 5, self.fncCount, self.burgerCount, self.ribsCount, self.sweetnsourCount, self.wontonCount, self.hoisinCount, self.prawnCount, self.riceCount, self.noodleCount, self.chipCount, self.pmaxCount, self.fantaCount, self.spriteCount, self.pepperCount))
        self.hoisinpositive.grid(row=12, column=11)
        self.formatlabel3 = tk.Label(myframe, text="Sides", bg="white", font=('Helvetica', 15), fg="black").grid(row=13,column=7, pady=20)

        self.prawnlabel = tk.Label(myframe, text="Prawn Toast", bg="white", font=('Helvetica', 15), fg="black")
        self.prawnlabel.grid(row=14, column=3, columnspan=4)
        self.prawn = Image.open('prawn.png')
        self.prawn = self.prawn.resize((142, 142), resample=Image.BILINEAR)
        self.photo8 = ImageTk.PhotoImage(self.prawn)
        self.label8 = tk.Label(myframe, image=self.photo8)
        self.label8.prawn = self.photo8
        self.label8.grid(row=15,column=3,columnspan=4)
        self.prawnnegative = tk.Button(myframe, text="-", bg="white", font=('Helvetica', 10), fg="black", command=lambda: MenuScreen.removeFromBasket(self, 6, self.fncCount, self.burgerCount, self.ribsCount, self.sweetnsourCount, self.wontonCount, self.hoisinCount, self.prawnCount, self.riceCount, self.noodleCount, self.chipCount, self.pmaxCount, self.fantaCount, self.spriteCount, self.pepperCount))
        self.prawnnegative.grid(row=16, column=3)
        self.prawnnumber = tk.Label(myframe, text="0", bg="white", font=('Helvetica', 10), fg="black", relief="raised",padx=6,pady=5)
        self.prawnnumber.grid(row=16, column=4)
        self.prawnprice = tk.Label(myframe, text="£4.99", bg="white", font=('Helvetica', 10), fg="black", relief="raised",padx=6,pady=5)
        self.prawnprice.grid(row=16, column=5)
        self.prawnpositive = tk.Button(myframe, text="+", bg="white", font=('Helvetica', 10), fg="black", command=lambda: MenuScreen.addToBasket(self, 6, self.fncCount, self.burgerCount, self.ribsCount, self.sweetnsourCount, self.wontonCount, self.hoisinCount, self.prawnCount, self.riceCount, self.noodleCount, self.chipCount, self.pmaxCount, self.fantaCount, self.spriteCount, self.pepperCount))
        self.prawnpositive.grid(row=16, column=6)

        self.ricelabel = tk.Label(myframe, text="Rice", bg="white", font=('Helvetica', 15), fg="black")
        self.ricelabel.grid(row=14, column=8, columnspan=4)
        self.rice = Image.open('rice.png')
        self.rice = self.rice.resize((142, 142), resample=Image.BILINEAR)
        self.photo9 = ImageTk.PhotoImage(self.rice)
        self.label9 = tk.Label(myframe, image=self.photo9)
        self.label9.rice = self.photo9
        self.label9.grid(row=15,column=8,columnspan=4)
        self.ricenegative = tk.Button(myframe, text="-", bg="white", font=('Helvetica', 10), fg="black", command=lambda: MenuScreen.removeFromBasket(self, 7, self.fncCount, self.burgerCount, self.ribsCount, self.sweetnsourCount, self.wontonCount, self.hoisinCount, self.prawnCount, self.riceCount, self.noodleCount, self.chipCount, self.pmaxCount, self.fantaCount, self.spriteCount, self.pepperCount))
        self.ricenegative.grid(row=16, column=8)
        self.ricenumber = tk.Label(myframe, text="0", bg="white", font=('Helvetica', 10), fg="black", relief="raised",padx=6,pady=5)
        self.ricenumber.grid(row=16, column=9)
        self.riceprice = tk.Label(myframe, text="£1.99", bg="white", font=('Helvetica', 10), fg="black", relief="raised",padx=6,pady=5)
        self.riceprice.grid(row=16, column=10)
        self.ricepositive = tk.Button(myframe, text="+", bg="white", font=('Helvetica', 10), fg="black", command=lambda: MenuScreen.addToBasket(self, 7, self.fncCount, self.burgerCount, self.ribsCount, self.sweetnsourCount, self.wontonCount, self.hoisinCount, self.prawnCount, self.riceCount, self.noodleCount, self.chipCount, self.pmaxCount, self.fantaCount, self.spriteCount, self.pepperCount))
        self.ricepositive.grid(row=16, column=11)
        self.formatlabel4 = tk.Label(myframe, text="", bg="white", font=('Helvetica', 15), fg="black").grid(row=17)

        self.noodlelabel = tk.Label(myframe, text="Noodles", bg="white", font=('Helvetica', 15), fg="black")
        self.noodlelabel.grid(row=18, column=3, columnspan=4)
        self.noodle = Image.open('noodle.png')
        self.noodle = self.noodle.resize((142, 142), resample=Image.BILINEAR)
        self.photo10 = ImageTk.PhotoImage(self.noodle)
        self.label10 = tk.Label(myframe, image=self.photo10)
        self.label10.noodle = self.photo10
        self.label10.grid(row=19,column=3,columnspan=4)
        self.noodlenegative = tk.Button(myframe, text="-", bg="white", font=('Helvetica', 10), fg="black", command=lambda: MenuScreen.removeFromBasket(self, 8, self.fncCount, self.burgerCount, self.ribsCount, self.sweetnsourCount, self.wontonCount, self.hoisinCount, self.prawnCount, self.riceCount, self.noodleCount, self.chipCount, self.pmaxCount, self.fantaCount, self.spriteCount, self.pepperCount))
        self.noodlenegative.grid(row=20, column=3)
        self.noodlenumber = tk.Label(myframe, text="0", bg="white", font=('Helvetica', 10), fg="black", relief="raised",padx=6,pady=5)
        self.noodlenumber.grid(row=20, column=4)
        self.noodleprice = tk.Label(myframe, text="£4.99", bg="white", font=('Helvetica', 10), fg="black", relief="raised",padx=6,pady=5)
        self.noodleprice.grid(row=20, column=5)
        self.noodlepositive = tk.Button(myframe, text="+", bg="white", font=('Helvetica', 10), fg="black", command=lambda: MenuScreen.addToBasket(self, 8, self.fncCount, self.burgerCount, self.ribsCount, self.sweetnsourCount, self.wontonCount, self.hoisinCount, self.prawnCount, self.riceCount, self.noodleCount, self.chipCount, self.pmaxCount, self.fantaCount, self.spriteCount, self.pepperCount))
        self.noodlepositive.grid(row=20, column=6)

        self.chiplabel = tk.Label(myframe, text="Chips", bg="white", font=('Helvetica', 15))
        self.chiplabel.grid(row=18, column=8, columnspan=4)
        self.chip = Image.open('chips.png')
        self.chip = self.chip.resize((142, 142), resample=Image.BILINEAR)
        self.photo11 = ImageTk.PhotoImage(self.chip)
        self.label11 = tk.Label(myframe, image=self.photo11)
        self.label11.chip = self.photo11
        self.label11.grid(row=19,column=8,columnspan=4)
        self.chipnegative = tk.Button(myframe, text="-", bg="white", font=('Helvetica', 10), fg="black", command=lambda: MenuScreen.removeFromBasket(self, 9, self.fncCount, self.burgerCount, self.ribsCount, self.sweetnsourCount, self.wontonCount, self.hoisinCount, self.prawnCount, self.riceCount, self.noodleCount, self.chipCount, self.pmaxCount, self.fantaCount, self.spriteCount, self.pepperCount))
        self.chipnegative.grid(row=20, column=8)
        self.chipnumber = tk.Label(myframe, text="0", bg="white", font=('Helvetica', 10), fg="black", relief="raised",padx=6,pady=5)
        self.chipnumber.grid(row=20, column=9)
        self.chipprice = tk.Label(myframe, text="£3.99", bg="white", font=('Helvetica', 10), fg="black", relief="raised",padx=6,pady=5)
        self.chipprice.grid(row=20, column=10)
        self.chippositive = tk.Button(myframe, text="+", bg="white", font=('Helvetica', 10), fg="black", command=lambda: MenuScreen.addToBasket(self, 9, self.fncCount, self.burgerCount, self.ribsCount, self.sweetnsourCount, self.wontonCount, self.hoisinCount, self.prawnCount, self.riceCount, self.noodleCount, self.chipCount, self.pmaxCount, self.fantaCount, self.spriteCount, self.pepperCount))
        self.chippositive.grid(row=20, column=11)
        self.formatlabel3 = tk.Label(myframe, text="Drinks", bg="white", font=('Helvetica', 15), fg="black").grid(row=21,column=7, pady=20)
      
        self.pmaxlabel = tk.Label(myframe, text="Pepsi Max", bg="white", font=('Helvetica', 15), fg="black")
        self.pmaxlabel.grid(row=22, column=3, columnspan=4)
        self.pmax = Image.open('pmax.png')
        self.pmax = self.pmax.resize((142, 142), resample=Image.BILINEAR)
        self.photo12 = ImageTk.PhotoImage(self.pmax)
        self.label12 = tk.Label(myframe, image=self.photo12)
        self.label12.pmax = self.photo12
        self.label12.grid(row=23,column=3,columnspan=4)
        self.pmaxnegative = tk.Button(myframe, text="-", bg="white", font=('Helvetica', 10), fg="black", command=lambda: MenuScreen.removeFromBasket(self, 10, self.fncCount, self.burgerCount, self.ribsCount, self.sweetnsourCount, self.wontonCount, self.hoisinCount, self.prawnCount, self.riceCount, self.noodleCount, self.chipCount, self.pmaxCount, self.fantaCount, self.spriteCount, self.pepperCount))
        self.pmaxnegative.grid(row=24, column=3)
        self.pmaxnumber = tk.Label(myframe, text="0", bg="white", font=('Helvetica', 10), fg="black", relief="raised",padx=6,pady=5)
        self.pmaxnumber.grid(row=24, column=4)
        self.pmaxprice = tk.Label(myframe, text="£0.99", bg="white", font=('Helvetica', 10), fg="black", relief="raised",padx=6,pady=5)
        self.pmaxprice.grid(row=24, column=5)
        self.pmaxpositive = tk.Button(myframe, text="+", bg="white", font=('Helvetica', 10), fg="black", command=lambda: MenuScreen.addToBasket(self, 10, self.fncCount, self.burgerCount, self.ribsCount, self.sweetnsourCount, self.wontonCount, self.hoisinCount, self.prawnCount, self.riceCount, self.noodleCount, self.chipCount, self.pmaxCount, self.fantaCount, self.spriteCount, self.pepperCount))
        self.pmaxpositive.grid(row=24, column=6)

        self.fantalabel = tk.Label(myframe, text="Fanta", bg="white", font=('Helvetica', 15))
        self.fantalabel.grid(row=22, column=8, columnspan=4)
        self.fanta = Image.open('fanta.png')
        self.fanta = self.fanta.resize((142, 142), resample=Image.BILINEAR)
        self.photo13 = ImageTk.PhotoImage(self.fanta)
        self.label13 = tk.Label(myframe, image=self.photo13)
        self.label13.fanta = self.photo13
        self.label13.grid(row=23,column=8,columnspan=4)
        self.fantanegative = tk.Button(myframe, text="-", bg="white", font=('Helvetica', 10), fg="black", command=lambda: MenuScreen.removeFromBasket(self, 11, self.fncCount, self.burgerCount, self.ribsCount, self.sweetnsourCount, self.wontonCount, self.hoisinCount, self.prawnCount, self.riceCount, self.noodleCount, self.chipCount, self.pmaxCount, self.fantaCount, self.spriteCount, self.pepperCount))
        self.fantanegative.grid(row=24, column=8)
        self.fantanumber = tk.Label(myframe, text="0", bg="white", font=('Helvetica', 10), fg="black", relief="raised",padx=6,pady=5)
        self.fantanumber.grid(row=24, column=9)
        self.fantaprice = tk.Label(myframe, text="£0.99", bg="white", font=('Helvetica', 10), fg="black", relief="raised",padx=6,pady=5)
        self.fantaprice.grid(row=24, column=10)
        self.fantapositive = tk.Button(myframe, text="+", bg="white", font=('Helvetica', 10), fg="black", command=lambda: MenuScreen.addToBasket(self, 11, self.fncCount, self.burgerCount, self.ribsCount, self.sweetnsourCount, self.wontonCount, self.hoisinCount, self.prawnCount, self.riceCount, self.noodleCount, self.chipCount, self.pmaxCount, self.fantaCount, self.spriteCount, self.pepperCount))
        self.fantapositive.grid(row=24, column=11)
        self.formatlabel5 = tk.Label(myframe, text="", bg="white", font=('Helvetica', 15), fg="black").grid(row=25,column=0, columnspan=12)
      
        self.spritelabel = tk.Label(myframe, text="Sprite", bg="white", font=('Helvetica', 15), fg="black")
        self.spritelabel.grid(row=26, column=3, columnspan=4)
        self.sprite = Image.open('sprite.png')
        self.sprite = self.sprite.resize((142, 142), resample=Image.BILINEAR)
        self.photo14 = ImageTk.PhotoImage(self.sprite)
        self.label14 = tk.Label(myframe, image=self.photo14)
        self.label14.sprite = self.photo14
        self.label14.grid(row=27,column=3,columnspan=4)
        self.spritenegative = tk.Button(myframe, text="-", bg="white", font=('Helvetica', 10), fg="black", command=lambda: MenuScreen.removeFromBasket(self, 12, self.fncCount, self.burgerCount, self.ribsCount, self.sweetnsourCount, self.wontonCount, self.hoisinCount, self.prawnCount, self.riceCount, self.noodleCount, self.chipCount, self.pmaxCount, self.fantaCount, self.spriteCount, self.pepperCount))
        self.spritenegative.grid(row=28, column=3)
        self.spritenumber = tk.Label(myframe, text="0", bg="white", font=('Helvetica', 10), fg="black", relief="raised",padx=6,pady=5)
        self.spritenumber.grid(row=28, column=4)
        self.spriteprice = tk.Label(myframe, text="£0.99", bg="white", font=('Helvetica', 10), fg="black", relief="raised",padx=6,pady=5)
        self.spriteprice.grid(row=28, column=5)
        self.spritepositive = tk.Button(myframe, text="+", bg="white", font=('Helvetica', 10), fg="black", command=lambda: MenuScreen.addToBasket(self, 12, self.fncCount, self.burgerCount, self.ribsCount, self.sweetnsourCount, self.wontonCount, self.hoisinCount, self.prawnCount, self.riceCount, self.noodleCount, self.chipCount, self.pmaxCount, self.fantaCount, self.spriteCount, self.pepperCount))
        self.spritepositive.grid(row=28, column=6)

        self.pepperlabel = tk.Label(myframe, text="Dr pepper", bg="white", font=('Helvetica', 15))
        self.pepperlabel.grid(row=26, column=8, columnspan=4)
        self.pepper = Image.open('drpepper.png')
        self.pepper = self.pepper.resize((142, 142), resample=Image.BILINEAR)
        self.photo15 = ImageTk.PhotoImage(self.pepper)
        self.label15 = tk.Label(myframe, image=self.photo15)
        self.label15.pepper = self.photo15
        self.label15.grid(row=27,column=8,columnspan=4)
        self.peppernegative = tk.Button(myframe, text="-", bg="white", font=('Helvetica', 10), fg="black", command=lambda: MenuScreen.removeFromBasket(self, 13, self.fncCount, self.burgerCount, self.ribsCount, self.sweetnsourCount, self.wontonCount, self.hoisinCount, self.prawnCount, self.riceCount, self.noodleCount, self.chipCount, self.pmaxCount, self.fantaCount, self.spriteCount, self.pepperCount))
        self.peppernegative.grid(row=28, column=8)
        self.peppernumber = tk.Label(myframe, text="0", bg="white", font=('Helvetica', 10), fg="black", relief="raised",padx=6,pady=5)
        self.peppernumber.grid(row=28, column=9)
        self.pepperprice = tk.Label(myframe, text="£0.99", bg="white", font=('Helvetica', 10), fg="black", relief="raised",padx=6,pady=5)
        self.pepperprice.grid(row=28, column=10)
        self.pepperpositive = tk.Button(myframe, text="+", bg="white", font=('Helvetica', 10), fg="black", command=lambda: MenuScreen.addToBasket(self, 13, self.fncCount, self.burgerCount, self.ribsCount, self.sweetnsourCount, self.wontonCount, self.hoisinCount, self.prawnCount, self.riceCount, self.noodleCount, self.chipCount, self.pmaxCount, self.fantaCount, self.spriteCount, self.pepperCount))
        self.pepperpositive.grid(row=28, column=11)

        self.basketimg = Image.open('basket.png')
        self.basketimg = self.basketimg.resize((30, 30), resample=Image.BILINEAR)
        self.photobasket = ImageTk.PhotoImage(self.basketimg)
        self.basketButton = tk.Button(myframe, image=self.photobasket, command=lambda: BasketScreen(self.basket, customerID, myframe, mainRoot, userEntry, passEntry))
        self.basketButton.basketimg = self.basketButton
        self.basketButton.grid(row=29,column=7,pady=30)
      
        self.image2 = Image.open("backarrow.png")
        self.image2 = self.image2.resize((30, 30))
        self.photo2 = ImageTk.PhotoImage(self.image2)
        self.backButton = tk.Button(myframe, image=self.photo2, bg="white", command=lambda: self.goBack(master, mainRoot, userEntry, passEntry))
        self.backButton.grid(row=29,column=0,pady=5)
      
class BasketScreen():
    def goBack(self):
      self.master.destroy()

    def addOrder(self, master, basket, customerID, deliveryOpt, discount, oldWin, mainRoot, userEntry, passEntry, extranotes, total):
          basketStr = ""
          if deliveryOpt == "Delivery":
              total += 1.5
          previousOrders = BasketScreen.getOrders(self)
          if len(previousOrders) == 0:
              orderID = 1
          else:
              orderID = int((previousOrders[(len(previousOrders)-1)][0])[2:3]) + 1
    
          for items in basket:
              basketStr += str(items)
          if deliveryOpt != "" and basketStr != "00000000000000":
              with open("orders.txt", "a")as q:
                  q.write("O-" + str(orderID) + "\n")
                  q.write(customerID + "\n")
                  q.write(basketStr)
                  q.write("\n"+ str(total) + "\n")
                  q.write(str(deliveryOpt) + "\n")
                  q.write(str(discount) + "\n")
                  q.write(str(extranotes) + "\n")
                  mainRoot.deiconify()
                  MainScreen.clearEntrys(userEntry, passEntry)
                  popup = tk.Toplevel(bg="white")
                  popup.title("Success")
                  label = tk.Label(popup, text="Added order\nRef:" + str(orderID), bg="white", fg="green")
                  label.pack(padx=10, pady=10)
                  popup.after(5000, popup.destroy)
                  oldWin.destroy()
                  self.myframe.destroy()
                  master.destroy()
          elif basketStr == "00000000000000":
              popup = tk.Toplevel(bg="white")
              popup.title("Error")
              label = tk.Label(popup, text="Can't order with an empty basket", bg="white", fg="red")
              label.pack(padx=10, pady=10)
              popup.after(5000, popup.destroy)            
          else:
              popup = tk.Toplevel(bg="white")
              popup.title("Error")
              label = tk.Label(popup, text="Select Service", bg="white", fg="red")
              label.pack(padx=10, pady=10)
              popup.after(5000, popup.destroy)
              # create a new instance of MainScreen before destroying the current window
    def getOrders(self):
        list = []
        with open("orders.txt", "r") as f:
            eof = False
            while not eof:
                orderID = f.readline().strip()
                customerID = f.readline().strip()
                items = f.readline().strip()
                total = f.readline().strip()
                deliveryOpt = f.readline().strip()
                discount = f.readline().strip()
                orderNotes = f.readline().strip()
                list.append([orderID, customerID, items, total, deliveryOpt, discount, orderNotes])
                if orderID == "":
                 eof = True
            list.pop()
        return list
      
    def __init__(self, tbasket, customerID, oldWin, mainRoot, userEntry, passEntry):
        self.master = tk.Toplevel()
        self.master.geometry("475x375")
        self.master.configure(bg="white")

        wrapper = tk.LabelFrame(self.master, bg="white")
        wrapper.pack(fill="both", expand="yes")
        myCanvas = tk.Canvas(wrapper, bg="white", height=600)
        myCanvas.pack(side=tk.LEFT, fill="both", expand="yes")
        
        yscrollbar = ttk.Scrollbar(wrapper, orient="vertical", command=myCanvas.yview)
        yscrollbar.pack(side=tk.RIGHT, fill="y")
      
        self.myframe = tk.Frame(myCanvas, bg="white")   
        myCanvas.configure(yscrollcommand=yscrollbar.set, bg="white")
        myCanvas.bind("<Configure>", lambda e: myCanvas.configure(scrollregion=myCanvas.bbox("all")))
      
        myCanvas.create_window((0,0), window=self.myframe, anchor="nw")

        self.tbasket = tbasket
        self.basketlabel = tk.Label(self.myframe, text="Basket", bg="white", font=('Helvetica', 15), fg="black")
        self.basketlabel.grid(row=0, column=0)
      
        img = Image.open("fishysunak.jpg")
        img = img.resize((100, 100))
        img = ImageOps.expand(img, border=-20)
        photo = ImageTk.PhotoImage(img)
      
        imglabel = tk.Label(self.myframe, image=photo, bg="white")
        imglabel.image = photo 
        imglabel.grid(row=0, column=2)

        def addLabel(item, numberOf, r):
            itemLabel = tk.Label(self.myframe, text=(item + " Quantity: " + numberOf), bg="white", font=('Helvetica', 15)).grid(row=r, column=1, columnspan=2)
        r = 0
        for i in range(0, len(self.tbasket)):
            if self.tbasket[i] != 0:
                r += 1
                if i == 0:
                    addLabel("Fish and Chips", str(self.tbasket[i]), r)
                elif i == 1:
                    addLabel("Burger", str(self.tbasket[i]), r)
                elif i == 2:
                    addLabel("Ribs", str(self.tbasket[i]), r)
                elif i == 3:
                    addLabel("Sweet & Sour", str(self.tbasket[i]), r)
                elif i == 4:
                    addLabel("Wonton Soup", str(self.tbasket[i]), r)
                elif i == 5:
                    addLabel("Hoisin Ribs", str(self.tbasket[i]), r)
                elif i == 6:
                    addLabel("Prawn Toast", str(self.tbasket[i]), r)
                elif i == 7:
                    addLabel("Rice", str(self.tbasket[i]), r)
                elif i == 8:
                    addLabel("Noodles", str(self.tbasket[i]), r)
                elif i == 9:
                    addLabel("Chips", str(self.tbasket[i]), r)
                elif i == 10:
                    addLabel("Pepsi Max", str(self.tbasket[i]), r)
                elif i == 11:
                    addLabel("Fanta", str(self.tbasket[i]), r)
                elif i == 12:
                    addLabel("Sprite", str(self.tbasket[i]), r)
                elif i == 13:
                    addLabel("Dr Pepper", str(self.tbasket[i]), r)

        discountLabel = tk.Label(self.myframe, text="Discounts:", bg="white", font=('Helvetica', 15), fg="black")
        discountLabel.grid(row=r+1, column=1, pady=5)
        discounts = ['None', 'Discount 1', 'Discount 2', 'Discount 3']
        self.discountVar = tk.StringVar(self.myframe)
        self.discountVar.set(discounts[0])
        self.discountDropdown = tk.OptionMenu(self.myframe, self.discountVar, *discounts)
        self.discountDropdown.config(bg="white", font=('Helvetica', 15), fg="black")
        self.discountDropdown.grid(row=r+1, column=2,rowspan=2, pady=5)
        self.image2 = Image.open("backarrow.png")
        self.image2 = self.image2.resize((30, 30))
        self.photo2 = ImageTk.PhotoImage(self.image2)
        self.backButton = tk.Button(self.myframe, image=self.photo2, bg="white", command=lambda: self.goBack())
        self.backButton.grid(row=r+5,column=0,pady=20)
        self.backButton.image = self.photo2
        self.total = round((8.99*self.tbasket[0] + 7.99*self.tbasket[1] + 9.99*self.tbasket[2] + 6.99*self.tbasket[3] + 4.99*self.tbasket[4]  + 7.99*self.tbasket[5] + 4.99*self.tbasket[6] + 1.99*self.tbasket[7] + 4.99*self.tbasket[8] + 3.99*self.tbasket[9] + 0.99*self.tbasket[10] + 0.99*self.tbasket[11] + 0.99*self.tbasket[12] + 0.99*self.tbasket[13]), 2)
        self.totalLabel = tk.Label(self.myframe, text="Total: " + str(self.total), bg="white", font=('Helvetica', 15))
        self.totalLabel.grid(row=r+5,column=1,pady=2)
        selected_option = tk.StringVar()
        original_price = self.total
        option = ""
        
        def update_option(current, label, delivery_var, eating_in_var):
            delivery = delivery_var.get()
            eating_in = eating_in_var.get()
            if delivery:
                selected_option.set("Delivery")
                label.configure(text="Total: " + str(current+1.5), fg="black")
            elif eating_in:
                selected_option.set("Eating In")
                label.configure(text="Total: " + str(current), fg="black")
                selected_option.set("Eating In")
            else:
                selected_option.set("")
                current = original_price
                label.configure(text="Total: " + str(current), fg="black")
        
        delivery_var = tk.BooleanVar()
        delivery_checkbox = tk.Checkbutton(self.myframe, text="Delivery", variable=delivery_var, command=lambda: update_option(self.total, self.totalLabel, delivery_var, eating_in_var), bg="white")
        delivery_checkbox.grid(row=r+1)
        
        eating_in_var = tk.BooleanVar()
        eating_in_checkbox = tk.Checkbutton(self.myframe, text="Eating In", variable=eating_in_var, command=lambda: update_option(self.total, self.totalLabel, delivery_var, eating_in_var), bg="white")
        eating_in_checkbox.grid(row=r+2)

        self.extranotes = tk.Label(self.myframe, text="Extra notes:", bg="white", font=('Helvetica', 15), fg="black")
        self.extranotes.grid(row = r+4,column=1)

        self.noteEntry = tk.Entry(self.myframe, font=('Helvetica', 15), width=10)
        self.noteEntry.grid(row = r+4, column=2)
        
        self.orderButton = tk.Button(self.myframe, text="Order", bg="white", font=('Helvetica', 15), fg="black", command= lambda: BasketScreen.addOrder(self, self.master, self.tbasket, customerID, selected_option.get(), self.discountVar.get(), oldWin, mainRoot, userEntry, passEntry, self.noteEntry.get(), self.total))
        self.orderButton.grid(row = r+5, column = 3)
Home = MainScreen(root)
root.mainloop()
