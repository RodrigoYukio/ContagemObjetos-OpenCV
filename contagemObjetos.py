import cv2
import numpy 
import imutils
 
image = cv2.imread("parafusos.jpg")
 
cv2.imshow(" Imagem original", image)
 
#aplicação do filtro cinza
image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("Tons de cinza", image_gray)
 
#mediana aplicada para realizar a limiarização "image_blur", caso eu colocasse somente "image_gray" ele contabiliza 30 moedas ao inves de 28
image_blur = cv2.medianBlur(image_gray, 5)
cv2.imshow("Mediana", image_blur)
 
#fiz a alteração de "image_thresh" para "image_otsu" e depois de "THRESH_BINARY_INV" para "THRESH_OTSU" com essa comando alterado é feito a limiarização através do OTSU
#aplicação do limiar
image_res ,image_otsu = cv2.threshold(image_blur,30,255,cv2.THRESH_OTSU)
print("Limiarizacao: ", image_res)
cv2.imshow("Limiarizacao", image_otsu)
 
#alterei de "numpy.ones((7,7)" para numpy.ones((1,1)
#aplicação da morfologia
kernel = numpy.ones((1,1),numpy.uint8)
morpho = cv2.morphologyEx(image_otsu,cv2.MORPH_ERODE ,kernel)
cv2.imshow("Morfologia matematica ", morpho)
 
cnts = cv2.findContours(morpho.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
 
cnts = imutils.grab_contours(cnts)
objects = str(len(cnts))
 
#Contagem de objetos
text = "Objetos encontrados:"+str(objects)
cv2.putText(image, text, (10, 25),  cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 1)
 
print(objects)
cv2.imshow("Contagem parafusos", image)
 
cv2.waitKey(0)