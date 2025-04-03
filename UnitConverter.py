from customtkinter import *
from CTkScrollableDropdown import CTkScrollableDropdown


root =CTk()

root.geometry("450x500")

root.title("Unit Calculator")



unit_converter_frame = CTkFrame(root)
unit_converter_frame.pack(fill="both", expand=True)


btn_frame = CTkFrame(unit_converter_frame, fg_color="transparent", width=120, height=500)
btn_frame.pack(fill="both", expand=True, side="left")

converter_frame = CTkFrame(unit_converter_frame, fg_color="green", width=280)
converter_frame.pack(fill="both", expand=True, side="right")

# btn_frame_middle = CTkFrame(btn_frame, fg_color="white", width=130)
# btn_frame_middle.place(relx=.5, rely=.5, anchor="center")

btn_frame_middle = CTkFrame(btn_frame,corner_radius=0, fg_color="red")
btn_frame_middle.pack(fill="y", expand=True, side="left",)

btn_frame_middle1 = CTkFrame(btn_frame_middle, fg_color="white", width=100 )
btn_frame_middle1.pack(fill="x", expand=True, side="left")



btn_area = CTkButton(btn_frame_middle1, width=100, text="Area",)
btn_area.pack(padx=20, pady=10, )
btn_length = CTkButton(btn_frame_middle1, width=100, text="Length")
btn_length.pack(padx=20, pady=10,)
btn_temperature = CTkButton(btn_frame_middle1, width=100, text="Temperature")
btn_temperature.pack(padx=20, pady=10,)
btn_time = CTkButton(btn_frame_middle1, width=100, text="Time")
btn_time.pack(padx=20, pady=10,)
btn_volume = CTkButton(btn_frame_middle1, width=100, text="Volume")
btn_volume.pack(padx=20, pady=10,)


converter_frame_middle1 = CTkFrame(converter_frame, fg_color="green", )
converter_frame_middle1.pack(fill="both", expand=True, anchor="center")

titel = CTkLabel(converter_frame_middle1, text="Area", width=120, font=("Helvetica", 30, "bold"), fg_color="black")
titel.place(relx=0.5, rely=0.2, anchor="center")

from_lable = CTkLabel(converter_frame_middle1, text="From", font=("Helvetica", 16, "bold"),)
from_lable.place(relx=0.17, rely=0.34, anchor="center")
to_lable = CTkLabel(converter_frame_middle1, text="To", font=("Helvetica", 16, "bold"),)
to_lable.place(relx=0.64, rely=0.34, anchor="center")


area=['1','2','3','4','5','6','7']
from_combbox = CTkComboBox(converter_frame_middle1, values=area, font=("Helvetica", 16, "bold"), width=100 )
from_combbox.place(relx=0.25, rely=0.4, anchor="center")
from_combbox_deopdown = CTkScrollableDropdown(from_combbox, values=area)


to_combbox = CTkComboBox(converter_frame_middle1, values=area, font=("Helvetica", 16, "bold"), width=100 )
to_combbox.place(relx=0.76, rely=0.4, anchor="center")
to_combbox_deopdown = CTkScrollableDropdown(to_combbox, values=area)


from_in_out_box = CTkEntry(converter_frame_middle1, width=100)
from_in_out_box.place(relx=0.25, rely=0.5, anchor="center")

to_in_out_box = CTkLabel(converter_frame_middle1, width=100, fg_color="gray", text="0")
to_in_out_box.place(relx=0.76, rely=0.5, anchor="center")

btn_convert = CTkButton(converter_frame_middle1, text="Convert", width=120)
btn_convert.place(relx=0.5, rely=0.6, anchor="center")




root.mainloop()