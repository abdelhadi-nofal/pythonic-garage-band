from abc import abstractmethod, ABC

class Band:

    
    instances=[]


    def __init__(self,name,members):
        
        self.name=name
        self.members=members
        Band.instances.append(self)


        
        
    def play_solos(self):
        solos=[]
        for i in self.members:
             solos.append(i.play_solo())
        return solos

    
    def __str__(self):
        return f'Our band is {self.name}'
    def __repr__(self):

        return f"Band instance. Name = {self.name}"

    @classmethod

    def to_list(cls) :
        return cls.instances   


class Musician:
        members = []

        def __init__(self,name):
            self.name=name
            Musician.members.append(self.name)

        @abstractmethod  

        def __str__(self):
            pass
        
        def __repr__(self):
           pass
        

        def get_instrument(self):
            pass
        

        def play_solo(self):
            pass

        


class Guitarist(Musician):
    def __init__(self,name):
        super().__init__(name)
    
    def __str__(self):
        return f"My name is {self.name} and I play guitar"
    def __repr__(self):
        return f"Guitarist instance. Name = {self.name}"

        

    @staticmethod
    def get_instrument():
        return "guitar"
    @staticmethod
    def play_solo():
        return "face melting guitar solo"  


class Drummer(Musician):
    def __init__(self,name):
        super().__init__(name)
    def __str__(self):
        return f"My name is {self.name} and I play drums"
    def __repr__(self):
        return f"Drummer instance. Name = {self.name}"
    @staticmethod
    def get_instrument():
        return "drums"
    @staticmethod
    def play_solo():
        return "rattle boom crash"
    

class Bassist(Musician):
    def __init__(self,name):
        super().__init__(name)
    def __str__(self):
        return f"My name is {self.name} and I play bass"
    def __repr__(self):
        return f"Bassist instance. Name = {self.name}"
    @staticmethod
    def get_instrument():
        return "bass"
    @staticmethod
    def play_solo():
        return "bom bom buh bom"




# if __name__ == "__main__":
#     heros = Band('heros',members=['Jhon','Devid','Lionel'])
#     fluffy = Band('fluffy',["fsa",'sdfds','dsfds'])
#     Jhon = Guitarist('Jhon')
#     Devid=Drummer('Devid')
#     Lionel = Bassist('Lionel')
    
#     print(Musician.members)    
#     print(Devid.play_solo())
#     print(Jhon.play_solo())
#     print(Lionel.play_solo())
   
    
#     print(Band.bandslist)
#     print(fluffy.members)
#     print(heros.members)
#     print(fluffy.to_list())

#     print(Jhon.get_instrument())
#     print(Devid.get_instrument())
#     print(Lionel.get_instrument())


