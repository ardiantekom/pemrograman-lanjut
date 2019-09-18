# mendefinisikan kelas induk pertama
class Induk1(object):
   def __init__(self, a):
      self.a = a
   def cetakA(self):
      print("Nilai a = ", self.a)

# mendefinisikan kelas induk kedua
class Induk2(object):
   def __init__(self, b):
      self.b = b
   def cetakB(self):
      print("Nilai b = ", self.b)

# mendefinisikan kelas turunan
class Anak(Induk1, Induk2):
   def __init__(self, a, b, c):
      # memanggil Induk1.__init__()
      Induk1.__init__(self, a)
      # memanggil Induk2.__init__()
      Induk2.__init__(self, b)
      self.c = c
   def cetakC(self):
      print("Nilai c = ", self.c)

def main():
   # membuat objek dari kelas Anak
   obj = Anak(111, 222, 333)

   # memanggil metode kelas Induk1 dari obj
   obj.cetakA()

   # memanggil metode kelas Induk2 dari obj
   obj.cetakB()

   # memanggil metode kelas Anak
   obj.cetakC()

if __name__ == "__main__":
   main()
