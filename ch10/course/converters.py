class FourDigitYearConverter:
    regex = '[0-9]{4}'

    def to_pyton(self,value):
        return int(value)
    
    def to_url(self,value):
        return f"{value:4d}"