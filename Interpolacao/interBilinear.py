import cv2

imagem = cv2.imread(r"C:\Users\WEB\Pictures\wallpaperflare.com_wallpaper (1).jpg")
imagem_ampliada = cv2.resize(imagem, None, fx=2, fy=2, interpolation=cv2.INTER_LINEAR)

cv2.imwrite(r"ampliada_bilinear.jpg", imagem_ampliada)  
imagem_reduzida = cv2.resize(imagem, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_LINEAR)
cv2.imwrite(r"reduzida_bilinear.jpg", imagem_reduzida)

