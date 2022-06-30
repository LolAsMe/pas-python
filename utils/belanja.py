class Belanja:
    
  def __init__(self):
    self.daftar = []
    self.total = 0
    
  def addBelanja(self, nama, harga, jumlah):
      self.daftar.append([nama,harga,jumlah])
      self.total = self.total + int(harga)*int(jumlah)
      
  def showBelanja(self):
      for barang in self.daftar:
         print('nama: {}, harga: {}, jumlah: {}, total:{}'.format(barang[0],barang[1], barang[2], int(barang[1])*int(barang[2])))
      print("jumlah total", self.total)
      
  def toFile(self):
      with open('daftar.txt', 'w') as f:
         for item in self.daftar:
             f.write('\n nama: {}, harga: {}, jumlah: {}, total:{}'.format(item[0],item[1], item[2], int(item[1])*int(item[2])))
         f.write("\n grand total: %s" % self.total)