class Category:

    def __init__(self, name):
        self.name = name
        self.ledger = []
        self.withdrawamount = 0.0

    def deposit(self, amount, description = ""):
        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount, description = ""):
        if(self.check_funds(amount)):
            self.ledger.append({"amount": -amount, "description": description})
            self.withdrawamount += amount
            return True
        else:
            return False

    def get_balance(self):
        totalamount = 0
        for items in self.ledger:
            totalamount += items["amount"]
        return totalamount

    def transfer(self, amount, category):
        if(self.check_funds(amount)):
            self.withdraw(amount, "Transfer to " + category.name)
            category.deposit(amount, "Transfer from " + self.name)
            return True
        else:
            return False

    def check_funds(self, amount):
        if(self.get_balance() >= amount):
            return True
        else:
            return False

    def __str__(self):
        titleline = f"{self.name:*^30}\n"
        detailline = ""
        total = 0
        for details in self.ledger:
            detailline += f"{details['description'][:23]:23}" + f"{details['amount']:>7.2f}\n"
            total += details['amount']

        finalout = titleline + detailline + "Total: " + str(total)
        return finalout

def create_spend_chart(categories):
    balances = []
    percentage = []
    names = []
    total_amount = 0.0
    for category in categories:
        names.append(category.name)
        total_amount  += category.withdrawamount
        balances.append(category.withdrawamount)
    for i in range(len(categories)):
        percentage.append(int((balances[i]/total_amount)*10)*10)

    heading = "Percentage spent by category\n"
    axis = 100
    axisbot = ""
    bar = ""
    finalaxisbot = ""
    for j in range(11):
        graph = ""
        for individual in percentage:
            if(individual >= axis):
                graph += " o "
            else:
                graph += "   "
        bar += str(str(axis).rjust(3) + "|" + graph + " \n")
        axis -= 10

    lines = "    " + len(percentage)*"---" + "-\n"
    maxlength = max(names, key = len)
    for k in range(len(maxlength)):
        axisbot = "    "
        for cat in names:
            if(len(cat) <= k):
                axisbot += "   "
            else:
                axisbot += str(cat[k].center(3))
        if(k >= len(maxlength)-1):
            finalaxisbot += str(axisbot + " ")
        else:
            finalaxisbot += str(axisbot + " \n")

    final = heading + bar + lines + finalaxisbot

    return final
