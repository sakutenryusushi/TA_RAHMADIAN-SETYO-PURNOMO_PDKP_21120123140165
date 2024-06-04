import tkinter as tk
from tkinter import messagebox, simpledialog
from car_wash_app import CarWashAppLogic

class CarWashAppGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Car Wash Ticket Applier")
        self.master.geometry("400x300")
        self.master.configure(bg="#f0f0f0")
        
        self.logic = CarWashAppLogic()
        
        self.setup_gui()
    
    def setup_gui(self):
        self.label = tk.Label(self.master, text="Car Wash Ticket Booking System", font=("Helvetica", 16, "bold"), bg="#f0f0f0")
        self.label.pack(pady=10)
        
        self.book_button = tk.Button(self.master, text="Book Ticket", command=self.book_ticket, width=20, bg="#4CAF50", fg="white")
        self.book_button.pack(pady=5)
        
        self.cancel_button = tk.Button(self.master, text="Cancel Booking", command=self.cancel_booking, width=20, bg="#f44336", fg="white")
        self.cancel_button.pack(pady=5)
        
        self.view_button = tk.Button(self.master, text="View Queue", command=self.view_queue, width=20, bg="#2196F3", fg="white")
        self.view_button.pack(pady=5)
        
        self.queue_listbox = tk.Listbox(self.master, width=50, height=10)
        self.queue_listbox.pack(pady=10)
    
    def book_ticket(self):
        name = simpledialog.askstring("Input", "Enter your name:")
        plate = simpledialog.askstring("Input", "Enter your car plate (e.g., B 1234 XYZ):")
        if plate:
            plate = plate.upper()
        message = self.logic.book_ticket(name, plate)
        self.update_queue_listbox()
        messagebox.showinfo("Info", message)
    
    def cancel_booking(self):
        message = self.logic.cancel_booking()
        self.update_queue_listbox()
        messagebox.showinfo("Info", message)
    
    def view_queue(self):
        queue_str = self.logic.view_queue()
        messagebox.showinfo("Queue", queue_str)
    
    def update_queue_listbox(self):
        self.queue_listbox.delete(0, tk.END)
        for entry in self.logic.get_queue_list():
            self.queue_listbox.insert(tk.END, entry)

if __name__ == "__main__":
    root = tk.Tk()
    app = CarWashAppGUI(root)
    root.mainloop()
