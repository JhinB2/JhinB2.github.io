class ore():
    def __init__(self,type,value):
        self.type = type
        self.value = value
    def checkValue(self):
        print("This is actually ", self.type)
        print("It is worth ", self.value)

iron = ore("Iron","100$")
gold = ore("Gold","500$")
diamond = ore("Diamond", "1000$")

#--------------------------------------------------------

iron.checkValue()
gold.checkValue()
diamond.checkValue()