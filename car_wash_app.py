from queue_module import Queue
from stack_module import Stack
import re

class CarWashAppLogic:
    def __init__(self):
        self.queue = Queue()
        self.cancel_stack = Stack()
    
    def validate_plate(self, plate):
        pattern = r'^[A-Z]{1,2} \d{1,4} [A-Z]{1,3}$'
        return re.match(pattern, plate)
    
    def book_ticket(self, name, plate):
        if name and plate and self.validate_plate(plate):
            self.queue.enqueue((name, plate))
            return f"Booking successful for {name} with plate {plate}"
        return "Booking failed: Invalid name or plate format"
    
    def cancel_booking(self):
        if self.queue.is_empty():
            return "No bookings to cancel"
        else:
            cancelled_booking = self.queue.dequeue()
            self.cancel_stack.push(cancelled_booking)
            name, plate = cancelled_booking
            return f"Booking cancelled for {name} with plate {plate}"
    
    def view_queue(self):
        if self.queue.is_empty():
            return "No bookings in the queue"
        else:
            return "\n".join([f"{name} - {plate}" for name, plate in self.queue.get_all()])
    
    def get_queue_list(self):
        return [f"{name} - {plate}" for name, plate in self.queue.get_all()]
