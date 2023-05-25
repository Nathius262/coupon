from decimal import Decimal

class Currency:
    """
    Note that the base currency used to 
    calculate the following currency is USD($)
    """
    def __init__(self):
        self.naira = 460.78 # $1 to Nigerian naira
        self.usd = 1.00 # $1 
        self.pkr = 286.17 # $1 to Pakistani Rupee
        self.ghs = 10.99 # $1 to Ghanaian Cedis
        
    def usd_naira(self, currency, amount):
        """a function that convert USD to Nigerian naira

        Args:
            currency (string): the currency should either be in $ or N
            amount (integer|two decimal place): the amount to convert to

        Returns:
            integer|two decimal place: returns either a naira value or $ depending on what currency is passed as an argument
        """
        value=""
        if currency == "$":
            value = amount*self.naira
        elif currency == "N":
            value = amount/self.naira            
        return value
    
    def usd_pkr(self, currency, amount):
        """a function that convert USD to Pakistani Rupee

        Args:
            currency (string): the currency should either be in $ or PKR
            amount (integer|two decimal place): the amount to convert to

        Returns:
            integer|two decimal place: returns either a PKR value or $ depending on what currency is passed as an argument
        """
        value=""
        if currency == "$":
            value = amount*self.pkr
        elif currency == "PKR":
            value = amount/self.pkr        
        return value
        
    def usd_ghs(self, currency, amount):
        """a function that convert USD to Ghanaian Cedis

        Args:
            currency (string): the currency should either be in $ or GHS
            amount (integer|two decimal place): the amount to convert to

        Returns:
            integer|two decimal place: returns either a GHS value or $ depending on what currency is passed as an argument
        """
        value=""
        if currency == "$":
            value = amount*self.ghs
        elif currency == "GHS":
            value = amount/self.ghs            
        return value
        

    def currencyConverter(self, currency_from, currency_to, amount):
        """
        convert between the list of currency below using their sign
        e.g GHS, PKR, $ and N
        
        ('USD', '$'),
        ("Naira", 'N'),
        ("Pakistani Rupee", 'PKR'),
        ("Ghanaian Cedis", 'GHS')

        Args:
            currency_from (string): the currency you want to convert from comes as the first argument
            currency_to (string): the currency you want to convert to comes as the second argument
            amount (integer|two decimal place): the amount to convert to comes as the third argument
            
        Returns:
            integer|two decimal place: returns either a GHS value or $ depending on what currency is passed as an argument
        
        """
        
        new_amount = ""
        USD = "$"
        if currency_from == USD:
            if currency_to == "N":
                new_amount = self.usd_naira(currency_from, amount=amount)
            elif currency_to == "PKR":
                new_amount =self.usd_pkr(currency_from, amount=amount)
            elif currency_to =="GHS":
                new_amount =self.usd_ghs(currency_from, amount=amount)
        elif currency_from == "N":
            usd_naira = self.usd_naira(currency_from, amount=amount)
            if currency_to == USD:
                new_amount = usd_naira
            elif currency_to == "PKR":
                new_amount = self.usd_pkr(USD, usd_naira)
            elif currency_to == "GHS":              
                new_amount = self.usd_ghs(USD, usd_naira)
        elif currency_from == "PKR":
            usd_pkr = self.usd_pkr(currency_from, amount=amount)
            if currency_to == USD:
                new_amount = usd_pkr
            elif currency_to == "N":
                new_amount = self.usd_naira(USD, usd_pkr)
            elif currency_to == "GHS":              
                new_amount = self.usd_ghs(USD, usd_pkr)
        elif currency_from == "GHS":
            usd_ghs = self.usd_ghs(currency=currency_from, amount=amount)
            if currency_to == USD:
                new_amount = usd_ghs
            elif currency_to == "N":
                new_amount = self.usd_naira(USD, usd_ghs)
            elif currency_to == "PKR":              
                new_amount = self.usd_pkr(USD, usd_ghs)
                
        return round(new_amount, 2)