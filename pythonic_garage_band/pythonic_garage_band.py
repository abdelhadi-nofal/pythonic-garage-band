from abc import abstractmethod, ABC

class Band:
    members=[]
    def __init__(self, name, members):
        self.name = name
        self.members = members
        Band.members.append(members)
        
    
    def play_solos(self):
        for i in Band.members:
            return f"{i.play_solos()}plays solo!"

    
    def to_list(self,cls):
        return cls.members

    def __str__(self):
        return f"Band {self.name}"
    
    def __repr__(self):
        return f" '{self.name}' "
        

class Musician():
        
    def __init__(self,name):
        self.name=name
    
    @abstractmethod
    def __str__(self):
        pass

    def __repr__(self):
        pass
    
    def play_solo(self):
        pass

class Guitarist(Musician):

    def __init__(self,name):
        super().__init__(name)

    def __str__(self):
        return f"Guitarist {self.name}"
    
    def __repr__(self):
        return f" '{self.name}' "
    
    def get_instrument(self):
        return (f'{self.name} is a Guitarist')
    

class Bassist(Musician):

    def __init__(self,name):
        super().__init__(name)

    def __str__(self):
        return f"Bassist {self.name}"
    
    def __repr__(self):
        return f" '{self.name}' "

    def get_instrument(self,name):
        return (f'{self.name} is a Bassist')
    

class Drummer(Musician):

    def __init__(self,name):
        super().__init__(name)

    def __str__(self):
        return f"Drummer {self.name}"
    
    def __repr__(self):
        return f" '{self.name}' "

    def get_instrument(self):
        return (f'{self.name} is a Drummer')       
