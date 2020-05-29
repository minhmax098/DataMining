# Image Compression using K-means clustering
#
# tiền xử lí
# import các thư viện
from PIL import Image
import numpy as np
from sklearn.cluster import KMeans

# Load ảnh lên, hiển thị ảnh gốc
image = Image.open('D:\\Tài liệu năm 4 ĐH kì 2\\Trí tuệ nhân tạo\\vitcon.jpg')
image.show()

# xử lí dữ liệu với ảnh
image = np.array(image)  # chuyển ảnh sang nhị phân array
shapeRoot = image.shape

# reshape lại matrix
image_feed = image.reshape((shapeRoot[0] * shapeRoot[1]) * shapeRoot[2])

# Aps dụng Kmeans vào để phân cụm
kmeans = KMeans(n_clusters=8, max_iter= 300, random_state=0).fit(image_feed)

#
# Xay dung lai mang hinh anh roi hien thi

rs_list = [kmeans.cluster_centers_[i] for i in (kmeans.labels_)]
rs_list = np.array(rs_list)
rs_list = rs_list.reshape(shapeRoot)

rs_list = rs_list.astype("uint8")
img_end = Image.fromarray(rs_list, 'RGB')
img_end.save('outimg2.jpg')
img_end.show()




