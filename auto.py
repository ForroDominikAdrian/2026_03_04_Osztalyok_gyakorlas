class Auto:
    def __init__(self, marka, tipus, evjarat):
        self.marka = marka
        self.tipus = tipus
        self.evjarat = evjarat
    
    def __str__(self):
        return f"{self.marka},{self.tipus},{self.evjarat}"