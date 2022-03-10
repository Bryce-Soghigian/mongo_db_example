


class UserFactory:
    def __init__(self, first, last, email=None):
        self.first = first
        self.last = last
        self.email = f'Your email: {self.first}.{self.last}@yahoo.com' if email is None else email 
    
    def __str__(self):
        return f'USER: {self.first} {self.last}'
    
    def to_dict(self):
        return {
            "first":self.first,
            "last": self.last,
            "email": self.email
        }