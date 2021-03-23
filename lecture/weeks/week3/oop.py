"""class instance, object method class method """

class ZuChan:
    def __init__(self,zuchan):
        self.zuchan=zuchan

    def emergcy(self, savelife):
        if self.zuchan < savelife:
            return 'you just can use ' + str(self.zuchan)
        else:
            self.zuchan = self.zuchan - savelife
            return self.zuchan

class Account:
    interest = 0.1 # interest :0.1 is very b
    zuchan = ZuChan(1000)

    def __init__(self,name,mount=777):
        self.name = name
        self.begin_mount= mount
        self._private =mount
        # self.zuchan = ZuChan(9) # if the class attribute name and the instance attribute name is same, then instance attribute is first

    def deposit(self,checkin):
        self.begin_mount = self.begin_mount+checkin
        return self.begin_mount

    def withdraw(self,checkout):
        if checkout>self.begin_mount:
            return 'over amount'
        else:
            self.begin_mount = self.begin_mount-checkout
            return self.begin_mount

    def emergency(self,savelife):
        return self.zuchan.emergcy(savelife)


    def checkZuchan(self):
        return self.zuchan.zuchan

    def __str__(self):
        return self.name +' has '+ str(self.begin_mount) +" in account"



charlie = Account('charlie',100)

lena = Account('fiona',1000)
daniel =lena

daniel.withdraw(500)
assert lena.begin_mount == 500

lena.begin_mount=90000
daniel.begin_mount=-10

daniel._private =-90

print(lena._private)


print(lena)

print(type(charlie))
print(charlie)

assert charlie.deposit(10)==110
assert charlie.withdraw(20)==90
assert charlie.withdraw(100) == 'over amount'

print(type(charlie))
print(type(Account))

assert charlie.interest ==0.1
assert daniel.interest == 0.1

print(charlie.interest)
assert Account.interest == 0.1

# class instance can not edit the class attribute
charlie.interest ==0.4

assert daniel.interest ==0.1

# the class attribute just can be edited by the class itself.
Account.interest =0.25

assert daniel.interest ==0.25


class CheckAccount(Account):
    def __init__(self,account,accountNumber):
        self.accountNumber= accountNumber
        self.begin_mount = account.begin_mount
        self.name =account.name


    def withdraw(self,checkout):
        if checkout > self.begin_mount:
            return 'Your CheckAccount has not enough money'
        else:
            self.begin_mount = self.begin_mount-checkout -1
            return self.begin_mount



charlie_check_1= CheckAccount(charlie,'10081009')


print(charlie_check_1)

charlie_check_1.withdraw(10)



assert charlie_check_1.begin_mount == 79

charlie_check_1.deposit(11)

assert charlie_check_1.begin_mount == 90

charlie.withdraw(10)

print(charlie.begin_mount)

print(charlie_check_1.begin_mount)
# assert charlie_check_1.begin_mount ==80


assert charlie.checkZuchan() ==1000
charlie.emergency(100)

print(charlie.checkZuchan())
print(charlie_check_1.checkZuchan())

assert charlie_check_1.checkZuchan() == 900

charlie_check_1.emergency(200)

assert lena.checkZuchan() == 700

