import cv2 as cv 
import time
import threading
from fastai.vision import *

#Opcion 1, Imagenes en 224 * 224, ResNet34
img_size = 224
model = models.resnet34
trained_ia = 'baches224_rn34'

#variables para modelo
root = '.'
path = Path(root)
classes = ['Negative data', 'Positive data']
data = ImageDataBunch.single_from_classes(path, classes, ds_tfms=get_transforms(do_flip=False),size=img_size).normalize(imagenet_stats)
learn = cnn_learner(data, models.resnet34)

#carga del modelo
learn.load('baches224_rn34')

#variables para prediccion
img = None
prediccion = 'Inicializando...'


#Open CV variables
option_test_val = 1

fp = 0
terminado = False
font = cv.FONT_HERSHEY_SIMPLEX 
org = (50, 50) 
fontScale = 1
color = (255, 255, 255) 
thickness = 2

def reproducir_video():
    cap = cv.VideoCapture(0)
    while(True):
        global terminado
        global fp
        global img

        fp = fp +1
        ret, frame = cap.read()

        frame = cv.putText(frame, prediccion, org, font,fontScale, color, thickness, cv.LINE_AA)
        cv.imshow('video', frame)

        if (fp % 90 == 0):
            cv.imwrite('frame.jpg',frame)
            print('captura guardada')
            img = open_image(path/'frame.jpg')
            print('imagen asignada')

        if cv.waitKey(1) & 0xFF == ord('q'):
            terminado = True
            break
    cap.release()
    cv.destroyAllWindows()

def option_test():
  global option_test_val
  option_test_val = option_test_val + 1.0
  return option_test_val

