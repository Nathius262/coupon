from decimal import Decimal

class Currency:
    """
    Note that the base currency used to 
    calculate the following currency is 
    """
    def __init__(self):
        self.dollar = 500 #the rate of exchange in between naira and dollar i.e $1 = N500
        self.usd = 460 #the rate of exchange in between naira and USD i.e USD 1 = N460
        self.pkr = 1.6 #the rate of exchange in between naira and PKR i.e PKR 1 = N1.6
        self.php = 8.2 #the rate of exchange in between naira and PHP i.e PHP 1 = N8.2
        self.inr = 5.5 #the rate of exchange in between naira and INR i.e INR 1 = N5.2
        self.ghs = 0.00427 #the rate of exchange in between naira and GHS i.e GHS 1 = N0.00427
        self.zar = 23.4 #the rate of exchange in between naira and ZAR i.e ZAR 1 = N23.4
        
        
    def naira_dollar(self, currency, amount):
        """a function that convert dollar to Nigerian naira

        Args:
            currency (string): the currency should either be in $ or N
            amount (integer|float): the amount to convert to

        Returns:
            integer|float: returns either a naira value or $ depending on what currency is passed as an argument
        """
        value=""
        if currency == "N":
            value = amount*self.dollar
        elif currency == "$":
            value = amount/self.dollar            
        return value
    
    def naira_usd(self, currency, amount):
        """a function that convert between naira and usd

        Args:
            currency (string): the currency should either be in usd or N
            amount (integer|float): the amount to convert to

        Returns:
            integer|float: returns either a naira value or usd depending on what currency is passed as an argument
        """
        value=""
        if currency == "N":
            value = amount*self.usd
        elif currency == "USD":
            value = amount/self.usd            
        return value
    
    def naira_pkr(self, currency, amount):
        """a function that convert between naira and Pakistani Rupee

        Args:
            currency (string): the currency should either be in N or PKR
            amount (integer|float): the amount to convert to

        Returns:
            integer|float: returns either a PKR value or N depending on what currency is passed as an argument
        """
        value=""
        if currency == "N":
            value = amount*self.pkr
        elif currency == "PKR":
            value = amount/self.pkr        
        return value
        
    def naira_ghs(self, currency, amount):
        """a function that convert between naira and ghs

        Args:
            currency (string): the currency should either be in N or GHS
            amount (integer|float): the amount to convert to

        Returns:
            integer|float: returns either a GHS value or N depending on what currency is passed as an argument
        """
        value=""
        if currency == "N":
            value = amount*self.ghs
        elif currency == "GHS":
            value = amount/self.ghs            
        return value
    
    def naira_inr(self, currency, amount):
        """a function that convert between naira and inr

        Args:
            currency (string): the currency should either be in N or inr
            amount (integer|float): the amount to convert to

        Returns:
            integer|float: returns either a inr value or N depending on what currency is passed as an argument
        """
        value=""
        if currency == "N":
            value = amount*self.inr
        elif currency == "INR":
            value = amount/self.inr            
        return value
    
    def naira_php(self, currency, amount):
        """a function that convert between naira and php

        Args:
            currency (string): the currency should either be in N or php
            amount (integer|float): the amount to convert to

        Returns:
            integer|float: returns either a php value or N depending on what currency is passed as an argument
        """
        value=""
        if currency == "N":
            value = amount*self.php
        elif currency == "PHP":
            value = amount/self.php            
        return value
    
    def naira_zar(self, currency, amount):
        """a function that convert between naira and zar

        Args:
            currency (string): the currency should either be in N or zar
            amount (integer|float): the amount to convert to

        Returns:
            integer|float: returns either a zar value or N depending on what currency is passed as an argument
        """
        value=""
        if currency == "N":
            value = amount*self.zar
        elif currency == "ZAR":
            value = amount/self.zar            
        return value
    
    def __convertCurrencyfromBasetoGivenCurrency(self, currency_to, value_currency_from_base):
        """get the the value of the converted value from the base currency and convert it to the given currency

        Args:            
            currency_to (string): get the given currency
            value_currency_from_base (integer|float): gets the converted currency 

        Returns:
            integer|float: returns the value base on the given currency
        """
        #naira = "N"
        if currency_to == "$":
            given_currency_amount = self.naira_dollar(currency_to, amount=value_currency_from_base)
        elif currency_to == "PKR":
            given_currency_amount =self.naira_pkr(currency_to, amount=value_currency_from_base)
        elif currency_to =="USD":
            given_currency_amount =self.naira_usd(currency_to, amount=value_currency_from_base)
        elif currency_to =="INR":
            given_currency_amount =self.naira_inr(currency_to, amount=value_currency_from_base)
        elif currency_to =="PHP":
            given_currency_amount =self.naira_php(currency_to, amount=value_currency_from_base)
        elif currency_to =="ZAR":
            given_currency_amount =self.naira_zar(currency_to, amount=value_currency_from_base)
        elif currency_to =="GHS":
            given_currency_amount =self.naira_ghs(currency_to, amount=value_currency_from_base)
            
        return given_currency_amount
            
    def __convertCurrencytoBaseCurrency(self, currency_from, amount):
        """get the given currency to be converted as an argument and covert it to base currency

        Args:
            currency_from (string): the currency you want to convert from comes as the first argument
            amount (integer|float): the amount to convert to comes as the third argument

        Returns:
            integer|float: returns a value converted from a base currency from a given currency
        """
        naira = "N" #base currency
        if currency_from == "$":
            value_currency_from_base = self.naira_dollar(naira, amount=amount)
        elif currency_from == "PKR":
            value_currency_from_base =self.naira_pkr(naira, amount=amount)
        elif currency_from =="USD":
            value_currency_from_base =self.naira_usd(naira, amount=amount)
        elif currency_from =="INR":
            value_currency_from_base =self.naira_inr(naira, amount=amount)
        elif currency_from =="PHP":
            value_currency_from_base =self.naira_php(naira, amount=amount)
        elif currency_from =="ZAR":
            value_currency_from_base =self.naira_zar(naira, amount=amount)
        elif currency_from =="GHS":
            value_currency_from_base =self.naira_ghs(naira, amount=amount)
            
        return value_currency_from_base
            
    def currencyConverter(self, currency_from, currency_to, amount):
        """
        convert between the list of currency below using their sign
        e.g GHS, PKR, $ and N, INR, PHP, ZAR, USD
        
        ('USD', 'USD'),
        ('Dollar', '$'),
        ("Naira", 'N'),
        ("Pakistani Rupee", 'PKR'),
        ("Indian Rupee", 'INR')
        ("Phillippine Peso", 'PHP')
        ("South African Rand", 'ZAR')
        ("Ghanaian Cedis", 'GHS')

        Args:
            currency_from (string): the currency you want to convert from comes as the first argument
            currency_to (string): the currency you want to convert to comes as the second argument
            amount (integer|float): the amount to convert to comes as the third argument
            
        Returns:
            integer|float: returns either a GHS value or $ depending on what currency is passed as an argument
        
        """
        
        new_amount = ""
        if currency_from == "N":
            new_amount = self.__convertCurrencyfromBasetoGivenCurrency(currency_to=currency_to, value_currency_from_base=amount)
        elif currency_to == "N":
            new_amount = self.__convertCurrencytoBaseCurrency(currency_from, amount)
        else:
            base_value = self.__convertCurrencytoBaseCurrency(currency_from, amount)
            new_amount = self.__convertCurrencyfromBasetoGivenCurrency(currency_to, base_value)
        
                
        return round(Decimal(new_amount), 2)
    
    def isBaseCurrency(self, currency):
        """checkBaseCurrency is a method that checks and returns a boolean if the given currency is a base currency that is, naira

        Args:
            currency (string): the currency that needs to be compared with the base currency in the database
        """
        
        base_currency = "N"
        given_currency = currency
        
        return base_currency == given_currency

        
currency = Currency()


"""
##### testing code
affilate = 4996.54
task = 9729.34

data={
    "affilate":currency.currencyConverter("PKR", "INR", affilate),
    "task":currency.currencyConverter("PKR", "INR", task),
}
print(data)#

"""