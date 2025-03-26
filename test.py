import customtkinter as ctk
from PIL import Image

# Initialize CustomTkinter
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

# Create Main Window
root = ctk.CTk()
root.geometry("500x400")
root.title("Tabview with Different Icons")

# Load Different Icons for Each Tab
icon1 = ctk.CTkImage(light_image=Image.open("image/calculator.png"), size=(20, 20))  # Tab 1 icon
icon2 = ctk.CTkImage(light_image=Image.open("image/exchange.png"), size=(20, 20))  # Tab 2 icon
icon3 = ctk.CTkImage(light_image=Image.open("image/unit-1png.png"), size=(20, 20))  # Tab 3 icon

# Load Selected Icons (When Tab is Clicked)
icon1_selected = ctk.CTkImage(light_image=Image.open("image/calculator.png"), size=(20, 20))
icon2_selected = ctk.CTkImage(light_image=Image.open("image/exchange.png"), size=(20, 20))
icon3_selected = ctk.CTkImage(light_image=Image.open("image/unit-1png.png"), size=(20, 20))

# Create Tabview
main_tab = ctk.CTkTabview(root)
main_tab.pack(pady=20, padx=20, fill="both", expand=True)

tab_names = ["Calculator", "Currency Converter", "Unit Converter"]  # Tab Names
# Tab Names
calculator_tab = main_tab.add("Calculator")
currency_converter_tab = main_tab.add("Currency Converter")
unit_converter_tab = main_tab.add("Unit Converter")


# Add Content to Tabs
# for i, tab in enumerate(tab_names):
tab_1 = ctk.CTkLabel(calculator_tab, text=f"This is calculator").pack(pady=10)
tab_2 = ctk.CTkLabel(currency_converter_tab, text=f"This is currency").pack(pady=10)
tab_3 = ctk.CTkLabel(unit_converter_tab, text=f"This is unit").pack(pady=10)

# Get Button Dictionary
buttons = main_tab._segmented_button._buttons_dict

# Initial Icon Setup (3 Different Icons)
icons = [icon1, icon2, icon3]  # Initial icons for each tab
selected_icons = [icon1_selected, icon2_selected, icon3_selected]  # Selected icons
for i, (name, btn) in enumerate(buttons.items()):
    btn.configure(text=" ", image=icons[i]) 
 # Set individual icons at start



for j, (name, btn) in enumerate(buttons.items()):
    if j == 0:
        btn.configure(text=tab_names[j], image=selected_icons[j])  # Show text + new icon
    else:
        btn.configure(text=" ", image=icons[j])


# Function to Update Tabs
def update_tabs(selected_index):
    main_tab.set(tab_names[selected_index])

    for i, (name, btn) in enumerate(buttons.items()):
        if i == selected_index:
            btn.configure(text=tab_names[i], image=selected_icons[i])
              # Show text + new icon
        else:
            btn.configure(text=" ", image=icons[i])  # Show only original icon

# Bind Click Events to Tabs
for i, btn in enumerate(buttons.values()):
    btn.configure(command=lambda idx=i: update_tabs(idx))

# Run the App
root.mainloop()
