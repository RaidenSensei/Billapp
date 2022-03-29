from tkinter import *
import random
from tkinter import messagebox
import os
class Bill_App:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1365x735+-8+0")
        self.root.title("Billing Software")
        bg_color="#074463"
        title = Label(self.root,text="Billing Software",bd=12, relief=GROOVE,bg= bg_color, fg = "gold", font=("arial",30,"bold"),pady=2).pack(fill=X)
        #===============variables=============

        #======cosmetics==========
        self.soap = IntVar()
        self.face_cream = IntVar()
        self.face_wash = IntVar()
        self.hair_spray = IntVar()
        self.body_lotion = IntVar()
        self.hair_gel = IntVar()
        #==============Grocery=============
        self.tea = IntVar()
        self.rice = IntVar()
        self.food_oil = IntVar()
        self.daal = IntVar()
        self.wheat = IntVar()
        self.sugar = IntVar()
        #==========drinks==============
        self.maaza = IntVar()
        self.coca_cola = IntVar()
        self.frooti = IntVar()
        self.thums_up = IntVar()
        self.sprite = IntVar()
        self.limca = IntVar()
        #================total product price and tax variable==============
        self.cosmetic_price = StringVar()
        self.grocery_price = StringVar()
        self.drink_price = StringVar()

        self.cosmetic_tax = StringVar()
        self.grocery_tax = StringVar()
        self.drinks_tax = StringVar()

        #================customer==============
        self.c_name = StringVar()
        self.c_phon = StringVar()
        self.bill_no = StringVar()
        x = random.randint(1000, 9999)
        self.bill_no.set(str(x))
        self.cus_address = StringVar()

        #============payment===========
        self.amtrec = IntVar()

        #=================customer detail frame=========
        F1=LabelFrame(self.root,bd=10,relief=GROOVE,text="Customer Details", font=("arial", 15,"bold"), fg="gold", bg=bg_color)
        F1.place(x=0,y=80,relwidth = 1)

        cname_lbl=Label(F1,text="Customer Name", bg = bg_color,fg= "white",font=("arial", 18,"bold")).grid(row=0,column=0, padx=20, pady =5)
        cname_txt=Entry(F1, width=15,textvariable=self.c_name,font = "arial 15",bd=7,relief=SUNKEN).grid(row=0,column=1,pady=5,padx=10)

        cphn_lbl = Label(F1, text="Phone No.", bg=bg_color, fg="white", font=("arial", 18, "bold")).grid(row=0,column=2,padx=20,pady=5)
        cphn_txt = Entry(F1, width=15,textvariable=self.c_phon, font="arial 15", bd=7, relief=SUNKEN).grid(row=0, column=3, pady=5, padx=10)

        c_bill_lbl = Label(F1, text="Address", bg=bg_color, fg="white", font=("arial", 18, "bold")).grid(row=0,column=4,padx=20,pady=5)
        c_bill_txt = Entry(F1, width=15,textvariable=self.cus_address, font="arial 15", bd=7, relief=SUNKEN).grid(row=0, column=5, pady=5, padx=10)

        clear_btn = Button(F1, text="Clear", command=self.clear_data, bg="cadetblue", fg="white", bd=2, pady=15,
                           width=11,
                           font="arial 12 bold").grid(row=0, column=6, padx=5, pady=5)

        #=======cosmetics frame===========

        F2 = LabelFrame(self.root, bd=10, relief=GROOVE, text="Cosmetics", font=("arial", 15, "bold"), fg="gold",bg=bg_color)
        F2.place(x=5, y=190, width=325,height=380)

        soap_lbl=Label(F2,text="Soap ₹5",font=("arial",16,"bold"),bg=bg_color,fg="lightgreen",).grid(row=0,column=0,padx=10,pady=10,sticky="w")
        soap_txt=Entry(F2,width=10,textvariable=self.soap,font=("arial",16,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10)

        fc_lbl = Label(F2, text="Face Cream ₹600", font=("arial", 16, "bold"), bg=bg_color, fg="lightgreen", ).grid(row=1,column=0,padx=10,pady=10,sticky="w")
        fc_txt = Entry(F2, width=10,textvariable=self.face_cream, font=("arial", 16, "bold"), bd=5, relief=SUNKEN).grid(row=1, column=1, padx=10,pady=10)

        facw_lbl = Label(F2, text="Face Wash ₹170", font=("arial", 16, "bold"), bg=bg_color, fg="lightgreen", ).grid(row=2, column=0,padx=10,pady=10,sticky="w")
        facw_txt = Entry(F2, width=10,textvariable=self.face_wash, font=("arial", 16, "bold"), bd=5, relief=SUNKEN).grid(row=2, column=1, padx=10,pady=10)

        hairs_lbl = Label(F2, text="Hair Spray ₹200", font=("arial", 16, "bold"), bg=bg_color, fg="lightgreen", ).grid(row=3,column=0,padx=10,pady=10,sticky="w")
        hairs_txt = Entry(F2, width=10,textvariable=self.hair_spray, font=("arial", 16, "bold"), bd=5, relief=SUNKEN).grid(row=3, column=1, padx=10,pady=10)

        body_lbl = Label(F2, text="Body Lotion ₹250", font=("arial", 16, "bold"), bg=bg_color, fg="lightgreen", ).grid(row=4,column=0,padx=10,pady=10,sticky="w")
        body_txt = Entry(F2, width=10,textvariable=self.body_lotion, font=("arial", 16, "bold"), bd=5, relief=SUNKEN).grid(row=4, column=1, padx=10,pady=10)

        hairg_lbl = Label(F2, text="Hair Gel ₹75", font=("arial", 16, "bold"), bg=bg_color, fg="lightgreen", ).grid(row=5,column=0,padx=10,pady=10,sticky="w")
        hairg_txt = Entry(F2, width=10,textvariable=self.hair_gel, font=("arial", 16, "bold"), bd=5, relief=SUNKEN).grid(row=5, column=1, padx=10,pady=10)

        # =======GROCERY frame===========

        F3 = LabelFrame(self.root, bd=10, relief=GROOVE, text="Grocery", font=("arial", 15, "bold"), fg="gold",
                        bg=bg_color)
        F3.place(x=340, y=190, width=325, height=380)

        g1 = Label(F3, text="Rice 100g ₹0.75", font=("arial", 16, "bold"), bg=bg_color, fg="lightgreen", ).grid(row=0,
                                                                                                           column=0,
                                                                                                           padx=10,
                                                                                                           pady=10,
                                                                                                           sticky="w")
        g1 = Entry(F3, width=10,textvariable=self.rice, font=("arial", 16, "bold"), bd=5, relief=SUNKEN).grid(row=0, column=1, padx=10,
                                                                                             pady=10)

        g2 = Label(F3, text="Food Oil 1l ₹102", font=("arial", 16, "bold"), bg=bg_color, fg="lightgreen", ).grid(row=1,
                                                                                                               column=0,
                                                                                                               padx=10,
                                                                                                               pady=10,
                                                                                                               sticky="w")
        g2 = Entry(F3, width=10,textvariable=self.food_oil, font=("arial", 16, "bold"), bd=5, relief=SUNKEN).grid(row=1, column=1, padx=10,
                                                                                           pady=10)

        g3 = Label(F3, text="Daal 100g ₹17", font=("arial", 16, "bold"), bg=bg_color, fg="lightgreen", ).grid(row=2,
                                                                                                                column=0,
                                                                                                                padx=10,
                                                                                                                pady=10,
                                                                                                                sticky="w")
        g3 = Entry(F3, width=10,textvariable=self.daal, font=("arial", 16, "bold"), bd=5, relief=SUNKEN).grid(row=2, column=1, padx=10,
                                                                                             pady=10)

        g4 = Label(F3, text="Wheat 1kg ₹54", font=("arial", 16, "bold"), bg=bg_color, fg="lightgreen", ).grid(row=3,
                                                                                                                  column=0,
                                                                                                                  padx=10,
                                                                                                                  pady=10,
                                                                                                                  sticky="w")
        g4 = Entry(F3, width=10,textvariable=self.wheat, font=("arial", 16, "bold"), bd=5, relief=SUNKEN).grid(row=3, column=1, padx=10,
                                                                                              pady=10)

        g5 = Label(F3, text="Sugar 1kg ₹46", font=("arial", 16, "bold"), bg=bg_color, fg="lightgreen", ).grid(row=4,
                                                                                                                  column=0,
                                                                                                                  padx=10,
                                                                                                                  pady=10,
                                                                                                                  sticky="w")
        g5 = Entry(F3, width=10,textvariable=self.sugar, font=("arial", 16, "bold"), bd=5, relief=SUNKEN).grid(row=4, column=1, padx=10,
                                                                                             pady=10)

        g6 = Label(F3, text="Tea 1pc ₹110", font=("arial", 16, "bold"), bg=bg_color, fg="lightgreen", ).grid(row=5,
                                                                                                                column=0,
                                                                                                                padx=10,
                                                                                                                pady=10,
                                                                                                                sticky="w")
        g6 = Entry(F3, width=10,textvariable=self.tea, font=("arial", 16, "bold"), bd=5, relief=SUNKEN).grid(row=5, column=1, padx=10,
                                                                                              pady=10)

        #==========Drinks Frame================

        F4 = LabelFrame(self.root, bd=10, relief=GROOVE, text="Drinks", font=("arial", 15, "bold"), fg="gold",
                        bg=bg_color)
        F4.place(x=340+335, y=190, width=325, height=380)

        d1 = Label(F4, text="Maaza 1pc ₹10", font=("arial", 16, "bold"), bg=bg_color, fg="lightgreen", ).grid(row=0,
                                                                                                           column=0,
                                                                                                           padx=10,
                                                                                                           pady=10,
                                                                                                           sticky="w")
        d1 = Entry(F4, width=4,textvariable=self.maaza, font=("arial", 16, "bold"), bd=5, relief=SUNKEN).grid(row=0, column=1, padx=10,
                                                                                             pady=10)

        d2 = Label(F4, text="Coca Cola 500ml ₹30", font=("arial", 16, "bold"), bg=bg_color, fg="lightgreen", ).grid(row=1,
                                                                                                               column=0,
                                                                                                               padx=10,
                                                                                                               pady=10,
                                                                                                               sticky="w")
        d2 = Entry(F4, width=4,textvariable=self.coca_cola, font=("arial", 16, "bold"), bd=5, relief=SUNKEN).grid(row=1, column=1, padx=10,
                                                                                           pady=10)

        d3 = Label(F4, text="Frooti 1pc ₹10", font=("arial", 16, "bold"), bg=bg_color, fg="lightgreen", ).grid(row=2,
                                                                                                                column=0,
                                                                                                                padx=10,
                                                                                                                pady=10,
                                                                                                                sticky="w")
        d3 = Entry(F4, width=4,textvariable=self.frooti, font=("arial", 16, "bold"), bd=5, relief=SUNKEN).grid(row=2, column=1, padx=10,
                                                                                             pady=10)

        d4 = Label(F4, text="Thumbs Up 250ml ₹20", font=("arial", 16, "bold"), bg=bg_color, fg="lightgreen", ).grid(row=3,
                                                                                                                  column=0,
                                                                                                                  padx=10,
                                                                                                                  pady=10,
                                                                                                                  sticky="w")
        d4 = Entry(F4, width=4,textvariable=self.thums_up, font=("arial", 16, "bold"), bd=5, relief=SUNKEN).grid(row=3, column=1, padx=10,
                                                                                              pady=10)

        d5 = Label(F4, text="Sprite 500ml ₹30", font=("arial", 16, "bold"), bg=bg_color, fg="lightgreen", ).grid(row=4,
                                                                                                                  column=0,
                                                                                                                  padx=10,
                                                                                                                  pady=10,
                                                                                                                  sticky="w")
        d5 = Entry(F4, width=4,textvariable=self.sprite, font=("arial", 16, "bold"), bd=5, relief=SUNKEN).grid(row=4, column=1, padx=10,
                                                                                             pady=10)

        d6 = Label(F4, text="Limca 500ml ₹25", font=("arial", 16, "bold"), bg=bg_color, fg="lightgreen", ).grid(row=5,
                                                                                                                column=0,
                                                                                                                padx=10,
                                                                                                                pady=10,
                                                                                                                sticky="w")
        d6 = Entry(F4, width=4,textvariable=self.limca, font=("arial", 16, "bold"), bd=5, relief=SUNKEN).grid(row=5, column=1, padx=10,
                                                                                              pady=10)

        #==============Bill Area==============

        F5 = Frame(self.root, bd=10, relief=GROOVE)
        F5.place(x=1010, y=190, width=337, height=380)

        bill_title=Label(F5,text="Bill Area",font="arial 15 bold",bd=7,relief=GROOVE).pack(fill=X)
        scroll_y=Scrollbar(F5,orient=VERTICAL)
        self.txtarea=Text(F5,yscrollcommand=scroll_y.set)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_y.config(command=self.txtarea.yview)
        self.txtarea.pack(fill=BOTH,expand=1)


        #=====================Button Frame==================

        F6 = LabelFrame(self.root, bd=10, relief=GROOVE, text="Bill Menu", font=("arial", 15, "bold"), fg="gold",
                        bg=bg_color)
        F6.place(x=0, y=580, relwidth=1, height=150)

        m1=Label(F6,text="Total Cosmetic Price",bg=bg_color,fg="white",font=("arial", 14, "bold")).grid(row=0,column=0,padx=20,pady=1,sticky="w")
        m1_txt=Entry(F6,width=18,textvariable=self.cosmetic_price,font="arial 10 bold", bd=7, relief=SUNKEN).grid(row=0,column=1, padx=10,pady=1)

        m2 = Label(F6, text="Total Grocery Price", bg=bg_color, fg="white", font=("arial", 14, "bold")).grid(row=1,
                                                                                                              column=0,
                                                                                                              padx=20,
                                                                                                              pady=1,
                                                                                                              sticky="w")
        m2_txt = Entry(F6, width=18,textvariable=self.grocery_price, font="arial 10 bold", bd=7, relief=SUNKEN).grid(row=1, column=1, padx=10, pady=1)

        m3 = Label(F6, text="Total Drinks Price", bg=bg_color, fg="white", font=("arial", 14, "bold")).grid(row=2,
                                                                                                              column=0,
                                                                                                              padx=20,
                                                                                                              pady=1,
                                                                                                              sticky="w")
        m3_txt = Entry(F6, width=18,textvariable=self.drink_price, font="arial 10 bold", bd=7, relief=SUNKEN).grid(row=2, column=1, padx=10, pady=1)

        c1 = Label(F6, text="Cosmetic Tax Price", bg=bg_color, fg="white", font=("arial", 14, "bold")).grid(row=0,
                                                                                                              column=3,
                                                                                                              padx=20,
                                                                                                              pady=1,
                                                                                                              sticky="w")
        c1_txt = Entry(F6, width=18,textvariable=self.cosmetic_tax, font="arial 10 bold", bd=7, relief=SUNKEN).grid(row=0, column=4, padx=10, pady=1)

        c2 = Label(F6, text="Grocery Tax", bg=bg_color, fg="white", font=("arial", 14, "bold")).grid(row=1,
                                                                                                             column=3,
                                                                                                             padx=20,
                                                                                                             pady=1,
                                                                                                             sticky="w")
        c2_txt = Entry(F6, width=18,textvariable=self.grocery_tax, font="arial 10 bold", bd=7, relief=SUNKEN).grid(row=1, column=4, padx=10, pady=1)

        c3 = Label(F6, text="Drinks Tax", bg=bg_color, fg="white", font=("arial", 14, "bold")).grid(row=2,
                                                                                                            column=3,
                                                                                                            padx=20,
                                                                                                            pady=1,
                                                                                                            sticky="w")
        c3_txt = Entry(F6, width=18,textvariable=self.drinks_tax, font="arial 10 bold", bd=7, relief=SUNKEN).grid(row=2, column=4, padx=10, pady=1)

        c4 = Label(F6, text="Amount Received", bg=bg_color, fg="white", font=("arial", 14, "bold")).grid(row=1,
                                                                                                    column=5,
                                                                                                    padx=20,
                                                                                                    pady=1,
                                                                                                    sticky="w")
        c4_txt = Entry(F6, width=18, textvariable=self.amtrec, font="arial 10 bold", bd=7, relief=SUNKEN).grid(
            row=2, column=5, padx=10, pady=1)

        btn_F = Frame(F6, bd=7, relief=GROOVE)
        btn_F.place(x=1040, width=280, relheight=1)

        total_btn=Button(btn_F,command=self.total,text="Total", bg="cadetblue", fg="white",bd=2,pady=15,width=11,font="arial 12 bold").grid(row=0,column=0,padx=5,pady=5)
        gbill_btn = Button(btn_F, text="Generate Bill",command=self.bill_area, bg="cadetblue", fg="white", bd=2, pady=15, width=11,
                           font="arial 12 bold").grid(row=0, column=1, padx=5, pady=5)
        exit_btn = Button(btn_F, text="Exit", command=self.exit_app, bg="cadetblue", fg="white", bd=2,
                           pady=15, width=11,
                           font="arial 12 bold").grid(row=1, column=0, padx=5, pady=5)
        self.welcome_bill()



    def total(self):
        self.c_s_p= self.soap.get() * 5
        self.c_fc_p= self.face_cream.get() * 600
        self.c_fw_p=self.face_wash.get()*170
        self.c_hs_p = self.hair_spray.get() * 200
        self.c_bl_p=self.body_lotion.get() *250
        self.c_hg_p=self.hair_gel.get() * 75
        self.total_cosmetic_price = float(
            self.c_s_p+
            self.c_fc_p+
            self.c_fw_p+
            self.c_hs_p+
            self.c_bl_p+
            self.c_hg_p
        )
        self.cosmetic_price.set("₹. "+str(self.total_cosmetic_price))
        self.c_tax=round((self.total_cosmetic_price*0.05),2)
        self.cosmetic_tax.set("₹."+str(self.c_tax))


        self.g_r_p= self.rice.get() * 0.75
        self.g_f_p=self.food_oil.get() * 102
        self.g_d_p=self.daal.get() * 17
        self.g_w_p=self.wheat.get() * 54
        self.g_s_p=self.sugar.get() * 46
        self.g_t_p=self.tea.get() * 110

        self.total_grocery_price = float(
            self.g_r_p +
            self.g_f_p +
            self.g_d_p +
            self.g_w_p +
            self.g_s_p +
            self.g_t_p
        )
        self.grocery_price.set("₹. "+str(self.total_grocery_price))
        self.g_tax=round((self.total_grocery_price * 0.1),2)
        self.grocery_tax.set("₹." + str(self.g_tax))


        self.d_m_p=self.maaza.get() * 10
        self.d_c_p=self.coca_cola.get() * 30
        self.d_f_p=self.frooti.get() * 60
        self.d_t_p=self.thums_up.get() * 240
        self.d_s_p=self.sprite.get() * 45
        self.d_l_p=self.limca.get() * 120

        self.total_drinks_price = float(
            self.d_m_p +
            self.d_c_p +
            self.d_f_p +
            self.d_t_p +
            self.d_s_p +
            self.d_l_p
        )
        self.drink_price.set("₹. "+str(self.total_drinks_price))
        self.d_tax=round((self.total_drinks_price * 0.15),2)
        self.drinks_tax.set("₹." + str(self.d_tax))

        self.total_bill=int(self.total_cosmetic_price+
                              self.total_grocery_price+
                              self.total_drinks_price+
                              self.c_tax+
                              self.g_tax+
                              self.d_tax
                                                )


        self.amre = self.amtrec.get()*1
        self.amount_received = int(
            self.amre -
            self.total_bill

        )
        self.drink_price.set("₹. " + str(self.total_drinks_price))
        self.d_tax = round((self.total_drinks_price * 0.15), 2)
        self.drinks_tax.set("₹" + str(self.d_tax))
        self.amtrec.set("₹. "+ (str(self.total_bill)))

    def welcome_bill(self):
        self.txtarea.delete(1.0, END)
        self.txtarea.insert(END, "\tWelcome to our store\n")
        self.txtarea.insert(END, f"\n Bill Number:{self.bill_no.get()}")
        self.txtarea.insert(END, f"\n Customer Name:{self.c_name.get()}")
        self.txtarea.insert(END, f"\n Phone Number:{self.c_phon.get()}")
        self.txtarea.insert(END, f"\n Customer Address:{self.cus_address.get()}")
        self.txtarea.insert(END, f"\n ====================================")
        self.txtarea.insert(END, f"\n Products\t\tQTY\t\tPrice")
        self.txtarea.insert(END, f"\n ====================================")


    def bill_area(self):
        if self.c_name.get() =="" or self.c_phon.get() == "" or self.cus_address.get() == "":
            messagebox.showerror("!!Error!!","Customer details are must")
        elif self.cosmetic_price.get() == "₹. 0.0" and self.grocery_price.get() == "₹. 0.0" and self.drink_price.get() == "₹. 0.0":
            messagebox.showerror("!!Error!!", "No product has been purchased")
        else:
            self.welcome_bill()
            #=====cosmetics========
            if self.soap.get() != 0:
                self.txtarea.insert(END, f"\n Soap\t\t{self.soap.get()}\t\t{self.c_s_p}")

            if self.face_cream.get() != 0:
                self.txtarea.insert(END, f"\n Face Cream\t\t{self.face_cream.get()}\t\t{self.c_fc_p}")

            if self.face_wash.get() != 0:
                self.txtarea.insert(END, f"\n Face Wash\t\t{self.face_wash.get()}\t\t{self.c_fw_p}")

            if self.hair_spray.get() != 0:
                self.txtarea.insert(END, f"\n Hair Spray\t\t{self.hair_spray.get()}\t\t{self.c_hs_p}")

            if self.body_lotion.get() != 0:
                self.txtarea.insert(END, f"\n Body lotion\t\t{self.body_lotion.get()}\t\t{self.c_bl_p}")

            if self.hair_gel.get() != 0:
                self.txtarea.insert(END, f"\n Hair Gel\t\t{self.hair_gel.get()}\t\t{self.c_hg_p}")

                #===grocery=========

            if self.rice.get() != 0:
                self.txtarea.insert(END, f"\n Rice\t\t{self.rice.get()}\t\t{self.g_r_p}")

            if self.food_oil.get() != 0:
                self.txtarea.insert(END, f"\n Food Oil\t\t{self.food_oil.get()}\t\t{self.g_f_p}")

            if self.daal.get() != 0:
                self.txtarea.insert(END, f"\n Daal\t\t{self.daal.get()}\t\t{self.g_d_p}")

            if self.wheat.get() != 0:
                self.txtarea.insert(END, f"\n Wheat\t\t{self.wheat.get()}\t\t{self.g_w_p}")

            if self.sugar.get() != 0:
                self.txtarea.insert(END, f"\n Sugar\t\t{self.sugar.get()}\t\t{self.g_s_p}")

            if self.tea.get() != 0:
                self.txtarea.insert(END, f"\n Tea\t\t{self.tea.get()}\t\t{self.g_t_p}")

            #========drink price===========


            if self.maaza.get() != 0:
                self.txtarea.insert(END, f"\n Maaza\t\t{self.maaza.get()}\t\t{self.d_m_p}")

            if self.coca_cola.get() != 0:
                self.txtarea.insert(END, f"\n Coca Cola\t\t{self.coca_cola.get()}\t\t{self.d_c_p}")

            if self.frooti.get() != 0:
                self.txtarea.insert(END, f"\n Frooti\t\t{self.frooti.get()}\t\t{self.d_f_p}")

            if self.thums_up.get() != 0:
                self.txtarea.insert(END, f"\n Thums Up\t\t{self.thums_up.get()}\t\t{self.d_t_p}")

            if self.sprite.get() != 0:
                self.txtarea.insert(END, f"\n Sprite\t\t{self.sprite.get()}\t\t{self.d_s_p}")

            if self.limca.get() != 0:
                self.txtarea.insert(END, f"\n Limca\t\t{self.limca.get()}\t\t{self.d_l_p}")

            self.txtarea.insert(END, f"\n ------------------------------------")
            if self.cosmetic_tax.get()!="Rs.0.0":
                self.txtarea.insert(END, f"\n Cosmetic Tax\t\t\t{self.cosmetic_tax.get()}")

            if self.grocery_tax.get()!="Rs.0.0":
                self.txtarea.insert(END, f"\n Grocery Tax\t\t\t{self.grocery_tax.get()}")

            if self.drinks_tax.get()!="Rs.0.0":
                self.txtarea.insert(END, f"\n Drinks Tax\t\t\t{self.drinks_tax.get()}")

            self.txtarea.insert(END, f"\n ------------------------------------")
            self.txtarea.insert(END, f"\n Total Amount\t\t\t Rs.{self.total_bill}")
            self.txtarea.insert(END, f"\n Amount Received\t\t\t Rs.{self.amre}")
            self.txtarea.insert(END, f"\n Change\t\t\t Rs.{self.amount_received}")
            self.txtarea.insert(END, f"\n ------------------------------------")
            self.save_bill()

    def save_bill(self):
        op=messagebox.askyesno("Save Bill","Do you want to save the bill")
        if op>0:
            self.bill_data=self.txtarea.get(1.0, END)
            f1=open("bills/"+str(self.bill_no.get())+".txt","w")
            f1.write(self.bill_data)
            f1.close()
            messagebox.showinfo("Saved", f"Bill no. {self.bill_no.get()} saved successfully")
        else:
            return


    def clear_data(self):

        op = messagebox.askyesno("Clear", "Do you really want to clear?")
        if op > 0:

            self.soap.set(0)
            self.face_cream.set(0)
            self.face_wash.set(0)
            self.hair_spray.set(0)
            self.body_lotion.set(0)
            self.hair_gel.set(0)
            # ==============Grocery=============
            self.tea.set(0)
            self.rice.set(0)
            self.food_oil.set(0)
            self.daal.set(0)
            self.wheat.set(0)
            self.sugar.set(0)
            # ==========drinks==============
            self.maaza.set(0)
            self.coca_cola.set(0)
            self.frooti.set(0)
            self.thums_up.set(0)
            self.sprite.set(0)
            self.limca.set(0)
            # ================total product price and tax variable==============
            self.cosmetic_price.set("")
            self.grocery_price.set("")
            self.drink_price.set("")

            self.cosmetic_tax.set("")
            self.grocery_tax.set("")
            self.drinks_tax.set("")

            # ================customer==============
            self.c_name.set("")
            self.c_phon.set("")
            self.bill_no .set("")
            x = random.randint(100000000, 999999999)
            self.bill_no.set(str(x))
            self.cus_address.set("")

            self.welcome_bill()

    def exit_app(self):
        op=messagebox.askyesno("Exit", "Do you really want to exit?")
        if op>0:
            self.root.destroy()


root = Tk()
obj= Bill_App(root)
root.mainloop()
