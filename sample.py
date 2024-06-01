class Color:

    def __init__(self, color, symbol, mood, effect, weddings, positive, negative):
        self.color = color
        self.symbol = symbol
        self.mood = mood
        self.effects = effect
        self.weddings = weddings
        self.positive = positive
        self.negative = negative

    def reaction_mood(self):
        print(f"{self.color} represent its mood as {self.mood}. ")

    def ambiance_wedding(self):
        print(f"{self.color} in the wedding it means {self.weddings}")

    def positives(self):
        print(f"{self.color} fosters {self.positive}.")

    def negatives(self):
        print(f"{self.color} has a negative side which is {self.negative}")

class Red(Color):
    def __init__(self, color, symbol, mood, effect, weddings, positive, negative):
        super().__init__(color, symbol, mood, effect, weddings, positive, negative)

class Orange(Color):
    def __init__(self, color, symbol, mood, effect, weddings, positive, negative):
        super().__init__(color, symbol, mood, effect, weddings, positive, negative)

class Yellow(Color):
    def __init__(self, color, symbol, mood, effect, weddings, positive, negative):
        super().__init__(color, symbol, mood, effect, weddings, positive, negative)

class Green(Color):
    def __init__(self, color, symbol, mood, effect, weddings, positive, negative):
        super().__init__(color, symbol, mood, effect, weddings, positive, negative)

class Blue(Color):
    def __init__(self, color, symbol, mood, effect, weddings, positive, negative):
        super().__init__(color, symbol, mood, effect, weddings, positive, negative)

class Purple(Color):
    def __init__(self, color, symbol, mood, effect, weddings, positive, negative):
        super().__init__(color, symbol, mood, effect, weddings, positive, negative)

class Pink(Color):
    def __init__(self, color, symbol, mood, effect, weddings, positive, negative):
        super().__init__(color, symbol, mood, effect, weddings, positive, negative)

class Brown(Color):
    def __init__(self, color, symbol, mood, effect, weddings, positive, negative):
        super().__init__(color, symbol, mood, effect, weddings, positive, negative)

class Black(Color):
    def __init__(self, color, symbol, mood, effect, weddings, positive, negative):
        super().__init__(color, symbol, mood, effect, weddings, positive, negative)

class Gray(Color):
    def __init__(self, color, symbol, mood, effect, weddings, positive, negative):
        super().__init__(color, symbol, mood, effect, weddings, positive, negative)

red = Red ("Red", "Stregth", "Anger", "Attentions", "Love and Desire", "Sexuality", "Danger")
orange = Orange("Orange", "Emotion", "Excitement", "Encourage", "Happiness", "Positivity", "Domination")
yellow = Yellow("Yellow", "Optimism", "Cheerful", "Inspire", "New Beginnings", "Mentality", "Caution")
green = Green("Green", "Nature", "Relaxing", "Balances", "Growth", "Generousity", "Judgemental")
blue = Blue("Bule", "Trust", "Calming", "Protects", "Loyalty", "Peace", "Conservative")
purple = Purple("Purple", "Royalty", "Mysterious", "Inspire", "Passion", "Fantasy", "Immature")
pink = Pink("Pink", "Femininity", "Luxrious", "Kindness", "Romance", "Kindness", "Unconfident")
brown = Brown("Brown", "Stability", "Simplicity", "Grounds", "Warmth", "Appreciation", "Predictable")
black = Black("Black", "Protection", "Serious", "Secure", "Stregth", "Formality", "Depression")
gray = Gray("Gray", "Compromise", "Timeless", "Calms", "Maturity", "Realibility", "Unemotional")