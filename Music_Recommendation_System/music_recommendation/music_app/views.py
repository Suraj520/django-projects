
from django.shortcuts import render,redirect
from django.views import View
import bz2
import pickle
import _pickle as cPickle
import numpy as np


rating_df_path="/home/suraj/ClickUp/Jan-Feb/Django Projects/DjangoProjects/Music_Recommendation_System/notebook/rating_df.pbz2"
similarity_score_path ="/home/suraj/ClickUp/Jan-Feb/Django Projects/DjangoProjects/Music_Recommendation_System/notebook/similarity_scores.pbz2"
table_path = "/home/suraj/ClickUp/Jan-Feb/Django Projects/DjangoProjects/Music_Recommendation_System/notebook/final_table.pbz2"

# Load any compressed pickle file
def decompress_pickle(file):
    data = bz2.BZ2File(file, 'rb')
    data = cPickle.load(data)
    return data

#reading each pkl file
#rating_df = decompress_pickle(rating_df_path) 
similarity_scores = decompress_pickle(similarity_score_path) 
final_table =decompress_pickle(table_path)
#rating_df = decompress_pickle(table_path) 

# Create your views here.
# helper function

def recommender(artist_name,similarity_scores,final_table):
        #1. fetching index
        idx = np.where(final_table.index==artist_name)[0][0]
        #2. finding its similar ity score
        distances = similarity_scores[idx]
        #3. finding index and similarity score by sorting on similarity scores
        similar_artists = sorted(list(enumerate(similarity_scores[idx])), key=lambda x:x[1],reverse=True)[1:10]#ignoring 0th index since 0 is artist itself
        final_output = []
        for i in similar_artists:
            final_output.append(final_table.index[i[0]])

        return final_output
         
def home(request):
    return render(request,'src/index.html',{})


def predict(request):
    artist_name = request.GET['artist_name']
    print(final_table)
    recommendation = recommender(artist_name,similarity_scores=similarity_scores,final_table=final_table)
    return render(request,'src/index.html',{"recommended_artists":recommendation})

   