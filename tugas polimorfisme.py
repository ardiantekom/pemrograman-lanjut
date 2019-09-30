# mendefinisikan kelas BilanganBulat
class BilanganBulat(object):
   def __init__(self, nilai):
      if not isinstance(nilai, int):
         raise TypeError("Nilai harus bertipe bilangan bulat")
      self.nilai = nilai

   # overload terhadap operator +
   def __add__(self, objek):
      if isinstance(objek, int):
         return self.nilai + objek
      elif isinstance(objek, float):
         return float(self.nilai + objek)
      elif isinstance(objek, BilanganBulat):
         return self.nilai + objek.nilai
      else:
         raise TypeError("Objek harus bertipe numerik")
         
	 
   # overload terhadap operator >=
   def __ge__(self, objek):
      if isinstance(objek, int):
         return self.nilai >= objek
      elif isinstance(objek, float):
         return float(self.nilai) >= objek
      elif isinstance(objek, BilanganBulat):
         return self.nilai >= objek.nilai
      else:
         raise TypeError("Objek harus bertipe numerik")

	

def main():
   # objek dari kelas BilanganBulat
   a = BilanganBulat(7)
   b = BilanganBulat(2)

   # objek bertipe int
   c = 5

   # objek bertipe float
   d = 10.25

   # menggunakan operator +
   print("a >= b: ", a >= b)
   print("a >= c: ", a >= c)
   print("a >= d: ", a >= d)

if __name__ == "__main__":
   main()
