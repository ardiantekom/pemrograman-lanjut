class Kotak(object):
   def __init__(self, p, l, t):
      self.panjang = p
      self.lebar = l
      self.tinggi = t

   def hitungVolume(self):
      return self.panjang * self.lebar * \
             self.tinggi

   def cetakData(self):
      print("panjang\t: ", self.panjang)
      print("lebar\t: ", self.lebar)
      print("tinggi\t: ", self.tinggi)

   def cetakVolume(self):
      print("Volume\t= ", self.hitungVolume())

# mendefinisikan kelas turunan (subclass)
class KotakWarna(Kotak):
   def __init__(self, p, l, t, w):
      # memanggil Kotak.__init__()
      super(KotakWarna, self).__init__(p, l, t)
      # menambah atribut baru
      self.warna = w

   def cetakData(self):
      # memanggil Kotak.cetakData()
      super(KotakWarna, self).cetakData()
      print("warna\t: ", self.warna)

def main():
   # membuat objek KotakWarna
   kotakwarna1 = KotakWarna(6, 5, 4, "merah")

   # menggunakan objek
   kotakwarna1.cetakData()
   kotakwarna1.cetakVolume()

if __name__ == "__main__":
   main()
