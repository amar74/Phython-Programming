from tkinter import*
from tkinter import ttk
import random
import time
import datetime

root = Tk()
root.geometry("1350x650+0+0")
root.title("My Ordering System")
root.configure(background='red')

#==============================================

def Exit():
    Exit = messagebox.askyesno("My Online ordering System", "Do You Want To Exit The System")
    if Exit>0:
        root.destroy()
        return

    
#=====================
def Reset():
    CustomerRef.set("")
    Tax.set("")
    SubTotal.set("")
    TotalCost.set("")
    CustomerName.set("")
    CustomerPhone.set("")
    CustomerEmail.set("")
    CostofOther.set(0)
    Costofwhitemomo.set(0)
    CostofRedmomo.set(0)
    UnitPriceOther.set(0)
    UnitPriceRedmomo.set(0)
    UnitPricewhitemomo.set(0)
    Qtyother.set(0)
    QtyRedmomo.set(0)
    QtyWhitemomo.set(0)
    Discount.set(0)
#=================================
def OrderRef():
    Refpay=random.randint(10300, 709467)
    Refpaid = ("OS" + str(Refpay))
    CustomerRef.set(Refpaid)
#=====================================
def CostofOrder():
    Qty1=float(QtyWhitemomo.get())
    Qty2=float(QtyRedmomo.get())
    Qty3=float(Qtyother.get())

    UnitPrice1 = float(UnitPricewhitemomo.get())
    UnitPrice2 = float(UnitPriceRedmomo.get())
    UnitPrice3 = float(UnitPriceOther.get())
    UnitPrice4 = float(Discount.get())

    Costofmomo1 = "Rs",str('%.2f'%(Qty1 * UnitPrice1))
    Costofmomo2 = "Rs",str('%.2f'%(Qty2 * UnitPrice2))
    Costofmomo3 = "Rs",str('%.2f'%(Qty3 * UnitPrice3))
    Costofdiscount= "Rs", str('%.2f'%(UnitPrice4))

    Costofwhitemomo.set(Costofmomo1)
    CostofRedmomo.set(Costofmomo2)
    CostofOther.set(Costofmomo3)
    Discount.set(Costofdiscount)


    Costmomo1 = (Qty1 * UnitPrice1)
    Costmomo2 = (Qty2 * UnitPrice2)
    Costmomo3 = (Qty3 * UnitPrice3)
    Costofdiscount = (UnitPrice4)

    AllCost=((Qty1 * UnitPrice1) + (Qty2 * UnitPrice2) +(Qty3 * UnitPrice3)-(UnitPrice4) )
 
    TaxAll="Rs",str('%.2f'%((AllCost) * 0.18))
    Tax.set(TaxAll)

    SubTotalp="Rs", str('%.2f'%(AllCost))
    SubTotal.set(SubTotalp)

    TotalCostp="Rs", str('%.2f'% (AllCost + ((AllCost) * 0.18)))
    TotalCost.set(TotalCostp)

    return

    

#=========================================
    
CustomerRef=StringVar()
Tax=StringVar()
SubTotal=StringVar()
Costofwhitemomo=StringVar()
CostofRedmomo=StringVar()
CostofOther=StringVar()
CostofDelivery=StringVar()
CustomerName=StringVar()
CustomerPhone=StringVar()
TimeOfOrder=StringVar()
DateOfOrder=StringVar()
Discount=StringVar()
CostofOther=StringVar()
Costofwhitemomo=StringVar()
CostofRedmomo=StringVar()
UnitPriceOther=StringVar()
UnitPriceRedmomo=StringVar()
UnitPricewhitemomo=StringVar()
Qtyother=StringVar()
QtyRedmomo=StringVar()
QtyWhitemomo=StringVar()
Discount=StringVar()
TotalCost=StringVar()
CustomerEmail=StringVar()
#================================================

CostofOther.set(0)
Costofwhitemomo.set(0)
CostofRedmomo.set(0)
UnitPriceOther.set(0)
UnitPriceRedmomo.set(0)
UnitPricewhitemomo.set(0)
Qtyother.set(0)
QtyRedmomo.set(0)
QtyWhitemomo.set(0)
Discount.set(0)
TimeOfOrder.set(time.strftime("%H:%M:%S"))
DateOfOrder.set(time.strftime("%d/%m/%y"))

#============================================================

Tops=Frame(root, width=1350, height=40, bd=16, relief="raise")
Tops.pack(side=TOP)
LF=Frame(root, width=700, height=900, bd=16, relief="raise")
LF.pack(side=LEFT)
RF=Frame(root, width=550, height=700, bd=16, relief="raise")
RF.pack(side=RIGHT)

Tops.configure(background='black')
LF.configure(background='black')
RF.configure(background='black')

LeftInsideLF=Frame(LF, width=500, height=80, bd=7, relief="raise")
LeftInsideLF.pack(side=TOP)
LeftInsideLFLF=Frame(LF, width=500, height=350, bd=8, relief="raise")
LeftInsideLFLF.pack(side=LEFT)

RightInsideLF=Frame(RF, width=604, height=200, bd=8, relief="raise")
RightInsideLF.pack(side=TOP)
RightInsideLFLF=Frame(RF, width=306, height=400, bd=8, relief="raise")
RightInsideLFLF.pack(side=LEFT)
RightInsideRFRF=Frame(RF, width=300, height=400, bd=8, relief="raise")
RightInsideRFRF.pack(side=RIGHT)

lblInfo = Label(Tops, font=('arial',50,'bold'), text="                    My Ordering Systems              ",
                bd=10, anchor='w')
lblInfo.grid(row=0,column=0)
#=============================== Top left Frame============================================================
lblCustomerName = Label(LeftInsideLF,font=('arial',13,'bold'),text="        Customer Name              ",
                     fg="black", bd=10, anchor="w")

lblCustomerName.grid(row=0,column=0)
txtCustomerName=Entry(LeftInsideLF, font=('arial',13,'bold'),bd=20,width=43,
                     bg="white", justify='left', textvariable=CustomerName)
txtCustomerName.grid(row=0,column=1)

lblCustomerPhone = Label(LeftInsideLF,font=('arial',13,'bold'),text="Customer Phone",
                     fg="black", bd=10, anchor="w")
lblCustomerPhone.grid(row=1,column=0)
txtCustomerPhone=Entry(LeftInsideLF, font=('arial',12,'bold'),bd=20,width=43,
                     bg="white", justify='left', textvariable=CustomerPhone)
txtCustomerPhone.grid(row=1,column=1)

lblCustomerEmail = Label(LeftInsideLF,font=('arial',12,'bold'),text="Customer Email",
                     fg="black", bd=10, anchor="w")
lblCustomerEmail.grid(row=2,column=0)
txtCustomerEmail=Entry(LeftInsideLF, font=('arial',12,'bold'),bd=20,width=43,
                     bg="white", justify='left', textvariable=CustomerEmail)
txtCustomerEmail.grid(row=2,column=1)
#=============================== Top Right Frame============================================================
lblDateofOrder=Label(RightInsideLF,font=('arial',12,'bold'),text="Date of Order",
                     fg="black", bd=10, anchor="w")
lblDateofOrder.grid(row=0,column=0)
txtDateofOrder=Entry(RightInsideLF, font=('arial',12,'bold'),bd=20,width=43,
                     bg="white", justify='left', textvariable=DateOfOrder)
txtDateofOrder.grid(row=0,column=1)
lblTimeofOrder=Label(RightInsideLF,font=('arial',12,'bold'),text="Time of Order",
                     fg="black", bd=10, anchor="w")
lblTimeofOrder.grid(row=1,column=0)
txtTimeofOrder=Entry(RightInsideLF, font=('arial',12,'bold'),bd=20,width=43,
                     bg="white", justify='left', textvariable=TimeOfOrder)
txtTimeofOrder.grid(row=1,column=1)
lblCustomerRef=Label(RightInsideLF,font=('arial',12,'bold'),text="CustomerRef",
                     fg="black", bd=10, anchor="w")
lblCustomerRef.grid(row=2,column=0)
txtCustomerRef=Entry(RightInsideLF, font=('arial',12,'bold'),bd=20,width=43,
                     bg="white", justify='left', textvariable=CustomerRef)
txtCustomerRef.grid(row=2,column=1)

#===============================Right Frame============================================================
lblMethodOfPayment=Label(RightInsideLFLF,font=('arial',12,'bold'), text="Method of Payment",
                         fg="black", bd=16, anchor="w")
lblMethodOfPayment.grid(row=0,column=0)
cmdMethodOfPayment=ttk.Combobox(RightInsideLFLF,font=('arial',10,'bold'))
cmdMethodOfPayment['value']=('','cash','Debit Card','Visa Card','Master Card')
cmdMethodOfPayment.grid(row=0,column=1)
lblDiscount=Label(RightInsideLFLF,font=('arial',12,'bold'),text="Discount",
                  fg="black",bd=16, anchor='w')
lblDiscount.grid(row=1,column=0)
txtDiscount=Entry(RightInsideLFLF,font=('arial',12,'bold'),bd=16, width=18,
                  bg="white",justify='left',textvariable=Discount)
txtDiscount.grid(row=1,column=1)

lblTax=Label(RightInsideLFLF,font=('arial',12,'bold'),text="Tax",
                  fg="black",bd=16, anchor='w')
lblTax.grid(row=2,column=0)
txtTax=Entry(RightInsideLFLF,font=('arial',12,'bold'),bd=16, width=18,
                  bg="white",justify='left',textvariable=Tax)
txtTax.grid(row=2,column=1)
lblSubTotal=Label(RightInsideLFLF,font=('arial',12,'bold'),text="SubTotal",
                  fg="black",bd=16, anchor='w')
lblSubTotal.grid(row=3,column=0)
txtSubTotal=Entry(RightInsideLFLF,font=('arial',12,'bold'),bd=16, width=18,
                  bg="white",justify='left',textvariable=SubTotal)
txtSubTotal.grid(row=3,column=1)

lblTotalCost=Label(RightInsideLFLF,font=('arial',12,'bold'),text="TotalCost",
                  fg="black",bd=16, anchor='w')
lblTotalCost.grid(row=4,column=0)
txtTotalCost=Entry(RightInsideLFLF,font=('arial',12,'bold'),bd=16, width=18,
                  bg="white",justify='left',textvariable=TotalCost)
txtTotalCost.grid(row=4,column=1)
#==========================btn Right Frame=============================================================

lblItemOrder=Label(LeftInsideLFLF,font=('arial',13,'bold'),text='Item order',fg="black",bd=20)
lblItemOrder.grid(row=0,column=0)
lblQty=Label(LeftInsideLFLF,font=('arial',13,'bold'),text='Qty',fg="black",bd=10)
lblQty.grid(row=0,column=1)
lblUnitPrice=Label(LeftInsideLFLF,font=('arial',13,'bold'),text='Unit Price',fg="black",bd=20)
lblUnitPrice.grid(row=0,column=2)
lblCostofItem=Label(LeftInsideLFLF,font=('arial',13,'bold'),text='Cost of Item',fg="black",bd=20)
lblCostofItem.grid(row=0,column=3)
#=================================
lblWhitemomo=Label(LeftInsideLFLF,font=('arial',13),text='White momo',fg="black",bd=20)
lblWhitemomo.grid(row=1,column=0)
lblRedmomo=Label(LeftInsideLFLF,font=('arial',13),text='Red momo',fg="black",bd=20)
lblRedmomo.grid(row=2,column=0)
lblOther=Label(LeftInsideLFLF,font=('arial',13),text='Other',fg="black",bd=20)
lblOther.grid(row=3,column=0)
#================================
txtQtyWhitemomo=Entry(LeftInsideLFLF,font=('arial',12,'bold'),bd=20, width=16,
                      bg="white",justify='left',textvariable=QtyWhitemomo)
txtQtyWhitemomo.grid(row=1,column=1)

txtQtyRedmomo=Entry(LeftInsideLFLF,font=('arial',12,'bold'),bd=20, width=16,
                      bg="white",justify='left',textvariable=QtyRedmomo)
txtQtyRedmomo.grid(row=2,column=1)

txtOther=Entry(LeftInsideLFLF,font=('arial',12,'bold'),bd=20, width=16,
                      bg="white",justify='left',textvariable=Qtyother)
txtOther.grid(row=3,column=1)
#=================================
txtUnitPriceWhitemomo=Entry(LeftInsideLFLF,font=('arial',12,'bold'),bd=20, width=16,
                      bg="white",justify='left',textvariable=UnitPricewhitemomo)
txtUnitPriceWhitemomo.grid(row=1,column=2)

txtUnitPriceQtyRedmomo=Entry(LeftInsideLFLF,font=('arial',12,'bold'),bd=20, width=16,
                      bg="white",justify='left',textvariable=UnitPriceRedmomo)
txtUnitPriceQtyRedmomo.grid(row=2,column=2)

txtUnitPriceOther=Entry(LeftInsideLFLF,font=('arial',12,'bold'),bd=20, width=16,
                      bg="white",justify='left',textvariable=UnitPriceOther)
txtUnitPriceOther.grid(row=3,column=2)
#=====================================
txtCostWhitemomo=Entry(LeftInsideLFLF,font=('arial',12,'bold'),bd=20, width=16,
                      bg="white",justify='left',textvariable=Costofwhitemomo)
txtCostWhitemomo.grid(row=1,column=3)

txtCostQtyRedmomo=Entry(LeftInsideLFLF,font=('arial',12,'bold'),bd=20, width=16,
                      bg="white",justify='left',textvariable=CostofRedmomo)
txtCostQtyRedmomo.grid(row=2,column=3)

txtCostOther=Entry(LeftInsideLFLF,font=('arial',12,'bold'),bd=20, width=16,
                      bg="white",justify='left',textvariable=CostofOther)
txtCostOther.grid(row=3,column=3)
#==========================btn Right Frame=============================================================

btnTotalCost=Button(RightInsideRFRF,pady=8,bd=8,fg="black",font=('arial',16,'bold'), width=11,
                    text="Total Cost", bg="white",command=CostofOrder).grid(row=0,column=0)
btnReset=Button(RightInsideRFRF,pady=8,bd=8,fg="black",font=('arial',16,'bold'), width=11,
                    text="Reset", bg="white",command=Reset).grid(row=1,column=0)
btnOrderRef=Button(RightInsideRFRF,pady=8,bd=8,fg="black",font=('arial',16,'bold'), width=11,
                    text="Order Ref", bg="white",command=OrderRef).grid(row=2,column=0)
btnExit=Button(RightInsideRFRF,pady=8,bd=8,fg="black",font=('arial',16,'bold'), width=11,
                    text="Exit", bg="white",command=Exit).grid(row=3,column=0) 
   
root.mainloop()
