from customtkinter import *
from currency_converter import *
from tkinter import *
from PIL import Image
from CTkScrollableDropdown import CTkScrollableDropdown


set_appearance_mode("dark")
set_default_color_theme('dark-blue')
c=CurrencyConverter()


n=1            # for currency converter
frm=""         # for currency converter
mode="dark"
input_num=""   # for calculator


#  calculator functions start

def valu_input(val):
    input_box.configure(state="normal")
    global input_num
    input_num += str(val)
    input_box.delete(1.0,"end")
    input_box.insert(1.0,input_num)
    input_box.configure(state="disabled")


def calculation():
    global input_num
    try:
        input_num = str(eval(input_num))
        input_box.configure(state="normal")
        input_box.delete(1.0,"end")
        input_box.insert(1.0,input_num)
        input_box.configure(state="disabled")
    except:
        clear()
        input_box.configure(state="normal")
        input_box.insert(1.0,"Error")
        input_box.configure(state="disabled")


def clear():
    global input_num
    input_num = ""
    input_box.configure(state="normal")
    input_box.delete(1.0,"end")
    input_box.configure(state="disabled")

#   calculator functions end



# currency convator functions start

def change_mode():
    global mode
    if mode == "dark":
        mode_change_btn.configure(text="D",
                                  text_color="white",
                                  fg_color="black",
                                  hover_color="gray")
        set_appearance_mode("light")
        calculator_fram.configure(fg_color="white")
        input_box.configure(fg_color="white", text_color="black")

        windo.configure(fg_color="white")
        to_lable.configure(fg_color="white")
        exchange_btn.configure(fg_color="transparent",
                               hover_color="white",
                               image=exc_btn_img_black)
        to_lable_extra.configure(fg_color="#979da2")
        mode ="light"

    elif mode == "light":
        mode_change_btn.configure(text="L",
                                  text_color="black",
                                  fg_color="white",
                                  hover_color="gray")
        set_appearance_mode("dark")
        to_lable.configure(fg_color="#3A3B3C")
        exchange_btn.configure(fg_color="transparent",
                               hover_color="black",
                               image=exc_btn_img_white)
        calculator_fram.configure(fg_color="black")
        input_box.configure(fg_color="black", text_color="white")
        windo.configure(fg_color="black")
        mode ="dark"
    

def exc_btn():
    form=from_convart_box.get()
    too=to_convart_box.get()
    from_convart_box.set(too)
    to_convart_box.set(form)

def convaercurrency():
    global n, frm
    try:
        n=int(from_lable.get())
    except:
        n=0
    frm = from_convart_box.get()
    to = to_convart_box.get()
    try:
        ans=c.convert(n,frm,to)
        ans= round(ans,2)
        to_lable.configure(text=str(ans))
    except:
        if frm =='BDT' or to == 'BDT':
            if to == 'BDT' and frm != 'BDT':
                bdt = c.convert(n,frm)
                bdt = bdt*131.84                                          #change with the current valu EUR to BDT
                bdt= round(bdt,2)
                to_lable.configure(text=str(bdt))
            elif frm == 'BDT' and to != 'BDT':
                bdt = c.convert(n,'USD',to)
                bdt = bdt/121.47                                          #change with the current valu USD to BDT
                bdt= round(bdt,2)
                to_lable.configure(text=str(bdt))
            else:
                to_lable.configure(text=n)
        else:
            to_lable.configure(text="Error")

# currency convator functions end



main_windo = CTk()                                                                 # main window
main_windo.geometry("500x600")

mode_change_btn=CTkButton(main_windo,
                          text="L",
                          text_color="black",
                          fg_color="white",
                          hover_color="gray",
                          command=change_mode,
                          width=30,
                          height=30,
                          font=("Helvetica",12,"bold"))
mode_change_btn.place(x=468,y=10)

main_tab = CTkTabview(main_windo, width=430, height=500)                           # main tab
main_tab.pack()




calculator_tab = main_tab.add("Calculator")
currency_converter_tab = main_tab.add("Currency Converter")
unit_converter_tab = main_tab.add("Unit Converter")



reposition_calculater_frame = CTkFrame(calculator_tab, )                                          # calculator start
reposition_calculater_frame.pack()



calculator_fram = CTkFrame(reposition_calculater_frame, fg_color="black")
calculator_fram.pack(side="top", expand=True, fill="both")

input_box = CTkTextbox(calculator_fram, height=70,width=300, state="disabled", fg_color="black",font=("Helvetica",38,"bold"), text_color="white")
input_box.grid(columnspan=5, pady=10,padx=10)


num_c = CTkButton(calculator_fram, width=60, height=60 ,font=("Helvetica",16,"bold"), text="C", command=clear)
num_c.grid(row=1, column=1, padx=5, pady=5)
num_open_brackt = CTkButton(calculator_fram, width=60, height=60 ,font=("Helvetica",16,"bold"), text="(",command=lambda :valu_input("("))
num_open_brackt.grid(row=1, column=2, padx=5, pady=5)
num_close_brackt = CTkButton(calculator_fram, width=60, height=60 ,font=("Helvetica",16,"bold"), text=")",command=lambda :valu_input(")"))
num_close_brackt.grid(row=1, column=3, padx=5, pady=5)

num_1 = CTkButton(calculator_fram, width=60, height=60 ,font=("Helvetica",16,"bold"), text="1",command=lambda: valu_input("1"))
num_1.grid(row=2, column=1, padx=5, pady=5)
num_2 = CTkButton(calculator_fram, width=60, height=60,font=("Helvetica",16,"bold"), text="2",command=lambda: valu_input("2"))
num_2.grid(row=2, column=2, padx=5, pady=5)
num_3 = CTkButton(calculator_fram, width=60, height=60,font=("Helvetica",16,"bold"), text="3",command=lambda: valu_input("3"))
num_3.grid(row=2, column=3, padx=5, pady=5)
num_4 = CTkButton(calculator_fram, width=60, height=60,font=("Helvetica",16,"bold"), text="4",command=lambda: valu_input("4"))
num_4.grid(row=3, column=1, padx=5, pady=5)
num_5 = CTkButton(calculator_fram, width=60, height=60,font=("Helvetica",16,"bold"), text="5",command=lambda: valu_input("5"))
num_5.grid(row=3, column=2, padx=5, pady=5)
num_6 = CTkButton(calculator_fram, width=60, height=60,font=("Helvetica",16,"bold"), text="6",command=lambda: valu_input("6"))
num_6.grid(row=3, column=3, padx=5, pady=5)
num_7 = CTkButton(calculator_fram, width=60, height=60,font=("Helvetica",16,"bold"), text="7",command=lambda: valu_input("7"))
num_7.grid(row=4, column=1, padx=5, pady=5)
num_8 = CTkButton(calculator_fram, width=60, height=60,font=("Helvetica",16,"bold"), text="8",command=lambda: valu_input("8"))
num_8.grid(row=4, column=2, padx=5, pady=5)
num_9 = CTkButton(calculator_fram, width=60, height=60,font=("Helvetica",16,"bold"), text="9",command=lambda: valu_input("9"))
num_9.grid(row=4, column=3, padx=5, pady=5)
num_0 = CTkButton(calculator_fram, width=60, height=60,font=("Helvetica",16,"bold"), text="0",command=lambda: valu_input("0"))
num_0.grid(row=5, column=2, padx=5, pady=5)
num_0 = CTkButton(calculator_fram, width=60, height=60,font=("Helvetica",16,"bold"), text=".",command=lambda: valu_input("."))
num_0.grid(row=5, column=1, padx=5, pady=5)
num_eq = CTkButton(calculator_fram, width=60, height=60,font=("Helvetica",16,"bold"), text="=",command=calculation)
num_eq.grid(row=5, column=3, padx=5, pady=5)

num_plus = CTkButton(calculator_fram, width=60, height=130,font=("Helvetica",16,"bold"), text="+",command=lambda: valu_input("+"))
num_plus.grid(row=4, column=4,rowspan=2, padx=5, pady=5)
num_minus = CTkButton(calculator_fram, width=60, height=60,font=("Helvetica",24,"bold"), text="-",command=lambda: valu_input("-"))
num_minus.grid(row=3, column=4, padx=5, pady=5)
num_mul = CTkButton(calculator_fram, width=60, height=60,font=("Helvetica",24,"bold"), text="*",command=lambda: valu_input("*"))
num_mul.grid(row=2, column=4, padx=5, pady=5)
num_div = CTkButton(calculator_fram, width=60, height=60,font=("Helvetica",16,"bold"), text="/",command=lambda: valu_input("/"))
num_div.grid(row=1, column=4, padx=5, pady=5)



# back_calculator_btn = CTkButton(calculator_fram,width=10, height=10,corner_radius=50, text="<", command=calculator_fram.destroy)
# back_calculator_btn.place(x=0,y=0)
# home_calculator_btn = CTkButton(calculate_windo,width=1, text="Home", bg_color="transparent", fg_color="transparent")
# home_calculator_btn.place(x=140, y=460)

 
                                                                                                # calculator end


# currency convator start


currency_converter_frame = CTkFrame(currency_converter_tab )
currency_converter_frame.pack(fill="both", expand=True, side="top")

windo = CTkFrame(currency_converter_frame, fg_color="black")
windo.pack(fill="both", expand=True, side="top")


exc_btn_img_black = CTkImage(light_image=Image.open('image/logo black.png'),
                       dark_image=Image.open('image/logo black.png'),
                       size=(33,33))
exc_btn_img_white = CTkImage(light_image=Image.open('image/logo white.png'),
                       dark_image=Image.open('image/logo white.png'),
                       size=(33,33))

titel_leble=CTkLabel(windo,
                     text="Currency Converter",
                     font=("Helvetica",22,"bold"))
titel_leble.pack(pady=10)

from_leble=CTkLabel(windo,
                     text="FROM",
                     font=("Helvetica",16,"bold"))
from_leble.place(x=45,y=55)

to_leble=CTkLabel(windo,
                     text="TO",
                     font=("Helvetica",16,"bold"))
to_leble.place(x=255,y=55)

exchange_btn=CTkButton(windo,
                       width=20,
                       height=20,
                       border_spacing=0,
                       border_width=0,
                       corner_radius=5,
                       text="",
                       hover_color="#1a1a1a",
                       bg_color="transparent",
                       fg_color="transparent",
                       image=exc_btn_img_white,
                       command=exc_btn)
exchange_btn.place(x=192,y=81)

cuntry = [
    "BDT", "USD", "JPY", "BGN", "CZK", "DKK", "GBP", "HUF", "PLN", "RON", "SEK", "CHF", 
    "ISK", "NOK", "TRY", "AUD", "BRL", "CAD", "CNY", "HKD", "IDR", "ILS", "INR", "KRW", 
    "MXN", "MYR", "NZD", "PHP", "SGD", "THB", "ZAR"
]

from_convart_box= CTkComboBox(windo,
                              values=cuntry,
                              justify='center',
                              font=("Helvetica",14,"bold"),)
from_convart_box.place(x=40,y=85)
from_box_deopdown = CTkScrollableDropdown(from_convart_box, values=cuntry)

to_convart_box=CTkComboBox(windo,
                           values=cuntry,
                           justify='center',
                           font=("Helvetica",14,"bold"))
to_convart_box.place(x=250,y=85)
to_box_deopdown = CTkScrollableDropdown(to_convart_box, values=cuntry)

from_lable=CTkEntry(windo,
                    font=("Helvetica",14, "bold"),
                    placeholder_text="Enter Amount",
                    justify='center')
from_lable.place(x=40,y=130)

to_lable_extra = CTkLabel(windo, text="", corner_radius=5, fg_color="#565b5e", bg_color="transparent", height=28, width=140)
to_lable_extra.place(x=250,y=130)

to_lable=CTkLabel(windo,
                  text="0",
                  justify="center",
                  width=135,
                  height=23,
                  corner_radius=7,
                  fg_color="#343638",
                  bg_color="#343638",
                  font=("Helvetica",14, "bold"),)
to_lable.place(x=252,y=132)


convart_btn=CTkButton(windo,
                      text="Convert",
                      font=("Helvetica",14, "bold"),
                      command=convaercurrency)
convart_btn.place(x=150,y=180)



main_windo.mainloop()