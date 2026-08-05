#POLYMORPHISM

#Whereby one method name can have different behaviour depending on the object using it.

class Man:
    def language(self):
        print("Man speaks")

class KhoiKhoi(Man):
    def language(self):
        print("Click sound")

class Kamba(Man):
    def language(self):
        print("Kikamba")


#creating objects
khoikhoi = KhoiKhoi()
kamba = Kamba()

khoikhoi.language()
kamba.language()