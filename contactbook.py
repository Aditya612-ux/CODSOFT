import tkinter as tk
from tkinter import messagebox, simpledialog

class Contact:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone

class ContactBook:
    def __init__(self, root):
        self.root = root
        self.root.title("Contact Book")
        self.contacts = []
        
        # GUI Layout
        self.frame = tk.Frame(self.root)
        self.frame.pack(pady=20)

        self.label = tk.Label(self.frame, text="Contact Book", font=("Cascadia Code", 16))
        self.label.pack()

        self.listbox = tk.Listbox(self.frame, width=50, height=15)
        self.listbox.pack(pady=10)

        self.add_button = tk.Button(self.frame, text="Add Contact", command=self.add_contact)
        self.add_button.pack(side=tk.LEFT, padx=10)

        self.delete_button = tk.Button(self.frame, text="Delete Contact", command=self.delete_contact)
        self.delete_button.pack(side=tk.LEFT, padx=5)

        self.view_button = tk.Button(self.frame, text="View Contact", command=self.view_contact)
        self.view_button.pack(side=tk.LEFT, padx=10)

    def add_contact(self):
        name = simpledialog.askstring("Input", "Enter Contact Name:")
        phone = simpledialog.askstring("Input", "Enter Contact Phone Number:")
        
        if name and phone:
            self.contacts.append(Contact(name, phone))
            self.update_listbox()
        else:
            messagebox.showwarning("Input Error", "Please enter both name and phone number.")

    def delete_contact(self):
        selected_contact_index = self.listbox.curselection()
        if selected_contact_index:
            del self.contacts[selected_contact_index[0]]
            self.update_listbox()
        else:
            messagebox.showwarning("Selection Error", "Please select a contact to delete.")

    def view_contact(self):
        selected_contact_index = self.listbox.curselection()
        if selected_contact_index:
            contact = self.contacts[selected_contact_index[0]]
            messagebox.showinfo("Contact Info", f"Name: {contact.name}\nPhone: {contact.phone}")
        else:
            messagebox.showwarning("Selection Error", "Please select a contact to view.")

    def update_listbox(self):
        self.listbox.delete(0, tk.END)
        for contact in self.contacts:
            self.listbox.insert(tk.END, contact.name)

if __name__ == "__main__":
    root = tk.Tk()
    contact_book = ContactBook(root)
    root.mainloop()