from tkinter import*
from tkinter import Tk, StringVar, ttk
import random
import datetime
import time;
root = Tk()
root.geometry("1350x750+0+0")
root.title("Stock Control System")


TopFrame=Frame(root, width = 1350, height = 100, bd=14, relief='raise')
TopFrame.pack(side=TOP)

LeftMidFrame=Frame(root, width = 600, height = 1000, bd=14, relief='raise')
LeftMidFrame.pack(side=LEFT)

RightMidFrame=Frame(root, width = 750, height = 1000, bd=14, relief='raise')
RightMidFrame.pack(side=RIGHT)




lblTitle=Label(TopFrame, font=('arial',50,'bold'),text="Stock Control System", bd=10, width=41, justify='center')
lblTitle.grid(row=0,column=0)
#==========================Var ================================
var1=IntVar()
var2=IntVar()
var3=IntVar()
var4=IntVar()
var5=IntVar()
var6=IntVar()
var7=IntVar()
var8=IntVar()
var9=IntVar()
Tax=StringVar()
Date1=StringVar()
Costperunit=StringVar()




var1.set("")
var2.set("")
var3.set("")
var4.set("")
var5.set("")
var6.set("")
var7.set("")
var8.set("")
var9.set("")
Tax.set("0")
Costperunit.set("")

Date1.set(time.strftime("%d/%m/%y"))

def Product():
    if (var1.get() == "PID001"):
              var2.set("Rice")
              var3.set("White seed")
              var4.set(800)
              var5.set(50)
              var6.set(2)
              var7.set("")
              var8.set("")
              var9.set("0")
              Costperunit.set(5.8)
    elif (var1.get()=="PID002"):
              var2.set("Rice")
              var3.set("White seed")
              var4.set(800)
              var5.set(50)
              var6.set(2)
              var7.set("")
              var8.set("")
              var9.set("0")
              Costperunit.set(5.8)
   
#==========================Product Details ================================

lblProductID=Label(LeftMidFrame, font=('arial',14,'bold'),text="Product Id", bd=10, width=20, anchor='w')
lblProductID.grid(row=0,column=0)
cmbProductID=ttk.Combobox(LeftMidFrame,textvariable=var1,state='readonly', font=('arial',14,'bold'), width=18,)
cmbProductID['value']=('','PID001','PID002','PID003','PID004','PID005','PID006','PID007','PID008','PID009')
cmbProductID.current(0)
cmbProductID.grid(row=0,column=1)

lblProductName=Label(LeftMidFrame, font=('arial',14,'bold'),text="Product Name", bd=10, width=20, anchor='w')
lblProductName.grid(row=1,column=0)
lblProductName1=Label(LeftMidFrame, font=('arial',14,'bold'),textvariable=var2, bd=10, width=18, relief='sunken')
lblProductName1.grid(row=1,column=1)

lblDescription=Label(LeftMidFrame, font=('arial',14,'bold'),text="Description", bd=10, width=20, anchor='w')
lblDescription.grid(row=2,column=0)
lblDescription1=Label(LeftMidFrame, font=('arial',14,'bold'),textvariable=var3, bd=10, width=18, relief='sunken')
lblDescription1.grid(row=2,column=1)

lblStockLevel=Label(LeftMidFrame, font=('arial',14,'bold'),text="Stock Level", bd=10, width=20, anchor='w')
lblStockLevel.grid(row=3,column=0)
lblStockLevel1=Label(LeftMidFrame, font=('arial',14,'bold'),textvariable=var4, bd=10, width=18, relief='sunken')
lblStockLevel1.grid(row=3,column=1)


lblRecordLevel=Label(LeftMidFrame, font=('arial',14,'bold'),text="Record Level", bd=10, width=20, anchor='w')
lblRecordLevel.grid(row=4,column=0)
lblRecordLevel1=Label(LeftMidFrame, font=('arial',14,'bold'),textvariable=var5, bd=10, width=18, relief='sunken')
lblRecordLevel1.grid(row=4,column=1)

lblOutofStock=Label(LeftMidFrame, font=('arial',14,'bold'),text="Out of Stock", bd=10, width=20, anchor='w')
lblOutofStock.grid(row=5,column=0)
lblOutofStock1=Label(LeftMidFrame, font=('arial',14,'bold'),textvariable=var6, bd=10, width=18, relief='sunken')
lblOutofStock1.grid(row=5,column=1)

lblNoofStockLevel=Label(LeftMidFrame, font=('arial',14,'bold'),text="No. of Stock", bd=10, width=20, anchor='w')
lblNoofStockLevel.grid(row=5,column=0)
lblNoofStockLevel1=Label(LeftMidFrame, font=('arial',14,'bold'),textvariable=var7, bd=10, width=18, relief='sunken')
lblNoofStockLevel1.grid(row=5,column=1)

lblAction=Label(LeftMidFrame, font=('arial',14,'bold'),text="Action", bd=10, width=20, anchor='w')
lblAction.grid(row=6,column=0)
lblAction1=Label(LeftMidFrame, font=('arial',14,'bold'),textvariable=var8, bd=10, width=18, relief='sunken')
lblAction1.grid(row=6,column=1)

lblRecorDate=Label(LeftMidFrame, font=('arial',14,'bold'),text="Record Date", bd=10, width=20, anchor='w')
lblRecorDate.grid(row=7,column=0)
lblRecorDate1=Label(LeftMidFrame, font=('arial',14,'bold'),textvariable=Date1, bd=10, width=18, relief='sunken')
lblRecorDate1.grid(row=7,column=1)

lblDiscount=Label(LeftMidFrame, font=('arial',14,'bold'),text="Discount", bd=10, width=20, anchor='w')
lblDiscount.grid(row=8,column=0)
lblDiscount1=Label(LeftMidFrame, font=('arial',14,'bold'),textvariable=var9, bd=10, width=18, relief='sunken')
lblDiscount1.grid(row=8,column=1)

lblCostperUnit=Label(LeftMidFrame, font=('arial',14,'bold'),text="cost per Unit", bd=10, width=20, anchor='w')
lblCostperUnit.grid(row=9,column=0)
lblCostperUnit1=Label(LeftMidFrame, font=('arial',14,'bold'),textvariable=Costperunit, bd=10, width=18, relief='sunken')
lblCostperUnit1.grid(row=9,column=1)
#=================================Right
lblValidForm=Label(RightMidFrame, font=('arial',14,'bold'),text="Valid Form", bd=10, width=14, anchor='w')
lblValidForm.grid(row=0,column=0)
lblValidForm1=Label(RightMidFrame, font=('arial',14,'bold'),textvariable=Date1, bd=10, width=14, relief='sunken')
lblValidForm1.grid(row=0,column=1)

lblDateofExpire=Label(RightMidFrame, font=('arial',14,'bold'),text="Date Expires", bd=10, width=14, anchor='w')
lblDateofExpire.grid(row=0,column=2)
lblDateofExpire=Label(RightMidFrame, font=('arial',14,'bold'),textvariable=Date1, bd=10, width=14, relief='sunken')
lblDateofExpire.grid(row=0,column=3)

lblRemainder=Label(RightMidFrame, font=('arial',14,'bold'),text="Remainder", bd=10, width=14, anchor='w')
lblRemainder.grid(row=1,column=0)
lblRemainder1=Label(RightMidFrame, font=('arial',14,'bold'),textvariable=var4, bd=10, width=14, relief='sunken')
lblRemainder1.grid(row=1,column=1)

lblOnSales=Label(RightMidFrame, font=('arial',14,'bold'),text="On Sales", bd=10, width=14, anchor='w')
lblOnSales.grid(row=1,column=2)
lblOnSales1=Label(RightMidFrame, font=('arial',14,'bold'),textvariable=var4, bd=10, width=14, relief='sunken')
lblOnSales1.grid(row=1,column=3)

lblOrderID=Label(RightMidFrame, font=('arial',14,'bold'),text="Order ID", bd=10, width=14, anchor='w')
lblOrderID.grid(row=2,column=0)
cmbOrderID1=ttk.Combobox(RightMidFrame,textvariable=var7,state='readonly', font=('arial',14,'bold'), width=14,)
cmbOrderID1['value']=('','CI001','CI002','CI003','CI004','CI005','CI006','CI007','CI008','CI009')
cmbOrderID1.current(0)
cmbOrderID1.grid(row=2,column=1)

lblDateofOrder=Label(RightMidFrame, font=('arial',14,'bold'),text="Date Of Order", bd=10, width=14, anchor='w')
lblDateofOrder.grid(row=2,column=2)
lblDateofOrder1=Label(RightMidFrame, font=('arial',14,'bold'),textvariable=Date1, bd=10, width=14, relief='sunken')
lblDateofOrder1.grid(row=2,column=3)

lblCustomerID=Label(RightMidFrame, font=('arial',14,'bold'),text="Customer ID", bd=10, width=14, anchor='w')
lblCustomerID.grid(row=3,column=0)
cmbCustomerID1=ttk.Combobox(RightMidFrame,textvariable=var8,state='readonly', font=('arial',14,'bold'), width=14,)
cmbCustomerID1['value']=('','CI001','CI002','CI003','CI004','CI005','CI006','CI007','CI008','CI009')
cmbCustomerID1.current(0)
cmbCustomerID1.grid(row=3,column=1)

lblNoofItemord=Label(RightMidFrame, font=('arial',14,'bold'),text="No. Of Item Odered", bd=10, width=14, anchor='w')
lblNoofItemord.grid(row=3,column=2)
lblNoofItemord1=Label(RightMidFrame, font=('arial',14,'bold'),textvariable=var4, bd=10, width=14, relief='sunken')
lblNoofItemord1.grid(row=3,column=3)


lblFirstName=Label(RightMidFrame, font=('arial',14,'bold'),text="First Name", bd=10, width=14, anchor='w')
lblFirstName.grid(row=4,column=0)
txtFirstName1=Entry(RightMidFrame, font=('arial',14,'bold'),bd=10, width=14, relief='sunken')
txtFirstName1.grid(row=4,column=1)

lblItemOrdered=Label(RightMidFrame, font=('arial',14,'bold'),text="Item Ordered", bd=10, width=14, anchor='w')
lblItemOrdered.grid(row=4,column=2)
lblItemOrdered1=Label(RightMidFrame, font=('arial',14,'bold'),bd=10, width=14, relief='sunken')
lblItemOrdered1.grid(row=4,column=3)

lblLastname=Label(RightMidFrame, font=('arial',14,'bold'),text="Last Name", bd=10, width=14, anchor='w')
lblLastname.grid(row=5,column=0)
txtLastname1=Entry(RightMidFrame, font=('arial',14,'bold'),bd=10, width=14, relief='sunken')
txtLastname1.grid(row=5,column=1)

lblPayment=Label(RightMidFrame, font=('arial',14,'bold'),text="Payment Method", bd=10, width=14, anchor='w')
lblPayment.grid(row=5,column=2)
cmbPayment1=ttk.Combobox(RightMidFrame,textvariable=var9,state='readonly', font=('arial',14,'bold'), width=14,)
cmbPayment1['value']=('','Cash','Debit Card','Master Card','Visa Card',)
cmbPayment1.current(0)
cmbPayment1.grid(row=5,column=3)

lblAddress=Label(RightMidFrame, font=('arial',14,'bold'),text="Address", bd=10, width=14, anchor='w')
lblAddress.grid(row=6,column=0)
lblAddress1=Label(RightMidFrame, font=('arial',14,'bold'),textvariable=var4, bd=10, width=45, height=3,relief='sunken')
lblAddress1.grid(row=6,column=1,columnspan=4)

lblAccounttype=Label(RightMidFrame, font=('arial',14,'bold'),text="Account Type", bd=10, width=14, anchor='w')
lblAccounttype.grid(row=7,column=0)
cmbAccounttype1=ttk.Combobox(RightMidFrame,textvariable=var6,state='readonly', font=('arial',14,'bold'), width=14,)
cmbAccounttype1['value']=('','Cash','Debit Card','Master Card','Visa Card',)
cmbAccounttype1.current(0)
cmbAccounttype1.grid(row=7,column=1)

lblGst=Label(RightMidFrame, font=('arial',14,'bold'),text="GST", bd=10, width=14, anchor='w')
lblGst.grid(row=7,column=2)
lblGst1=Label(RightMidFrame, font=('arial',14,'bold'),textvariable=Tax, bd=10, width=14, relief='sunken')
lblGst1.grid(row=7,column=3)

lblsubTotal=Label(RightMidFrame, font=('arial',14,'bold'),text="Sub Total", bd=10, width=14, anchor='w')
lblsubTotal.grid(row=8,column=0)
lblsubTotal1=Label(RightMidFrame, font=('arial',14,'bold'),textvariable=var4, bd=10, width=14, relief='sunken')
lblsubTotal1.grid(row=8,column=1)

lblTotal=Label(RightMidFrame, font=('arial',14,'bold'),text="Total", bd=10, width=14, anchor='w')
lblTotal.grid(row=8,column=2)
lblTotal1=Label(RightMidFrame, font=('arial',14,'bold'),textvariable=var4, bd=10, width=14, relief='sunken')
lblTotal1.grid(row=8,column=3)


btnTotal = Button(RightMidFrame, font=('rial',10,'bold'), text="Total",command=Product, bd=6, width=10)
btnTotal.grid(row=9,column=0)
btnReset = Button(RightMidFrame, font=('rial',10,'bold'), text="RESET", bd=2,width=10)
btnReset.grid(row=9,column=1)
btnExit = Button(RightMidFrame, font=('rial',10,'bold'), text="Exit", bd=2,width=10)
btnExit.grid(row=9,column=2)

root.mainloop()
