class Bird:

    all_birds = []
    bird_food = ["Seeds", "Corn", "Sunflowers"]

    @classmethod
    def show_me_all_the_birds(hamburger):
        print(hamburger)
        return hamburger.all_birds
    
    @classmethod
    def average_feathers(cls):
        all_feathers = [ bird.number_of_feathers for bird in cls.all_birds ]
        return sum(all_feathers) / len(all_feathers)
    
    def __init__(self, name, number_of_feathers):
        self.name = name
        self._number_of_feathers = number_of_feathers
        Bird.all_birds.append(self)

    def __repr__(self):
        return f"Bird(name={self.name}, number_of_feathers={self.number_of_feathers})"

    def tweet(self):
        return f"{self.name} is posting all their tweets... I mean X's"
    
    def chirp(self):
        self.tweet()

    @property
    def number_of_feathers(self):
        return self._number_of_feathers
    
    @number_of_feathers.setter
    def number_of_feathers(self, new_num):
        if new_num > self._number_of_feathers:
            print('YOU CANT ATTACH FEATHERS TO A BIRD')
        else:
            self._number_of_feathers = new_num
            return self.number_of_feathers