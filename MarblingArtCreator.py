"""import numpy as np
import cv2

# Desenin boyutları
width, height = 800, 600

# Boş bir resim oluşturun
ebru_pattern = np.zeros((height, width, 3), dtype=np.uint8)

# Renk paletti
colors = [(255, 153, 51), (0, 255, 0), (0, 0, 255)]

# Rastgele şekilleri ebru benzeri desende oluşturun
for _ in range(5000):
    x, y = np.random.randint(0, width), np.random.randint(0, height)
    radius = np.random.randint(10, 50)
    color = colors[np.random.randint(0, 3)]
    cv2.circle(ebru_pattern, (x, y), radius, color, -1)

# Deseni gösterin veya kaydedin
cv2.imshow('Ebru Deseni', ebru_pattern)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Deseni bir dosyaya kaydetmek için kullanabilirsiniz
cv2.imwrite('ebru_desen.png', ebru_pattern)
"""


import numpy as np
import cv2
from tkinter import *
from tkinter import colorchooser

# Desenin boyutları
width, height = 800, 600

# Boş bir resim oluşturun
ebru_pattern = np.zeros((height, width, 3), dtype=np.uint8)

# Kullanıcıya renk seçme arayüzü
def choose_color():
    color = colorchooser.askcolor()[0]
    if color:
        return tuple(int(c) for c in color)
    else:
        return None

# Renk paleti
def select_colors():
    colors = []
    for _ in range(3):
        color = choose_color()
        if color:
            colors.append(color)
        else:
            return None
    return colors

# Kullanıcıdan renkleri seçin
colors = select_colors()
if colors is None:
    print("Renk seçilmediği için program sonlandırıldı.")
    exit()

# Rastgele şekilleri ebru benzeri desende oluşturun
for _ in range(5000):
    x, y = np.random.randint(0, width), np.random.randint(0, height)
    radius = np.random.randint(10, 50)
    color = colors[np.random.randint(0, 3)]
    cv2.circle(ebru_pattern, (x, y), radius, color, -1)

# Deseni gösterin veya kaydedin
cv2.imshow('Ebru Deseni', ebru_pattern)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Deseni bir dosyaya kaydetmek için kullanabilirsiniz
cv2.imwrite('ebru_desen.png', ebru_pattern)
