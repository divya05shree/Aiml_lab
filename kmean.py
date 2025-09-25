import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
from sklearn.mixture import GaussianMixture
from sklearn.metrics import silhouette_score, calinski_harabasz_score
import matplotlib.pyplot as plt

# Load and preprocess
df = pd.read_csv("iris.csv")
df = df.select_dtypes(include=['float64', 'int64'])  # Use only numeric columns
data_scaled = StandardScaler().fit_transform(df)

# Clustering
kmeans_labels = KMeans(n_clusters=3, random_state=42).fit_predict(data_scaled)
gmm_labels = GaussianMixture(n_components=3, random_state=42).fit_predict(data_scaled)

# Evaluation
def evaluate(name, labels):
    sil = silhouette_score(data_scaled, labels)
    ch = calinski_harabasz_score(data_scaled, labels)
    print(f"{name}: Silhouette Score = {sil:.4f}, Calinski-Harabasz Index = {ch:.4f}")
    return sil, ch

k_sil, k_ch = evaluate("K-Means", kmeans_labels)
g_sil, g_ch = evaluate("EM (GMM)", gmm_labels)

print("\nComparison Summary:")
if k_sil > g_sil:
    print("K-Means has a better Silhouette Score indicating better-defined clusters.")
elif k_sil < g_sil:
    print("EM (Gaussian Mixture) has a better Silhouette Score indicating better-defined clusters.")
else:
    print("Both algorithms have equal Silhouette Scores.")

if k_ch > g_ch:
    print("K-Means has a better Calinski-Harabasz Index indicating better cluster separation.")
elif k_ch < g_ch:
    print("EM (Gaussian Mixture) has a better Calinski-Harabasz Index indicating better cluster separation.")
else:
    print("Both algorithms have equal Calinski-Harabasz Index.")

# Visualization using PCA
pca = PCA(n_components=2)
data_pca = pca.fit_transform(data_scaled)

plt.figure(figsize=(12, 5))

# K-Means plot
plt.subplot(1, 2, 1)
plt.scatter(data_pca[:, 0], data_pca[:, 1], c=kmeans_labels, cmap='viridis', s=30)
plt.title("K-Means Clustering")

# EM plot
plt.subplot(1, 2, 2)
plt.scatter(data_pca[:, 0], data_pca[:, 1], c=gmm_labels, cmap='plasma', s=30)
plt.title("EM (Gaussian Mixture) Clustering")

plt.tight_layout()
plt.show()
 