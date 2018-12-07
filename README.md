# ADS&A : ESILV IBO3
# Robin CONVERT & Sasha COLLOMÉ
# Project : ImageRecognition


VF

Notre objectif est de réaliser une intelligence artificielle spécialisée dans la reconnaissance d'images.
Pour cela, nous utilisons un Réseau Neuronal Convolutif (RNC) pour créer des features maps (matrices indiquant les caractéristiques physiques et géométriques d'une image) qui servent d'entrées à un MLP (MultiLayer Perceptron). Ce dernier retourne une probabilité pour la nature de l'image.

On commence par entrainer notre IA sur l'ensemble CIFAR-10 qui rassemble 60 000 images de 10 classes différentes. Nous utilisons, lors de cette première étape, le RNC VGG16.
Dans un second temps, nous réalisons une autre IA pour la reconnaissance de Pokemon à l'aide d'un dataset de 8 190 images avec 721 Pokemons (= classes) différents provenant du lien suivant : www.kaggle.com/ankitesh97/pokemon-images. Nous commençons par utiliser VGG16 puis nous créons notre propre RNC.


VO
Our goal is to create an artificial intelligence specialized in images recognition.
To do that, we use a Convolutional Neural Network (CNN) to generate features maps (matrices showing physical & geometrical features of an image) used as an input to a MLP (MultiLayer Perceptron). The latter returns a probability for an image's nature.

We start by training our AI on CIFAR-10 which gathers 60 000 images of 10 differents classes. We use, for this first step, the CNN VGG16.
Then, we create another AI for Pokemons recognition using a 8 190 images with 721 different Pokemons ( = classes) dataset from the following link : www.kaggle.com/ankitesh97/pokemon-images. We start by using VGG16 again and then we will create our own CNN.