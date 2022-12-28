import cv2
# 이미지 읽기
img_color = cv2.imread('cat.jpg', cv2.IMREAD_COLOR)


cv2.namedWindow('Show Image');
# 이미지 출력
cv2.imshow('Show Image', img_color);

cv2.waitKey(0)
# 이미지 그레이 스케일로 변환
img_gray = cv2.cvtColor(img_color, cv2.COLOR_BGR2GRAY)

cv2.imshow('gray Image', img_gray)
cv2.waitKey(0)
# 이미지 저장
cv2.imwrite('savedImage.jpg', img_gray)
cv2.destroyAllWindows()