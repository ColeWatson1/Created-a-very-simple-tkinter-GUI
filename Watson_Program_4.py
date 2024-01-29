#This program creates 4 different GUI's and at the end, if you press 'Display Charges' a message box popup will happen displaying the output
import tkinter as tk
import tkinter.messagebox

class MyGUI:
    def __init__(self):
        self.fName = ""
        self.lName = ""
        self.phone = ""
        self.email = ""
        self.prefShow = ""



        self.mainWindow = tk.Tk()
        self.mainWindow.configure(bg = "black")
        self.mainWindow.geometry("500x550")
        self.mainWindow.title("Watson Theater")
        self.topFrame = tk.Frame(self.mainWindow, bg = "navajo white")
        self.middleFrame = tk.Frame(self.mainWindow, bd = 20, bg = "light blue", relief = "ridge")
        self.bottomFrame = tk.Frame(self.mainWindow, bd = 20, bg = "light green", relief = "ridge")
        self.buttonFrame = tk.Frame(self.mainWindow, bd = 2, bg = "white", relief = "ridge")

        #TopFrame
        self.customerInfoLabel = tk.Label(self.topFrame, text = "CUSTOMER INFORMATION", font = ("Impact", 12), fg = "dark red", bg = "navajo white")
        self.enterfName = tk.Label(self.topFrame, text = "Enter Customer First Name:", bg = "navajo white")
        self.fName = tk.Entry(self.topFrame, fg = "blue", font = ("Arial", 14), width = 10, justify = "left")
        self.enterlName = tk.Label(self.topFrame, text = "Enter Customer Last Name:", bg = "navajo white")
        self.lName = tk.Entry(self.topFrame, fg = "blue", font = ("Arial", 14), width = 10, justify = "left")
        self.enterphone = tk.Label(self.topFrame, text = "Enter Customer Phone:", bg = "navajo white")
        self.phone = tk.Entry(self.topFrame, fg = "blue", font = ("Arial", 14), width = 11, justify = "left")
        self.enterEmail = tk.Label(self.topFrame, text = "Enter Customer Email:", bg = "navajo white")
        self.email = tk.Entry(self.topFrame, fg = "blue", font = ("Arial", 14), width = 20, justify = "left")
        self.enterShow = tk.Label(self.topFrame, text = "Enter Preferred Show:", bg = "navajo white")
        self.prefShow = tk.Entry(self.topFrame, fg = "blue", font = ("Arial", 14), width = 10, justify = "left")
        
        
        self.fName.focus()
        self.customerInfoLabel.pack()
        self.enterfName.pack()
        self.fName.pack()
        self.enterlName.pack()
        self.lName.pack()
        self.enterphone.pack()
        self.phone.pack()
        self.enterEmail.pack()
        self.email.pack()
        self.enterShow.pack()
        self.prefShow.pack(pady = 10)

        #Middle Frame
        self.showType = tk.IntVar()
        self.showType.set(0)
        self.showTypeLabel = tk.Label(self.middleFrame, text = "SHOW TYPE", font = ("Impact", 12), fg = "green", bg = "light blue")
        self.orchestra = tk.Radiobutton(self.middleFrame, bg = "light blue", fg = "black", text = "Orchestra - $209.00", variable = self.showType, value = 1)
        self.mezzanine = tk.Radiobutton(self.middleFrame, bg = "light blue", fg = "black", text = "Mezzanine - $179.00", variable = self.showType, value = 2)
        self.balcony = tk.Radiobutton(self.middleFrame, bg = "light blue", fg = "black", text = "Balcony - $149.00", variable = self.showType, value = 3)
        self.showTypeLabel.pack()
        self.orchestra.pack(side = "left")
        self.mezzanine.pack(side = "left")
        self.balcony.pack(side = "left")



        #BottomFrame Checkboxes
        self.cb1 = tk.IntVar()
        self.cb2 = tk.IntVar()
        self.cb3 = tk.IntVar()
        self.cb1.set(0)
        self.cb2.set(0)
        self.cb3.set(0)
        #Create the checkboxes
        self.addonLabel = tk.Label(self.bottomFrame, text = "ADD-ON", font = ("Impact", 12), fg = "navy", bg = "light green")
        self.cb1Var = tk.Checkbutton(self.bottomFrame, bg = "light green", fg = "black", text = "Pre-Paid Parking - $25.00", variable = self.cb1)
        self.cb2Var = tk.Checkbutton(self.bottomFrame, bg = "light green", fg = "black", text = "Refreshment Coupon ($50.00 Value) - $40.00", variable = self.cb2)
        self.cb3Var = tk.Checkbutton(self.bottomFrame, bg = "light green", fg = "black", text = "Coat Check - $10.00", variable = self.cb3)
        self.addonLabel.pack()
        self.cb1Var.pack()
        self.cb2Var.pack()
        self.cb3Var.pack()
                                   
        #Button Frame
        self.displayCharges = tk.Button(self.buttonFrame, text = "Display Charges", fg = "blue", bg = "white",  command = self.DisplayCharges)
        self.quit = tk.Button(self.buttonFrame, text = "Quit", fg = "red", bg = "white", command = self.mainWindow.destroy)
        self.clear = tk.Button(self.buttonFrame, text = "Clear", fg = "red", bg = "white", command = self.ClearFields)
        

        self.displayCharges.pack(side = 'left')
        self.quit.pack(side = 'left')
        self.clear.pack(side = 'left')

        #PACK FRAMES
        self.topFrame.pack()
        self.middleFrame.pack()
        self.bottomFrame.pack()
        self.buttonFrame.pack()


        #Backend Output and clear
    def ClearFields(self):
        self.fName.delete(0,'end')
        self.lName.delete(0, 'end')
        self.phone.delete(0, 'end')
        self.email.delete(0, 'end')
        self.prefShow.delete(0, 'end')
        self.showType.set(0)
        self.cb1Var.deselect()
        self.cb2Var.deselect()
        self.cb3Var.deselect()
        self.fName.focus_set()



    def DisplayCharges(self):
        self.total = 0.00
        fName = self.fName.get()
        lName = self.lName.get()
        phone = self.phone.get()
        email = self.email.get()
        prefShow = self.prefShow.get()
        #this method is called from the self.displayCharges button
        self.message = "Customer Name: " + fName + " " + lName + "\n"
        self.message += "Customer Phone: " + phone + "\n"
        self.message += "Customer Email: " + email + "\n"
        self.message += "Preferred Show: " + prefShow + "\n"
        if (self.showType.get() == 1):
            self.message = self.message + "Seat Type: Orchestra\n"
            self.message += "Seat Type Charge: $209.00\n"
            self.total = 209.00
        elif (self.showType.get() == 2):
            self.message += "Seat Type: Mezzanine\n"
            self.message += "Seat Type Charge: $179.00\n"
            self.total = 179.00
        elif (self.showType.get() == 3):
            self.message += "Seat Type: Balcony\n"
            self.message += "Seat Type Charge: $149.00\n"
            self.total = 149.00
        if (self.cb1.get() == 1):
            self.message += "Pre-Paid Parking: $25.00\n"
            self.total += 25.00
        if (self.cb2.get() == 1):
            self.message += "Refreshment Coupon ($50.00 Value): $40.00\n"
            self.total += 40.00
        if (self.cb3.get() == 1):
            self.message += "Coat Check: $10.00\n"
            self.total += 10.00
        if ((self.cb1.get() == 0 ) and (self.cb2.get() == 0) and (self.cb3.get() == 0)) or (self.showType.get() == 0) or (self.fName.get() == "") or (self.lName.get() == "") or (self.phone.get() == "") or (self.email.get() == "") or (self.prefShow.get() == ""):
            tk.messagebox.showinfo("ERROR", "\n\tNot all information is selected!")
        else:
            tk.messagebox.showinfo("Total Charges", self.message + "\n\nYour total charges: $" + str(format(self.total, ",.2f")))
        




instance = MyGUI()
        
