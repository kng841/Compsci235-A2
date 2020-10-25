import csv
import os
import random

from typing import List

from movie.adapters.repository import AbstractRepository, RepositoryException
from movie.domain.model import Director, Genre, Actor, Movie


class MemoryRepository(AbstractRepository):
    
    def __init__(self):
        self._movies = list()
        self._actors = list()
        self._directors = list()
        self._genres = list()
        
    def add_movie(self, movie: Movie):
        if movie not in self._movies:
            self._movies.append(movie)
            
    def add_actor(self, actor: Actor):
        if actor not in self._actors:
            self._actors.append(actor)
            
    def add_director(self, director: Director):
        if director not in self._directors:
            self._directors.append(director)
            
    def add_genre(self, genre: Genre):
        if genre not in self._genres:
            self._genres.append(genre)
    
    def get_movies(self):
        return self._movies[random.randrange(1000)]

    
    
    
    




def load_all(file_name: str, repo: MemoryRepository):
    with open(file_name, mode='r', encoding='utf-8-sig') as csvfile:
        movie_file_reader = csv.DictReader(csvfile)

        for row in movie_file_reader:
            movie = Movie(row['Title'], int(row['Year']))
            movie.description = row['Description']
            movie.runtime_minutes = int(row['Runtime (Minutes)'])
                
            director = Director(row['Director'])
            repo.add_director(director)
            movie.director = director

            parsed_genres = row['Genre'].split(',')
            for genre_string in parsed_genres:
                genre = Genre(genre_string)
                repo.add_genre(genre)
                movie.add_genre(genre)

            parsed_actors = row['Actors'].split(',')
            for actor_string in parsed_actors:
                actor = Actor(actor_string)
                repo.add_actor(actor)
                movie.add_actor(actor)
                    
            repo.add_movie(movie)
                
               
                
def populate(file_name: str, repo: MemoryRepository):
    load_all(file_name, repo)
