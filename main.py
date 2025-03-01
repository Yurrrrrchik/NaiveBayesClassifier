import numpy as np
from scipy.stats import norm
import matplotlib.pyplot as plt


class NaiveBayesClassifier:
    def fit(self, x, y):
        self.classes = np.unique(y)
        self.means = {}
        self.stds = {}
        self.priors = {}

        for c in self.classes:
            x_c = x[y == c]
            self.means[c] = np.mean(x_c, axis=0)
            self.stds[c] = np.std(x_c, axis=0)
            self.priors[c] = len(x_c) / len(x)

    def predict(self, X):
        predictions = []
        for x in X:
            posteriors = []
            for c in self.classes:
                prior = np.log(self.priors[c])
                posterior = np.sum(np.log(norm.pdf(x, self.means[c], self.stds[c])))
                posterior = prior + posterior
                posteriors.append(posterior)
            predictions.append(self.classes[np.argmax(posteriors)])
        return predictions


data_x = [(7.2, 2.5), (6.4, 2.2), (6.3, 1.5), (7.7, 2.2), (6.2, 1.8), (5.7, 1.3), (7.1, 2.1), (5.8, 2.4), (5.2, 1.4),
          (5.9, 1.5), (7.0, 1.4), (6.8, 2.1), (7.2, 1.6), (6.7, 2.4), (6.0, 1.5), (5.1, 1.1), (6.6, 1.3), (6.1, 1.4),
          (6.7, 2.1), (6.4, 1.8), (5.6, 1.3), (6.9, 2.3), (6.4, 1.9), (6.9, 2.3), (6.5, 2.2),
          (6.0, 1.5), (5.6, 1.1), (5.6, 1.5), (6.0, 1.0), (6.0, 1.8), (6.7, 2.5), (7.7, 2.3), (5.5, 1.1), (5.8, 1.0),
          (6.9, 2.1), (6.6, 1.4), (6.3, 1.6), (6.1, 1.4), (5.0, 1.0), (7.7, 2.0), (4.9, 1.7), (7.2, 1.8), (6.8, 1.4),
          (6.1, 1.2), (5.8, 1.9), (6.3, 2.5), (5.7, 2.0), (6.5, 1.8), (7.6, 2.1), (6.3, 1.5),
          (6.7, 1.4), (6.4, 2.3), (6.2, 2.3), (6.3, 1.9), (5.5, 1.3), (7.9, 2.0), (6.7, 1.8), (6.4, 1.3), (6.5, 2.0),
          (6.5, 1.5), (6.9, 1.5), (5.6, 1.3), (5.8, 1.2), (6.7, 2.3), (6.0, 1.6), (5.7, 1.2), (5.7, 1.0), (5.5, 1.0),
          (6.1, 1.4), (6.3, 1.8), (5.7, 1.3), (6.1, 1.3), (5.5, 1.3), (6.3, 1.3), (5.9, 1.8),
          (7.7, 2.3), (6.5, 2.0), (5.6, 2.0), (6.7, 1.7), (5.7, 1.3), (5.5, 1.2), (5.0, 1.0), (5.8, 1.9), (6.2, 1.3),
          (6.2, 1.5), (6.3, 2.4), (6.4, 1.5), (7.4, 1.9), (6.8, 2.3), (5.6, 1.3), (5.8, 1.2), (7.3, 1.8), (6.7, 1.5),
          (6.3, 1.8), (6.0, 1.6), (6.4, 2.1), (6.1, 1.8), (5.9, 1.8), (5.4, 1.5), (4.9, 1.0)]
data_y = [1, 1, 1, 1, 1, -1, 1, 1, -1, -1, -1, 1, 1, 1, -1, -1, -1, 1, 1, 1, -1, 1, 1, 1, 1, 1, -1, -1, -1, 1, 1, 1, -1,
          -1, 1, -1, -1, -1, -1, 1, 1, 1, -1, -1, 1, 1, 1, 1, 1, -1, -1,
          1, 1, 1, -1, 1, 1, -1, 1, -1, -1, -1, -1, 1, -1, -1, -1, -1, -1, 1, -1, -1, -1, -1, 1, 1, 1, 1, -1, -1, -1,
          -1, 1, -1, -1, 1, -1, 1, 1, -1, -1, 1, -1, 1, -1, 1, 1, -1, -1, -1]

data_x = np.array(data_x)
data_y = np.array(data_y)

classifier = NaiveBayesClassifier()
classifier.fit(data_x, data_y)

pred_y = classifier.predict(data_x)
print("Предсказание классов объектов: ", pred_y)
print("Настоящие классы объектов: ", data_y)

wrong_class = sum(data_y != pred_y)
wrong_class_percent = wrong_class / len(data_y) * 100
print("Процент неверных классификаций: ", wrong_class_percent)
print("Неверные классификации: ", data_x[data_y != pred_y])

class1 = data_x[data_y == -1]
class2 = data_x[data_y == 1]

plt.scatter(class1[:, 0], class1[:, 1], c='r', label='Class -1')
plt.scatter(class2[:, 0], class2[:, 1], c='b', label='Class 1')

plt.xlabel('x')
plt.ylabel('y')

plt.legend()
plt.show()
