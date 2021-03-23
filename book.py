import pandas as pd
class Order:
    def __init__(self, volume, price):
        self.vol = volume
        self.prx = price
class Book(Order):
    nbObj = 0
    def __init__(self, name):
        self.Name = name
        self.buyOrd = []
        self.sellOrd = []
    def display(self):
        res1=pd.DataFrame(columns=['Order', 'VolumePrix', 'ID'])
        res2=pd.DataFrame(columns=['Order', 'VolumePrix', 'ID'])
        for i in range(len(self.sellOrd)):
            res1 = res1.append({'Order' : 'SELL' , 'VolumePrix' : "%i@%g" % (self.sellOrd[i].get("ordre").vol, self.sellOrd[i].get("ordre").prx), 'ID' : "id=%i" % self.sellOrd[i].get("id")} , ignore_index=True)
        for i in range(len(self.buyOrd)):
            res2 = res2.append({'Order' : 'BUY' , 'VolumePrix' : "%i@%g" % (self.buyOrd[i].get("ordre").vol, self.buyOrd[i].get("ordre").prx), 'ID' : "id=%i" % self.buyOrd[i].get("id")}, ignore_index=True)
        res = pd.concat([res1,res2])
        print(res)
    def Inser_buy(self, volume, price):
        boule = True
        Book.nbObj = Book.nbObj +1
        new_ = Order(volume, price)
        to_add = {'id':self.nbObj,'ordre':new_}
        print('--- Insert BUY %i@%g id= %d On %s' % (new_.vol,new_.prx, Book.nbObj,self.Name))
        if len(self.buyOrd)!=0:
            boule = self.OperationB(to_add)
        else:
            print("Book on " + self.Name)
        if boule == True:
            self.buyOrd.append(to_add)
        self.SortedB()
        self.display()
        print("--------------------------------")
    def Inser_sell(self,volume, price):
        boule = True
        Book.nbObj = Book.nbObj +1
        new_ = Order(volume, price)
        to_add = {"id":self.nbObj,"ordre":new_}
        print('--- Insert SELL %i@%g id= %d On %s' % (new_.vol,new_.prx, Book.nbObj,self.Name))
        if len(self.sellOrd)!=0:
            boule = self.OperationS(to_add)
        else:
            print("Book on " + self.Name)
        if boule == True:
            self.sellOrd.append(to_add)
        self.SortedB()
        self.display()
        print("--------------------------------")
    def SortedB(self):
        self.buyOrd = sorted(self.buyOrd,key=lambda k:k["ordre"].prx, reverse=True)
        self.sellOrd = sorted(self.sellOrd,key=lambda k:k["ordre"].prx, reverse=True)
    def OperationB(self, to_add):
        boule = True
        condi = False
        i = 0
        while condi != True:
            if self.sellOrd[0].get("ordre").prx <= to_add.get("ordre").prx:
                temp = to_add.get("ordre").vol
                to_add.get("ordre").vol -= self.sellOrd[0].get("ordre").vol
                if temp >= self.sellOrd[0].get("ordre").vol:
                    print("Execute %i at %g on %s" % (self.sellOrd[0].get("ordre").vol,to_add.get("ordre").prx, self.Name))
                    del(self.sellOrd[0])
                else:
                    self.sellOrd[0].get("ordre").vol -= temp
                    print("Execute %i at %g on %s" % (temp,to_add.get("ordre").prx, self.Name))
                self.SortedB()
            if(to_add.get("ordre").vol<=0):
                boule = False
                condi = True
            if self.sellOrd[0].get("ordre").prx > to_add.get("ordre").prx:
                condi = True
        print("Book on " + self.Name)
        return boule
    def OperationS(self, to_add):
        boule = True
        condi = False
        while condi != True:
            if self.buyOrd[0].get("ordre").prx >= to_add.get("ordre").prx:
                temp = to_add.get("ordre").vol
                to_add.get("ordre").vol -= self.buyOrd[0].get("ordre").vol
                if temp >= self.buyOrd[0].get("ordre").vol:
                    print("Execute %i at %g on %s" % (self.buyOrd[0].get("ordre").vol,self.buyOrd[0].get("ordre").prx, self.Name))
                    del(self.buyOrd[0])
                else:
                    self.buyOrd[0].get("ordre").vol -= temp
                    print("Execute %i at %g on %s" % (temp,self.buyOrd[0].get("ordre").prx, self.Name))
                self.SortedB()
            if(to_add.get("ordre").vol<=0):
                boule = False
                condi = True
            if self.buyOrd[0].get("ordre").prx < to_add.get("ordre").prx:
                condi = True
        print("Book on " + self.Name)
        return boule

                    
    
