from abc import ABCMeta, abstractmethod
import math

# mendefinisikan kelas abstrak
class Bangun3D(metaclass=ABCMeta):
   # mendefinisikan metode abstrak
   @abstractmethod
   def cetakData(self):
      pass
   @abstractmethod
   def hitungVolume(self):
      pass
   @abstractmethod
   def cetakVolume(self):
      pass

# mendefinisikan kelas konkrit yang merupakan
# turunan dari kelas abstrak
class Kotak(Bangun3D):
   def __init__(self, p, l=None, t=None):
      if l == None and t == None:
         # jika berupa Kubus
         self.panjang = self.lebar = \
         self.tinggi = p
      else:
         # jika berupa Balok
         self.panjang = p
         self.lebar = l
         self.tinggi = t
   # mengimplementasikan metode cetakData()
   def cetakData(self):
      print("panjang\t: ", self.panjang)
      print("lebar\t: ", self.lebar)
      print("tinggi\t: ", self.tinggi)

   # mengimplementasikan metode hitungVolume()
   def hitungVolume(self):
      return self.panjang * self.lebar * \
             self.tinggi

   # mengimplementasikan metode cetakVolume()
   def cetakVolume(self):
      print("Volume Kotak \t= ",
            self.hitungVolume())

class Tabung(Bangun3D):
   def __init__(self, r, t):
      self.jarijari = r
      self.tinggi = t

   # mengimplementasikan metode cetakData()
   def cetakData(self):
      print("jari-jari alas \t: ",
            self.jarijari)
      print("tinggi tabung \t: ", self.tinggi)

   # mengimplementasikan metode hitungVolume()
   def hitungVolume(self):
      return math.pi * pow(self.jarijari, 2) * \
             self.tinggi

   # mengimplementasikan metode cetakVolume()
   def cetakVolume(self):
      print("Volume Tabung \t= ",
            self.hitungVolume())

def main():
   obj1 = Kotak(6, 5, 4)  # balok
   print("BALOK")
   obj1.cetakData()
   obj1.cetakVolume()

   obj2 = Kotak(5)  # kubus
   print("\nKUBUS")
   obj2.cetakData()
   obj2.cetakVolume()

   obj3 = Tabung(3, 4)  # tabung
   print("\nTABUNG")
   obj3.cetakData()
   obj3.cetakVolume()

if __name__ == "__main__":
   main()
