import matplotlib as mpl
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import numpy as np
from numpy.typing import NDArray

def plot_images(image_array: NDArray[np.uint8], clustered_image: NDArray[np.uint8]):
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5))

    # Imagem original
    ax1.imshow(image_array, cmap='gray')
    ax1.set_title('Original image')
    ax1.axis('off')

    # Imagem clusterizada
    ax2.imshow(clustered_image, cmap='gray')
    ax2.set_title('Clustered image')
    ax2.axis('off')

    plt.subplots_adjust(wspace=0.05) # diminui margem entre plots

    plt.show()

def print_cluster_percentage(predicted_clusters: NDArray[np.int32]):
    # Calcula a porcentagem de cada cluster
    unique, counts = np.unique(predicted_clusters, return_counts=True)
    percentages = (counts / counts.sum()) * 100

    # Seleciona os indices em ordem decrescente
    sorted_indices = np.argsort(-percentages)

    for idx in sorted_indices:
        cluster = unique[idx]
        percentage = percentages[idx]
        print(f"Cluster {cluster}: {percentage:.2f}%")

def print_prediction(image_path: str, kmeans):
    image_array = mpl.image.imread(image_path)
    pixels = image_array.reshape(-1, 4)

    # prediz o cluster de cada pixel
    predicted_clusters = kmeans.predict(pixels)

    # seleciona o centro de cada cluster
    cluster_centers = kmeans.cluster_centers_

    # cria um array no mesmo shape da imagem original com as cores de cada centroide
    clustered_pixels = cluster_centers[predicted_clusters]

    # faz o reshape para o formato original
    clustered_image = clustered_pixels.reshape(image_array.shape).astype(np.uint8)

    print_cluster_percentage(predicted_clusters)
    plot_images(image_array, clustered_image)
