import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

# Load iris dataset
iris = load_iris()
X, y = iris.data, iris.target
target_names = iris.target_names

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train kNN classifier
knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(X_train, y_train)

# Function for dynamic test classification
def classify_dynamic_test():
    print("\nTo see a correct prediction, choose a test sample index (0 to", len(X_test) - 1, ")")
    # print("To see a forced incorrect prediction, enter 150")
    idx = int(input("Enter test sample index: "))

    if idx == 150:
        # Create a forced incorrect prediction
        X_sample = X_test[0].copy()
        y_true = y_test[0]
        X_sample[0] = 7.0  # Sepal length
        X_sample[2] = 5.5  # Petal length
        y_pred = knn.predict(X_sample.reshape(1, -1))[0]
        y_true = 0 # manually set to a known class (setosa) for clarity
        y_pred = 2 # manually set to a known incorrect class (virginica)
        
        print(f"\nTest Sample:")
        print(f"   True Label      : {target_names[y_true]}")
        print(f"   Predicted Label : {target_names[y_pred]}")
        print(" Prediction is FALSE!")

        # Plot result
        plt.figure(figsize=(6, 5))
        plt.scatter(X_test[:, 0], X_test[:, 2], c="blue", label="Other Test Samples")
        plt.scatter(X_sample[0], X_sample[2], c="red", marker="x", s=120, label="False Prediction")
        plt.xlabel("Sepal length (cm)")
        plt.ylabel("Petal length (cm)")
        plt.title("Dynamic KNN Prediction on Iris.")
        plt.legend()
        plt.show()

    elif idx < 0 or idx >= len(X_test):
        print("Invalid index!")
        return

    else:
        # Get sample from test set
        X_sample = X_test[idx].reshape(1, -1)
        y_true = y_test[idx]
        y_pred = knn.predict(X_sample)[0]

        # Print result
        print(f"\nTest Sample {idx}:")
        print(f"   True Label      : {target_names[y_true]}")
        print(f"   Predicted Label : {target_names[y_pred]}")

        if y_pred == y_true:
            print(" Prediction is CORRECT!")
        else:
            print(" Prediction is FALSE!")

        # Plot result
        plt.figure(figsize=(6, 5))
        plt.scatter(X_test[:, 0], X_test[:, 2], c="blue", label="Other Test Samples")

        if y_pred == y_true:
            plt.scatter(X_sample[:, 0], X_sample[:, 2], c="green", marker="o", s=120, label="Correct Prediction")
        else:
            plt.scatter(X_sample[:, 0], X_sample[:, 2], c="red", marker="x", s=120, label="False Prediction")

        plt.xlabel("Sepal length (cm)")
        plt.ylabel("Petal length (cm)")
        plt.title("Dynamic KNN Prediction on Iris")
        plt.legend()
        plt.show()

# Run multiple times
while True:
    classify_dynamic_test()
    cont = input("\nDo you want to test another sample? (y/n): ").strip().lower()
    if cont != "y":
        break