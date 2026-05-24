import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt
import seaborn as sns
import json

with open('job_listings.json', encoding='utf-8') as f:
    data = json.load(f)

job_listings = pd.DataFrame.from_dict(data, orient='index', columns=['description'])
job_listings.head()

x_train = pd.read_csv('x_train_Meacfjr.csv', index_col=0)
y_train = pd.read_csv('y_train_SwJNMSu.csv', index_col=0)

#IA
from sentence_transformers import SentenceTransformer, util

model = SentenceTransformer('all-MiniLM-L6-v2')

# Récupère toutes les descriptions du tableau
descriptions = job_listings['description'].astype(str).tolist()

# Encode toutes les descriptions en embeddings
embeddings = model.encode(descriptions, convert_to_tensor=True, show_progress_bar=True)

# Calcule la matrice de similarité cosinus
similarity_matrix = util.cos_sim(embeddings, embeddings).cpu().numpy()

# Crée une matrice d'adjacence pandas avec les IDs de postings
adjacency_df = pd.DataFrame(similarity_matrix, index=job_listings.index, columns=job_listings.index)

# Affiche quelques informations
print('Nombre de postings :', len(job_listings))
print('Taille de la matrice d\'adjacence :', adjacency_df.shape)
print(adjacency_df.iloc[:5, :5])

# Enregistre la matrice si besoin
adjacency_df.to_csv('job_similarity_adjacency_matrix.csv')
print('Matrice d\'adjacence sauvegardée dans job_similarity_adjacency_matrix.csv')  