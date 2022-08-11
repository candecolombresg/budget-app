class Category:

    def __init__(self,category):
        self.category=category
        self.ledger=[]
        self.balance=0
        self.spend=0

    def deposit(self,amount,description=""):
        self.ledger.append({"amount":amount, "description":description})
        self.balance+=amount

    def withdraw(self,amount,description=""):
        if self.check_funds(amount) == False:
            return False
        else:
            self.ledger.append({"amount":-amount, "description":description})
            self.balance-=amount
            self.spend+=amount
            return True

    def get_balance(self):
        return self.balance

    def transfer(self,amount,category):
        if self.check_funds(amount) == True:
            self.withdraw(amount,"Transfer to "+category.category)
            category.deposit(amount,"Transfer from "+self.category)
            return True
        else:
            return False
            
    def check_funds(self,amount):
        if amount > self.balance:
            return False
        else:
            return True

    def __str__(self):
        lista = []
        category=str(self.category)
        lista.append("*"*(int((30-len(category))/2))+category+"*"*(int((30-len(category))/2))+"\n")
        for item in self.ledger:
            description = str(item["description"])[0:23]
            amount = "{:.2f}".format(item["amount"])
            lista.append(description+" "*(30-len(description)-len(amount))+amount+"\n")
        lista.append("Total: "+str(self.balance))
        return "".join(lista)




def create_spend_chart(categories):
    lista = ["Percentage spent by category"]

    total = sum([cat.spend for cat in categories])

    for i in range(11):
        number = str(100-i*10)
        line=" "*(3-len(number))+number+"|"
        for cat in categories:
            percentage = cat.spend*100/total
            if percentage > (100-i*10):
                line+=" o "
            else:
                line+="   "
        lista.append("\n"+line+" ")



    lista.append("\n"+4*" "+(3*len(categories))*"-"+"-")

    max_cat = max(len(cat.category) for cat in categories)
    i = 0
    while i<max_cat:
        line=4*" "
        for cat in categories:
            if i<len(cat.category):
                line += " "+cat.category[i]+" "
            else:
                line+=" "*3            
        i+=1
        lista.append("\n"+line+" ")


    return "".join(lista)