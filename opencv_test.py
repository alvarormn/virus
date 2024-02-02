import cv2

# Cargar una imagen de prueba
image = cv2.imread('WhatsApp Image 2024-01-14 at 20.30.24 (1).jpeg')

# Mostrar la imagen
cv2.imshow('Test Image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
