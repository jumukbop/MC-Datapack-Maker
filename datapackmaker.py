import os
from tkinter import *
from tkinter import filedialog, messagebox

# Define the datapack folder
datapack_folder = ""

# Define the main window
root = Tk()
root.title("Minecraft Datapack Maker")

# Define function to browse for datapack folder
def browse_folder():
    global datapack_folder
    datapack_folder = filedialog.askdirectory()
    datapack_folder_label.config(text=datapack_folder)

# Define function to create scoreboard objective
def create_objective():
    objective_name = objective_entry.get()
    os.system(f"minecraft/scoreboard objectives add {objective_name} dummy")

    messagebox.showinfo("Success", f"Scoreboard objective '{objective_name}' created successfully.")

# Define function to create function file
def create_function():
    function_name = function_entry.get()
    function_command = command_entry.get()

    # Create the function directory if it doesn't exist
    if not os.path.exists(f"{datapack_folder}/data/minecraft/functions"):
        os.makedirs(f"{datapack_folder}/data/minecraft/functions")

    # Create the function file
    with open(f"{datapack_folder}/data/minecraft/functions/{function_name}.mcfunction", "w") as f:
        f.write(function_command)

    messagebox.showinfo("Success", f"Function '{function_name}' created successfully.")

# Define function to create advancement
def create_advancement():
    advancement_name = advancement_entry.get()
    trigger_name = trigger_entry.get()
    os.system(f"minecraft/advancement grant @s only minecraft:{advancement_name}/{trigger_name}")

    messagebox.showinfo("Success", f"Advancement trigger '{trigger_name}' created successfully.")

# Define function to create loot table
def create_loot_table():
    loot_table_name = loot_table_entry.get()
    loot_table_json = loot_table_json_entry.get("1.0", END)

    # Create the loot_tables directory if it doesn't exist
    if not os.path.exists(f"{datapack_folder}/data/minecraft/loot_tables"):
        os.makedirs(f"{datapack_folder}/data/minecraft/loot_tables")

    # Create the loot table file
    with open(f"{datapack_folder}/data/minecraft/loot_tables/{loot_table_name}.json", "w") as f:
        f.write(loot_table_json)

    messagebox.showinfo("Success", f"Loot table '{loot_table_name}' created successfully.")

# Define function to create recipe
def create_recipe():
    recipe_name = recipe_entry.get()
    recipe_type = recipe_type_entry.get()
    recipe_json = recipe_json_entry.get("1.0", END)

    # Create the recipes directory if it doesn't exist
    if not os.path.exists(f"{datapack_folder}/data/minecraft/recipes"):
        os.makedirs(f"{datapack_folder}/data/minecraft/recipes")

    # Create the recipe file
    with open(f"{datapack_folder}/data/minecraft/recipes/{recipe_name}.json", "w") as f:
        f.write(recipe_json)

    messagebox.showinfo("Success", f"Recipe '{recipe_name}' created successfully.")

# Define function to create tag
def create_tag():
    tag_name = tag_entry.get()
    tag_type = tag_type_entry.get()

    # Create the tags directory if it doesn't exist
    if not os.path.exists(f"{datapack_folder}/data/minecraft/tags"):
        os.makedirs(f"{datapack_folder}/data/minecraft/tags")

    # Create the tag file
    with open(f"{datapack_folder}/data/minecraft/tags/{tag_type}/{tag_name}.json", "w") as f:
        f.write(f'{{"replace":false,"values":["minecraft:{tag_name}"]}}')

    messagebox.showinfo("Success", f"Tag '{tag_name}' created successfully.")

# Define function to clear scoreboard objective
def clear_objective():
    objective_name = objective_entry.get()
    os.system(f"minecraft/scoreboard objectives remove {objective_name}")

    messagebox.showinfo("Success", f"Scoreboard objective '{objective_name}' cleared successfully.")

# Define function to clear function file
def clear_function():
    function_name = function_entry.get()

    try:
        os.remove(f"{datapack_folder}/data/minecraft/functions/{function_name}.mcfunction")
        messagebox.showinfo("Success", f"Function '{function_name}' cleared successfully.")
    except FileNotFoundError:
        messagebox.showwarning("File Not Found", f"Function file '{function_name}.mcfunction' not found.")

# Define function to clear advancement
def clear_advancement():
    advancement_name = advancement_entry.get()
    trigger_name = trigger_entry.get()
    os.system(f"minecraft/advancement revoke @s only minecraft:{advancement_name}/{trigger_name}")

    messagebox.showinfo("Success", f"Advancement trigger '{trigger_name}' cleared successfully.")

# Define function to clear loot table
def clear_loot_table():
    loot_table_name = loot_table_entry.get()

    try:
        os.remove(f"{datapack_folder}/data/minecraft/loot_tables/{loot_table_name}.json")
        messagebox.showinfo("Success", f"Loot table '{loot_table_name}' cleared successfully.")
    except FileNotFoundError:
        messagebox.showwarning("File Not Found", f"Loot table file '{loot_table_name}.json' not found.")

# Define function to clear recipe
def clear_recipe():
    recipe_name = recipe_entry.get()

    try:
        os.remove(f"{datapack_folder}/data/minecraft/recipes/{recipe_name}.json")
        messagebox.showinfo("Success", f"Recipe '{recipe_name}' cleared successfully.")
    except FileNotFoundError:
        messagebox.showwarning("File Not Found", f"Recipe file '{recipe_name}.json' not found.")

# Define function to clear tag
def clear_tag():
    tag_name = tag_entry.get()
    tag_type = tag_type_entry.get()

    try:
        os.remove(f"{datapack_folder}/data/minecraft/tags/{tag_type}/{tag_name}.json")
        messagebox.showinfo("Success", f"Tag '{tag_name}' cleared successfully.")
    except FileNotFoundError:
        messagebox.showwarning("File Not Found", f"Tag file '{tag_name}.json' not found.")

# Define function to open datapack folder
def open_folder():
    os.system(f"start {datapack_folder}")

# Define function to close the window
def close_window():
    root.destroy()

# Define the labels for the datapack folder and instructions
datapack_folder_label = Label(root, text="Please select your datapack folder.")
instruction_label = Label(root, text="Fill in the fields below to create or clear datapack components:")

# Define the buttons to browse for the datapack folder and create/clear components
browse_button = Button(root, text="Browse", command=browse_folder)
create_objective_button = Button(root, text="Create Objective", command=create_objective)
create_function_button = Button(root, text="Create Function", command=create_function)
create_advancement_button = Button(root, text="Create Advancement Trigger", command=create_advancement)
create_loot_table_button = Button(root, text="Create Loot Table", command=create_loot_table)
create_recipe_button = Button(root, text="Create Recipe", command=create_recipe)
create_tag_button = Button(root, text="Create    Tag", command=create_tag)
clear_objective_button = Button(root, text="Clear Objective", command=clear_objective)
clear_function_button = Button(root, text="Clear Function", command=clear_function)
clear_advancement_button = Button(root, text="Clear Advancement Trigger", command=clear_advancement)
clear_loot_table_button = Button(root, text="Clear Loot Table", command=clear_loot_table)
clear_recipe_button = Button(root, text="Clear Recipe", command=clear_recipe)
clear_tag_button = Button(root, text="Clear Tag", command=clear_tag)

# Define the labels and entry fields for each component
function_frame = LabelFrame(root, text="Function Maker")
function_frame.grid(row=0, column=0, padx=10, pady=10, sticky="w")

command_entry = Entry(function_frame, width=50)
command_entry.grid(row=1, column=0, padx=10, pady=10)

objective_label = Label(root, text="Objective Name:")
objective_entry = Entry(root)

function_label = Label(root, text="Function Name:")
function_entry = Entry(root)

advancement_label = Label(root, text="Advancement Name:")
advancement_entry = Entry(root)
trigger_label = Label(root, text="Trigger Name:")
trigger_entry = Entry(root)

loot_table_label = Label(root, text="Loot Table Name:")
loot_table_entry = Entry(root)

recipe_label = Label(root, text="Recipe Name:")
recipe_entry = Entry(root)

tag_label = Label(root, text="Tag Name:")
tag_entry = Entry(root)
tag_type_label = Label(root, text="Tag Type:")
tag_type_entry = Entry(root)

# Define the button to open the datapack folder
open_folder_button = Button(root, text="Open Datapack Folder", command=open_folder)

# Define the button to close the window
close_button = Button(root, text="Close", command=close_window)

# Place the labels and entry fields in the grid
datapack_folder_label.grid(row=0, column=0, columnspan=2, padx=10, pady=10)
datapack_folder_var = StringVar()
datapack_folder_entry = Entry(root, width=40, textvariable=datapack_folder_var)
datapack_folder_entry.grid(row=2, column=1, padx=10, pady=10)
browse_button.grid(row=1, column=1, padx=10, pady=10)

instruction_label.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

objective_label.grid(row=3, column=0, padx=10, pady=10)
objective_entry.grid(row=3, column=1, padx=10, pady=10)
create_objective_button.grid(row=4, column=0, padx=10, pady=10)
clear_objective_button.grid(row=4, column=1, padx=10, pady=10)

function_label.grid(row=5, column=0, padx=10, pady=10)
function_entry.grid(row=5, column=1, padx=10, pady=10)
create_function_button.grid(row=6, column=0, padx=10, pady=10)
clear_function_button.grid(row=6, column=1, padx=10, pady=10)

advancement_label.grid(row=7, column=0, padx=10, pady=10)
advancement_entry.grid(row=7, column=1, padx=10, pady=10)
trigger_label.grid(row=8, column=0, padx=10, pady=10)
trigger_entry.grid(row=8, column=1, padx=10, pady=10)
create_advancement_button.grid(row=9, column=0, padx=10, pady=10)
clear_advancement_button.grid(row=9, column=1, padx=10, pady=10)

loot_table_frame = LabelFrame(root, text="Loot Table Maker")
loot_table_frame.grid(row=0, column=1, padx=10, pady=10, sticky="w")

loot_table_contents_text = Text(loot_table_frame, width=50, height=10)
loot_table_contents_text.grid(row=1, column=0, padx=10, pady=10)

create_loot_table_button = Button(loot_table_frame, text="Create Loot Table", command=create_loot_table)
create_loot_table_button.grid(row=2, column=0, padx=10, pady=10)

clear_loot_table_button = Button(loot_table_frame, text="Clear", command=clear_loot_table)
clear_loot_table_button.grid(row=2, column=1, padx=10, pady=10)

loot_table_name_var = StringVar()
loot_table_name_entry = Entry(loot_table_frame, width=40, textvariable=loot_table_name_var)
loot_table_name_entry.grid(row=3, column=0, padx=10, pady=10)

loot_table_json_var = StringVar()
loot_table_json_entry = Entry(loot_table_frame, width=40, textvariable=loot_table_json_var)
loot_table_json_entry.grid(row=4, column=0, padx=10, pady=10)

loot_table_folder_var = StringVar()
loot_table_folder_entry = Entry(loot_table_frame, width=40, textvariable=loot_table_folder_var)
loot_table_folder_entry.grid(row=5, column=0, padx=10, pady=10)


recipe_label.grid(row=12, column=0, padx=10, pady=10)
recipe_entry.grid(row=12, column=1, padx=10, pady=10)
create_recipe_button.grid(row=13, column=0, padx=10, pady=10)
clear_recipe_button.grid(row=13, column=1, padx=10, pady=10)

recipe_frame = LabelFrame(root, text="Recipe Maker")
recipe_frame.grid(row=0, column=2, padx=10, pady=10, sticky="w")

recipe_type_var = StringVar()
recipe_type_entry = Entry(recipe_frame, width=40, textvariable=recipe_type_var)
recipe_type_entry.grid(row=3, column=0, padx=10, pady=10)

recipe_json_var = StringVar()
recipe_json_entry = Entry(recipe_frame, width=40, textvariable=recipe_json_var)
recipe_json_entry.grid(row=4, column=0, padx=10, pady=10)

tag_label.grid(row=14, column=0, padx=10, pady=10)
tag_entry.grid(row=14, column=1, padx=10, pady=10)
tag_type_label.grid(row=15, column=0, padx=10, pady=10)
tag_type_entry.grid(row=15, column=1, padx=10, pady=10)
create_tag_button.grid(row=16, column=0, padx=10, pady=10)
clear_tag_button.grid(row=16, column=1, padx=10, pady=10)

open_folder_button.grid(row=17, column=0, columnspan=2, padx=10, pady=10)
close_button.grid(row=18, column=0, columnspan=2, padx=10, pady=10)

# Run the tkinter main loop
root.mainloop()
