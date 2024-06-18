# puc_satellite_deforestation
Usando dados de satélite para rastrear a pegada humana na floresta amazônica.

Objetivos:
1. Desenvolver um programa para calcular o percentual de floresta densa de uma imagem.
    a. Preferencialmente com segmentação de imagens por cores.
2. Desafio: Readequar o programa para segmentar a imagem nas diferentes categorias listadas na aba "Data" da página do Kaggle.

Data Labels
1. Primary
2. Water
3. Habitation
4. Agriculture
5. Road

Data source: [Kaggle - Planet: Understanding the Amazon from Space](https://www.kaggle.com/competitions/planet-understanding-the-amazon-from-space/data)

# Recursos
## K-Means
- [X] (Video) [Image Segmentation with K-Means Clustering in Python](https://www.youtube.com/watch?v=X-Y91ddBqaQ)

## Label Studio
- (Video) [Labeling images for semantic segmentation using Label Studio](https://www.youtube.com/watch?v=UUP_omOSKuc)

## Segmentação semnântica
- GSI Technology: [A Beginner’s Guide To Segmentation In Satellite Images: Walking Through Machine Learning Techniques For Image Segmentation And Applying Them To Satellite Imagery](https://gsitechnology.com/beginners-guide-to-segmentation-in-satellite-images/)
- (Video) [MATLAB:  Semantic Segmentation of Satellite Images](https://www.youtube.com/watch?v=k88RmW7mEig)
- [Satellite Image Semantic Segmentation](https://arxiv.org/abs/2110.05812) - Eric Guérin, Killian Oechslin, Christian Wolf, Benoît Martinez.
- [A brief introduction to satellite image segmentation with neural networks](https://medium.com/@robmarkcole/a-brief-introduction-to-satellite-image-segmentation-with-neural-networks-33ea732d5bce) - Robin Cole.
- [X] [How to do Semantic Segmentation using Deep learning](https://nanonets.com/blog/how-to-do-semantic-segmentation-using-deep-learning/)

# Possíveis arquiteturas
- UNet
- ResNet
- Global Convolution Network
