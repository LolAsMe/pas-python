produks = [
  {"nama":"sampo","harga":1000},
  {"nama":"odol", "harga":5000},
  {"nama":"sikat gigi", "harga":2000},
  {"nama":"sabun", "harga":4000}
]

def lengthProduks():
  return len(produks)

def printProduks():
  i=1
  for produk in produks:
    print(i,produk['nama'], produk['harga'])
    i=i+1

def tambahProduk(produk, harga):
    produks.append({"nama":produk,"harga":harga})