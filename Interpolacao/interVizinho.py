import cv2
imagem = cv2.imread(r"C:\Users\WEB\Pictures\wallpaperflare.com_wallpaper (1).jpg")

imagem_ampliada = cv2.resize(imagem, None, fx=2, fy=2, interpolation=cv2.INTER_NEAREST)
imagem_reduzida = cv2.resize(imagem, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_NEAREST)

cv2.imwrite('ampliada_vizinho.jpg', imagem_ampliada)
cv2.imwrite('reduzida_vizinho.jpg', imagem_reduzida)
