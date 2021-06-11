from abc import abstractmethod, ABC


class Musician():
        members = []

        def __init__(self,name):
            self.name=name
            Musician.members.append(self)

        @abstractmethod  

        def __str__(self):
            pass
        

        def __repr__(self):
           pass

        def get_instrument(self):
            pass

        def play_solo(self):
            pass

        
class Band(Musician):

    
    bandslist=[]


    def __init__(self,name,members):
        
        self.name=name
        self.members=members
        members=Musician.members
        Band.bandslist.append(name)


        
        
    def play_solos(self):
        return f"{self.name} you have to play solo!"

    
    def __str__(cls):
        pass
    def ____repr__(cls):
        pass

    @classmethod

    def to_list(cls) :
        return f"{cls.bandslist}"   

class Guitarist(Musician):
    def __init__(self,name):
        super().__init__(name)

    def get_instrument(self):
            return f"{self.name} is paly with guitar"   
        
    def play_solo(self):
            return f"The Guitaraist {self.name} can play solo"  


class Bassist(Musician):
    def __init__(self,name):
        super().__init__(name)

    def get_instrument(self):
            return f"{self.name} is paly with base"  

    def play_solo(self):
            return f"The Bassist {self.name} can play solo"  

class Drummer(Musician):
    def __init__(self,name):
        super().__init__(name)       

    def get_instrument(self):
            return f"{self.name} is paly with drums"     
    

    def play_solo(self):
            return f"The Drummer {self.name} can play solo"  




if __name__ == "__main__":
    heros = Band('heros',members=['Jhon','Devid','Lionel'])
    fluffy = Band('fluffy',["fsa",'sdfds','dsfds'])
    Jhon = Guitarist('Jhon')
    Devid=Drummer('Devid')
    Lionel = Bassist('Lionel')
    
    
    print(Devid.play_solo())
    print(Jhon.play_solo())
    print(Lionel.play_solo())
   
    
    print(Band.bandslist)
    print(fluffy.members)
    print(heros.members)
    print(fluffy.to_list())

    print(Jhon.get_instrument())
    print(Devid.get_instrument())
    print(Lionel.get_instrument())
