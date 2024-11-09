from tkinter import *
import random
import os
from tkinter import messagebox

# Color Constants
BG_COLOR = "#074463"
TITLE_COLOR = "turquoise"
FRAME_COLOR = "cyan2"
TEXT_COLOR = "#333333"
BUTTON_COLOR = "#4a90e2"
BUTTON_TEXT_COLOR = "#ffffff"

# ============ Main ============================
class Bill_App:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1350x700+0+0")
        self.root.title("Billing Software")
        
        title = Label(self.root, text="Billing Software", font=('times new roman', 30, 'bold'), pady=2, bd=12, bg=TITLE_COLOR, fg=BUTTON_TEXT_COLOR, relief=GROOVE)
        title.pack(fill=X)

        # ================ Variables =======================
        self.sanitizer = IntVar()
        self.mask = IntVar()
        self.hand_gloves = IntVar()
        self.dettol = IntVar()
        self.newsprin = IntVar()
        self.thermal_gun = IntVar()

        self.rice = IntVar()
        self.food_oil = IntVar()
        self.wheat = IntVar()
        self.daal = IntVar()
        self.flour = IntVar()
        self.maggi = IntVar()

        self.sprite = IntVar()
        self.limka = IntVar()
        self.mazza = IntVar()
        self.coke = IntVar()
        self.fanta = IntVar()
        self.mountain_duo = IntVar()

        self.medical_price = StringVar()
        self.grocery_price = StringVar()
        self.cold_drinks_price = StringVar()
        self.c_name = StringVar()
        self.c_phone = StringVar()
        self.bill_no = StringVar()
        x = random.randint(1000, 9999)
        self.bill_no.set(str(x))
        self.search_bill = StringVar()
        
        self.medical_tax = StringVar()
        self.grocery_tax = StringVar()
        self.cold_drinks_tax = StringVar()

        # ============= Customer Details ====================
        self.create_customer_frame()

        # ============== Medical Items ======================
        self.create_medical_frame()

        # ========== Grocery Items ===========================
        self.create_grocery_frame()

        # =========== Cold Drinks ============================
        self.create_cold_drinks_frame()

        # ================= Bill Area =======================
        self.create_bill_area()

        # ================= Button Frame =====================
        self.create_button_frame()

        self.welcome_bill()

    def create_customer_frame(self):
        F1 = LabelFrame(self.root, text="Customer Details", font=('times new roman', 15, 'bold'), bd=10, fg=TEXT_COLOR, bg=FRAME_COLOR)
        F1.place(x=0, y=80, relwidth=1)

        cname_lbl = Label(F1, text="Customer Name:", bg=FRAME_COLOR, font=('times new roman', 15, 'bold'))
        cname_lbl.grid(row=0, column=0, padx=20, pady=5)
        cname_txt = Entry(F1, width=15, textvariable=self.c_name, font='arial 15', bd=7, relief=GROOVE)
        cname_txt.grid(row=0, column=1, pady=5, padx=10)

        cphn_lbl = Label(F1, text="Customer Phone:", bg=FRAME_COLOR, font=('times new roman', 15, 'bold'))
        cphn_lbl.grid(row=0, column=2, padx=20, pady=5)
        cphn_txt = Entry(F1, width=15, textvariable=self.c_phone, font='arial 15', bd=7, relief=GROOVE)
        cphn_txt.grid(row=0, column=3, pady=5, padx=10)

        c_bill_lbl = Label(F1, text="Bill Number:", bg=FRAME_COLOR, font=('times new roman', 15, 'bold'))
        c_bill_lbl.grid(row=0, column=4, padx=20, pady=5)
        c_bill_txt = Entry(F1, width=15, textvariable=self.search_bill, font='arial 15', bd=7, relief=GROOVE)
        c_bill_txt.grid(row=0, column=5, pady=5, padx=10)

        bil_btn = Button(F1, text="Search", command=self.find_bill, width=10, bd=7, font=('arial', 12, 'bold'), relief=GROOVE, bg=BUTTON_COLOR, fg=BUTTON_TEXT_COLOR)
        bil_btn.grid(row=0, column=6, pady=5, padx=10)

    def create_medical_frame(self):
        F2 = LabelFrame(self.root, text="Medical Purpose", font=('times new roman', 15, 'bold'), bd=10, fg=TEXT_COLOR, bg=FRAME_COLOR)
        F2.place(x=5, y=180, width=325, height=380)

        items = [("Sanitizer", self.sanitizer), ("Mask", self.mask), ("Hand Gloves", self.hand_gloves), 
                 ("Dettol", self.dettol), ("Newsprin", self.newsprin), ("Thermal Gun", self.thermal_gun)]
        
        for i, (text, var) in enumerate(items):
            lbl = Label(F2, text=text, font=('times new roman', 16, 'bold'), bg=FRAME_COLOR, fg=TEXT_COLOR)
            lbl.grid(row=i, column=0, padx=10, pady=10, sticky='W')
            txt = Entry(F2, width=10, textvariable=var, font=('times new roman', 16, 'bold'), bd=5, relief=GROOVE)
            txt.grid(row=i, column=1, padx=10, pady=10)

    def create_grocery_frame(self):
        F3 = LabelFrame(self.root, text="Grocery Items", font=('times new roman', 15, 'bold'), bd=10, fg=TEXT_COLOR, bg=FRAME_COLOR)
        F3.place(x=340, y=180, width=325, height=380)

        items = [("Rice", self.rice), ("Food Oil", self.food_oil), ("Wheat", self.wheat), 
                 ("Daal", self.daal), ("Flour", self.flour), ("Maggi", self.maggi)]
        
        for i, (text, var) in enumerate(items):
            lbl = Label(F3, text=text, font=('times new roman', 16, 'bold'), bg=FRAME_COLOR, fg=TEXT_COLOR)
            lbl.grid(row=i, column=0, padx=10, pady=10, sticky='W')
            txt = Entry(F3, width=10, textvariable=var, font=('times new roman', 16, 'bold'), bd=5, relief=GROOVE)
            txt.grid(row=i, column=1, padx=10, pady=10)

    def create_cold_drinks_frame(self):
        F4 = LabelFrame(self.root, text="Cold Drinks", font=('times new roman', 15, 'bold'), bd=10, fg=TEXT_COLOR, bg=FRAME_COLOR)
        F4.place(x=670, y=180, width=325, height=380)

        items = [("Sprite", self.sprite), ("Limka", self.limka), ("Mazza", self.mazza), 
                 ("Coke", self.coke), ("Fanta", self.fanta), ("Mountain Duo", self.mountain_duo)]
        
        for i, (text, var) in enumerate(items):
            lbl = Label(F4, text=text, font=('times new roman', 16, 'bold'), bg=FRAME_COLOR, fg=TEXT_COLOR)
            lbl.grid(row=i, column=0, padx=10, pady=10, sticky='W')
            txt = Entry(F4, width=10, textvariable=var, font=('times new roman', 16, 'bold'), bd=5, relief=GROOVE)
            txt.grid(row=i, column=1, padx=10, pady=10)

    def create_bill_area(self):
        F5 = Frame(self.root, bd=10, relief=GROOVE)
        F5.place(x=1010, y=180, width=350, height=380)

        bill_title = Label(F5, text="Bill Area", font='arial 15 bold', bd=7, relief=GROOVE)
        bill_title.pack(fill=X)
        scroll_y = Scrollbar(F5, orient=VERTICAL)
        self.txtarea = Text(F5, yscrollcommand=scroll_y.set)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_y.config(command=self.txtarea.yview)
        self.txtarea.pack(fill=BOTH, expand=1)

    def create_button_frame(self):
        F6 = LabelFrame(self.root, text="Bill Area", font=('times new roman', 14, 'bold'), bd=10, fg=TEXT_COLOR, bg=FRAME_COLOR)
        F6.place(x=0, y=560, relwidth=1, height=140)

        labels = ["Total Medical Price", "Total Grocery Price", "Total Cold Drinks Price", 
                  "Medical Tax", "Grocery Tax", "Cold Drinks Tax"]
        variables = [self.medical_price, self.grocery_price, self.cold_drinks_price, 
                     self.medical_tax, self.grocery_tax, self.cold_drinks_tax]

        for i, (label, var) in enumerate(zip(labels, variables)):
            lbl = Label(F6, text=label, font=('times new roman', 14, 'bold'), bg=FRAME_COLOR, fg=TEXT_COLOR)
            lbl.grid(row=i // 3, column=(i % 3) * 2, padx=20, pady=1, sticky='W')
            txt = Entry(F6, width=18, textvariable=var, font='arial 10 bold', bd=7, relief=GROOVE)
            txt.grid(row=i // 3, column=(i % 3) * 2 + 1, padx=18, pady=1)

        btn_f = Frame(F6, bd=7, relief=GROOVE)
        btn_f.place(x=760, width=580, height=105)

        buttons = [("Total", self.total), ("Generate Bill", self.bill_area), 
                   ("Clear", self.clear_data), ("Exit", self.exit_app)]
        
        for i, (text, command) in enumerate(buttons):
            btn = Button(btn_f, command=command, text=text, bg=BUTTON_COLOR, bd=2, fg=BUTTON_TEXT_COLOR, pady=15, width=12, font='arial 13 bold')
            btn.grid(row=0, column=i, padx=5, pady=5)

    # ================== Logic Methods =======================

    def total(self):
        # Calculate total prices and taxes
        self.m_h_g_p = self.hand_gloves.get() * 12
        self.m_s_p = self.sanitizer.get() * 2
        self.m_m_p = self.mask.get() * 5
        self.m_d_p = self.dettol.get() * 30
        self.m_n_p = self.newsprin.get() * 5
        self.m_t_g_p = self.thermal_gun.get() * 15
        self.total_medical_price = float(self.m_m_p + self.m_h_g_p + self.m_d_p + self.m_n_p + self.m_t_g_p + self.m_s_p)

        self.medical_price.set("Rs. " + str(self.total_medical_price))
        self.c_tax = round((self.total_medical_price * 0.05), 2)
        self.medical_tax.set("Rs. " + str(self.c_tax))

        self.g_r_p = self.rice.get() * 10
        self.g_f_o_p = self.food_oil.get() * 10
        self.g_w_p = self.wheat.get() * 10
        self.g_d_p = self.daal.get() * 6
        self.g_f_p = self.flour.get() * 8
        self.g_m_p = self.maggi.get() * 5
        self.total_grocery_price = float(self.g_r_p + self.g_f_o_p + self.g_w_p + self.g_d_p + self.g_f_p + self.g_m_p)

        self.grocery_price.set("Rs. " + str(self.total_grocery_price))
        self.g_tax = round((self.total_grocery_price * 0.05), 2)
        self.grocery_tax.set("Rs. " + str(self.g_tax))

        self.c_d_s_p = self.sprite.get() * 10
        self.c_d_l_p = self.limka.get() * 10
        self.c_d_m_p = self.mazza.get() * 10
        self.c_d_c_p = self.coke.get() * 10
        self.c_d_f_p = self.fanta.get() * 10
        self.c_m_d = self.mountain_duo.get() * 10
        self.total_cold_drinks_price = float(self.c_d_s_p + self.c_d_l_p + self.c_d_m_p + self.c_d_c_p + self.c_d_f_p + self.c_m_d)

        self.cold_drinks_price.set("Rs. " + str(self.total_cold_drinks_price))
        self.c_d_tax = round((self.total_cold_drinks_price * 0.1), 2)
        self.cold_drinks_tax.set("Rs." + str(self.c_d_tax))

        self.total_bill = float(self.total_medical_price + self.total_grocery_price + self.total_cold_drinks_price + self.c_tax + self.g_tax + self.c_d_tax)

    def welcome_bill(self):
        self.txtarea.delete('1.0', END)
        self.txtarea.insert(END, "\tWelcome to Webcode Retail")
        self.txtarea.insert(END, f"\n Bill Number: {self.bill_no.get()}")
        self.txtarea.insert(END, f"\n Customer Name: {self.c_name.get()}")
        self.txtarea.insert(END, f"\n Phone Number: {self.c_phone.get()}")
        self.txtarea.insert(END, f"\n================================")
        self.txtarea.insert(END, f"\n Products\t\tQTY\t\tPrice")

    def bill_area(self):
        if self.c_name.get() == "" or self.c_phone.get() == "":
            messagebox.showerror("Error", "Customer Details Are Must")
        elif self.medical_price.get() == "Rs. 0.0" and self.grocery_price.get() == "Rs. 0.0" and self.cold_drinks_price.get() == "Rs. 0.0":
            messagebox.showerror("Error", "No Product Purchased")
        else:
            self.welcome_bill()
            # Medical items
            if self.sanitizer.get() != 0:
                self.txtarea.insert(END, f"\n Sanitizer\t\t{self.sanitizer.get()}\t\t{self.m_s_p}")
            if self.mask.get() != 0:
                self.txtarea.insert(END, f"\n Mask\t\t{self.mask.get()}\t\t{self.m_m_p}")
            if self.hand_gloves.get() != 0:
                self.txtarea.insert(END, f"\n Hand Gloves\t\t{self.hand_gloves.get()}\t\t{self.m_h_g_p}")
            if self.dettol.get() != 0:
                self.txtarea.insert(END, f"\n Dettol\t\t{self.dettol.get()}\t\t{self.m_d_p}")
            if self.newsprin.get() != 0:
                self.txtarea.insert(END, f"\n Newsprin\t\t{self.newsprin.get()}\t\t{self.m_n_p}")
            if self.thermal_gun.get() != 0:
                self.txtarea.insert(END, f"\n Thermal Gun\t\t{self.thermal_gun.get()}\t\t{self.m_t_g_p}")

            # Grocery items
            if self.rice.get() != 0:
                self.txtarea.insert(END, f"\n Rice\t\t{self.rice.get()}\t\t{self.g_r_p}")
            if self.food_oil.get() != 0:
                self.txtarea.insert(END, f"\n Food Oil\t\t{self.food_oil.get()}\t\t{self.g_f_o_p}")
            if self.wheat.get() != 0:
                self.txtarea.insert(END, f"\n Wheat\t\t{self.wheat.get()}\t\t{self.g_w_p}")
            if self.daal.get() != 0:
                self.txtarea.insert(END, f"\n Daal\t\t{self.daal.get()}\t\t{self.g_d_p}")
            if self.flour.get() != 0:
                self.txtarea.insert(END, f"\n Flour\t\t{self.flour.get()}\t\t{self.g_f_p}")
            if self.maggi.get() != 0:
                self.txtarea.insert(END, f"\n Maggi\t\t{self.maggi.get()}\t\t{self.g_m_p}")

            # Cold drinks
            if self.sprite.get() != 0:
                self.txtarea.insert(END, f"\n Sprite\t\t{self.sprite.get()}\t\t{self.c_d_s_p}")
            if self.limka.get() != 0:
                self.txtarea.insert(END, f"\n Limka\t\t{self.limka.get()}\t\t{self.c_d_l_p}")
            if self.mazza.get() != 0:
                self.txtarea.insert(END, f"\n Mazza\t\t{self.mazza.get()}\t\t{self.c_d_m_p}")
            if self.coke.get() != 0:
                self.txtarea.insert(END, f"\n Coke\t\t{self.coke.get()}\t\t{self.c_d_c_p}")
            if self.fanta.get() != 0:
                self.txtarea.insert(END, f"\n Fanta\t\t{self.fanta.get()}\t\t{self.c_d_f_p}")
            if self.mountain_duo.get() != 0:
                self.txtarea.insert(END, f"\n Mountain Duo\t\t{self.mountain_duo.get()}\t\t{self.c_m_d}")

            self.txtarea.insert(END, f"\n--------------------------------")
            # Taxes
            if self.medical_tax.get() != '0.0':
                self.txtarea.insert(END, f"\n Medical Tax\t\t\t{self.medical_tax.get()}")
            if self.grocery_tax.get() != '0.0':
                self.txtarea.insert(END, f"\n Grocery Tax\t\t\t{self.grocery_tax.get()}")
            if self.cold_drinks_tax.get() != '0.0':
                self.txtarea.insert(END, f"\n Cold Drinks Tax\t\t\t{self.cold_drinks_tax.get()}")

            self.txtarea.insert(END, f"\n Total Bill:\t\t\t Rs.{self.total_bill}")
            self.txtarea.insert(END, f"\n--------------------------------")
            self.save_bill()

    def save_bill(self):
        op = messagebox.askyesno("Save Bill", "Do you want to save the bill?")
        if op > 0:
            self.bill_data = self.txtarea.get('1.0', END)
            if not os.path.exists("bills"):
                os.makedirs("bills")
            with open(f"bills/{self.bill_no.get()}.txt", "w") as f1:
                f1.write(self.bill_data)
            messagebox.showinfo("Saved", f"Bill no: {self.bill_no.get()} Saved Successfully")

    def find_bill(self):
        present = "no"
        for i in os.listdir("bills/"):
            if i.split('.')[0] == self.search_bill.get():
                with open(f"bills/{i}", "r") as f1:
                    self.txtarea.delete("1.0", END)
                    for d in f1:
                        self.txtarea.insert(END, d)
                present = "yes"
        if present == "no":
            messagebox.showerror("Error", "Invalid Bill No")

    def clear_data(self):
        op = messagebox.askyesno("Clear", "Do you really want to Clear?")
        if op > 0:
            # Reset all IntVar variables
            for var in [self.sanitizer, self.mask, self.hand_gloves, self.dettol, self.newsprin, self.thermal_gun,
                         self.rice, self.food_oil, self.wheat, self.daal, self.flour, self.maggi,
                         self.sprite, self.limka, self.mazza, self.coke, self.fanta, self.mountain_duo]:
                var.set(0)

            # Reset all StringVar variables
            for var in [self.medical_price, self.grocery_price, self.cold_drinks_price,
                         self.medical_tax, self.grocery_tax, self.cold_drinks_tax,
                         self.c_name, self.c_phone, self.search_bill]:
                var.set("")

            # Reset bill number
            self.bill_no.set(str(random.randint(1000, 9999)))
            self.welcome_bill()

    def exit_app(self):
        op = messagebox.askyesno("Exit", "Do you really want to exit?")
        if op > 0:
            self.root.destroy()

# Run the application
root = Tk()
obj = Bill_App(root)
root.mainloop()
