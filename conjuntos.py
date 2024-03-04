import tkinter as tk
from tkinter import simpledialog, messagebox
from matplotlib import pyplot as plt
from matplotlib_venn import venn2, venn3

title = "Venn Diagram"

# Function to display Venn diagram for two or more sets
def show_venn_diagram(*args):
    
    plt.figure(figsize=(8, 6))
    if len(args) == 1:
        set1 = ', '.join(str(n) for n in difference_of_sets(args[0]))
        venn = venn2((args[0], set()), ('Set A', ''))
        venn.get_label_by_id('10').set_text(set1)
        venn.get_label_by_id('01').set_text('')
    
    if len(args) == 2:
        set1 = ', '.join(str(n) for n in difference_of_sets(args[0], args[1]))
        set2 = ', '.join(str(n) for n in difference_of_sets(args[1], args[0]))
        
        intersection = ', '.join(str(n) for n in intersection_of_sets(args[0], args[1]))
        
        venn = venn2(args, ('Set A', 'Set B'))
        venn.get_label_by_id('10').set_text(set1)
        venn.get_label_by_id('01').set_text(set2)
        
        if bool(intersection):
            venn.get_label_by_id('11').set_text(intersection)

    if len(args) == 3: 
       
        set1 = ', '.join(str(n) for n in difference_of_sets(args[0], args[2], args[1]))
        set2 = ', '.join(str(n) for n in difference_of_sets(args[1], args[0], args[2]))
        set3 = ', '.join(str(n) for n in difference_of_sets(args[2], args[1], args[0]))
        
        intersection12 = ', '.join(str(n) for n in difference_of_sets(intersection_of_sets(args[0], args[1]),
                                                intersection_of_sets(args[0], args[1], args[2])))
        intersection13 = ', '.join(str(n) for n in difference_of_sets(intersection_of_sets(args[0], args[2]),
                                                intersection_of_sets(args[0], args[1], args[2])))
        intersection23 = ', '.join(str(n) for n in difference_of_sets(intersection_of_sets(args[1], args[2]),
                                                intersection_of_sets(args[0], args[1], args[2])))
        intersection = ', '.join(str(n) for n in intersection_of_sets(args[0], args[1], args[2]))
        
        venn = venn3(args, ('Set A', 'Set B', 'Set C'))
        venn.hide_zeroes()
        venn.get_label_by_id('100').set_text(set1)
        venn.get_label_by_id('010').set_text(set2)
        venn.get_label_by_id('001').set_text(set3)
        if bool(intersection12):
            venn.get_label_by_id('110').set_text(intersection12)
        if bool(intersection13):
            venn.get_label_by_id('101').set_text(intersection13)
        if bool(intersection23):
            venn.get_label_by_id('011').set_text(intersection23)
        if bool(intersection):
            venn.get_label_by_id('111').set_text(intersection)
        
  
    plt.title(title)
    plt.show()


# Function to calculate the union of several sets
def union_of_sets(*args):
    union = set()
    for arg in args:
        for element in arg:
            if element not in union:
                union.add(element)
    return union

# Function to calculate the intersection of several sets
def intersection_of_sets(*args):
    intersection = set(args[0])
    for arg in args:
            intermediate_intersection = set()
            for element in intersection:
                if element in arg:
                    intermediate_intersection.add(element)
            intersection = set(intermediate_intersection)
    return intersection

# Function to calculate the difference between several sets
def difference_of_sets(*args):
    difference = set()
    for arg in args:
        if arg != args[0]:
            intermediate_difference = set()
            for element in difference:
                if element not in arg:
                    intermediate_difference.add(element)
            difference = set(intermediate_difference)
        else:
            difference = set(args[0])
    return difference

# Function to calculate the complement of a set in another universal set
def complement_in_universal_set(universal_set, set):
    complement = set()
    for element in universal_set:
        if element not in set:
            complement.add(element)
    return complement

# Function to calculate the combination of two sets
def combine_sets(*args):
    combination = set()
    combination = union_of_sets(union_of_sets(*args), intersection_of_sets(*args))
    return combination

# Function to calculate the cardinality of a set
def set_cardinality(set):
    cardinality = len(set)
    return cardinality

# Function to check if a set is a subset of another
def is_subset(set_a, set_b):
    return all(element in set_b for element in set_a)

# Function to check if two sets are disjoint
def are_disjoint(set_a, set_b):
    return intersection_of_sets(set_a, set_b) == set()

def menu():
    root = tk.Tk()
    root.withdraw()  # Hide the main window
    
    # Show the menu in a pop-up window
    option = simpledialog.askinteger("Set Menu", 
                                     "Select an option:\n"
                                     "1. Operations between sets\n"
                                     "2. Set cardinality\n"
                                     "3. Subset check\n"
                                     "4. Disjoint sets\n"
                                     "5. Exit\n\n"
                                     "Enter the number of the desired option:")

    if option == 1:
        set_operations()
        menu()
    elif option == 2:
        set_input = input_set("Enter the elements of the set separated by spaces:")
        messagebox.showinfo("Set Cardinality", f"The cardinality of the set is: {len(set_input)}")
        menu()
    elif option == 3:
        set_a = input_set("Enter the elements of the first set separated by spaces:")
        set_b = input_set("Enter the elements of the second set separated by spaces:")
        if is_subset(set_a, set_b):
            messagebox.showinfo("Subset", "The first set is a subset of the second set.")
        else:
            messagebox.showinfo("Subset", "The first set is NOT a subset of the second set.")
        menu()
    elif option == 4:
        set_a = input_set("Enter the elements of the first set separated by spaces:")
        set_b = input_set("Enter the elements of the second set separated by spaces:")
        if are_disjoint(set_a, set_b):
            messagebox.showinfo("Disjoint Sets", "The sets are disjoint.")
        else:
            messagebox.showinfo("Disjoint Sets", "The sets are NOT disjoint.")
        menu()
    elif option == 5:
        messagebox.showinfo("Exit", "Goodbye!")
    else:
        messagebox.showerror("Error", "Invalid option. Please try again.")
    

# Function to perform operations between sets
def set_operations():
    root = tk.Tk()
    root.withdraw()  # Hide the main window
    
    # Ask the user to enter the number of sets
    count = simpledialog.askinteger("Set Operations", 
                                    "Enter the number of sets you want to use:")
    
    # Ask the user to enter the elements of each set
    sets = []
    for i in range(count):
        set_input = simpledialog.askstring("Set Operations", 
                                           f"Enter the elements of set {i+1} separated by spaces:")
        sets.append(set(set_input.split()))

    # Show the operations in a pop-up window
    option = simpledialog.askinteger("Set Operations", 
                                     "Select the operation you want to perform:\n"
                                     "1. Union of sets\n"
                                     "2. Intersection of sets\n"
                                     "3. Set difference\n"
                                     "4. Complement of a set in another universal set\n"
                                     "5. Combination of two sets\n\n"
                                     "Enter the number of the desired option:")
    
    if option == 1:
        result = union_of_sets(*sets)
    elif option == 2:
        result = intersection_of_sets(*sets)
    elif option == 3:
        result = difference_of_sets(*sets)
    elif option == 4:
        universal_set = input_set("Enter the elements of the universal set separated by spaces:")
        set_input = input_set("Enter the elements of the set to compute its complement:")
        result = complement_in_universal_set(universal_set, set_input)
    elif option == 5:
        result = combine_sets(*sets)
    else:
        messagebox.showerror("Error", "Invalid option. Please try again.")
        return

    messagebox.showinfo("Result", f"The result of the operation is: {result}")

     # Show the Venn diagram for the performed operation
    show_venn_diagram(*sets)
    show_venn_diagram(result)

# Function to enter a set from user input
def input_set(message):
    root = tk.Tk()
    root.withdraw()  # Hide the main window
    
    set_input = simpledialog.askstring("Set Input", message)
    return set(set_input.split())

# Execute the menu
menu()
