import datetime


class Project:
    def __init__(self, name, start_date, priority, cost_estimate, percent_complete):
        self.name = name
        self.start_date = start_date
        self.priority = priority
        self.cost_estimate = cost_estimate
        self.percent_complete = percent_complete

    def __repr__(self):
        """Return string representation of a Project."""
        return f"{self.name}, start: {self.start_date}, priority {self.priority}, estimate: ${self.cost_estimate}, completion: {self.percent_complete}"

    def __lt__(self, other):
        return self.priority < other.priority

    def is_complete(self):
        """Determine if Project is complete."""
        return self.percent_complete == 100
