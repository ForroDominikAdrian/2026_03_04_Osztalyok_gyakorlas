class Auto:
    def __init__(self, marka, tipus, evjarat):
        self.marka = marka
        self.tipus = tipus
        self.evjarat = evjarat
        self.sebesseg = 0
        
    def __str__(self):
        return f"{self.marka},{self.tipus},{self.evjarat},{self.sebesseg}"
    
    def gyorsit(self,ertek):
        self.sebesseg += ertek
        if self.sebesseg > 200:
            self.sebesseg = 200
            print(f"NE GYORSíTSÁL MÁR MISTER VIN DIESEL! ({self.marka})")
    
    def fekez(self,ertek):
        self.sebesseg -= ertek
        if self.sebesseg < 0:
            self.sebesseg = 0
            print("HÚ DE NAGYOT FÉKEZTÉL ÖCSÉM!!!! ÓVATOSABBAN! KRESSZ MI AZ ANYÁMÉRT VAN?")