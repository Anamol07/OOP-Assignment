import datetime

# Task class representing individual tasks
class Task:
    def __init__(self, title, date_due):
        self.title = title
        self.completed = False
        self.date_created = datetime.datetime.now()
        self.date_due = date_due  
    
    def mark_completed(self):
        self.completed = True

    def change_title(self, new_title):
        self.title = new_title

    def change_date_due(self, new_due):
        self.date_due = new_due  

    def __str__(self):
        status = "Completed" if self.completed else "Not Completed"
        return (f"[{status}] {self.title} | "
                f"Created: {self.date_created.strftime('%Y-%m-%d')} | "
                f"Due: {self.date_due.strftime('%Y-%m-%d')}")
