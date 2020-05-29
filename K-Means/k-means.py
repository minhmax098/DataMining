# có một tập hợp tọa độ điểm, trên không gian Oxy, mỗi điểm có tọa độ (x,y) xác định. Bài toán xác đinh vấn đề là chia các điểm này thành K cụm phân biệt
# bắt đầu
import numpy as np   # thư viện tính toán toán học
import matplotlib.pyplot as plt # visualize data sử dụng đồ thị
import spicy.spatial.distance import cdist # hỗ trợ tính khoảng cách


# khởi tạo các mẫu dữ liệu xung quanh 3 tâm cụm(2,2);(9,2);(4,9)
# với mỗi tâm cum, ta sẽ tạo dữ liệu gồm 500 điểm xung quanh nó lần lượt là X0,X1,X2
means = [[2, 2], [9, 2], [4, 9]]
cov = [[2, 0], [0, 2]]
n_samples = 500  # 500 điểm xung quanh
n_cluster = 3   # 3 điểm X0,X1,X2
X0 = np.random.multivariate_normal(means[0], cov, n_samples)
X1 = np.random.multivariate_normal(means[1], cov, n_samples)
X2 = np.random.multivariate_normal(means[2], cov, n_samples)
X = np.concatenate((X0, X1, X2), axis = 0)

# vẽ ra
plt.xlabel('x')
plt.ylabel('y')
plt.plot(X[:, 0], X[:, 1], 'bo', markersize=5)
plt.plot()
plt.show()