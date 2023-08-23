import numpy as np
from PIL import Image
import os, glob, random
 
# 出力ファイル
outfile = "../animal_photos.npz"
# 画像数
max_photo = 150
# 画像の縦横サイズ（ピクセル）
photo_size = 150
 
x = []
y = []
 
# ディレクトリ以下の画像を読み込んでNumpy配列に追加する関数
# 　第一引数：画像のディレクトリパス、第二引数：分類ラベル
def read_files(path, label):
  files = glob.glob(path + "/*jpg")
  random.shuffle(files)
  
  num = 0
  for f in files:
    if num >= max_photo: break
    num += 1
    
    img = Image.open(f)
    img = img.convert("RGB")
    img = img.resize((photo_size, photo_size))
    img = np.asarray(img)
    x.append(img)
    y.append(label)
 
# 焼き鳥の画像には分類ラベル0、焼きそばは分類ラベル1、焼き芋は分類ラベル2を付与
read_files("../dog", 0)
read_files("../cat", 1)
 
# Numpy形式でファイルに保存
np.savez(outfile, x=x, y=y)