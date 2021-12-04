class Player:
    def __init__(self, name: str, rating:float) -> None:
        self.name = name
        self.rating = rating
        
    def is_bye(self):
        return self.name == 'BYE'