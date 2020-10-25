import abc
from typing import List

from movie.domain.model import Director, Genre, Actor, Movie

repo_instance = None


class RepositoryException(Exception):

    def __init__(self, message=None):
        pass
    
    
class AbstractRepository(abc.ABC):
    
    @abc.abstractmethod
    def add_movie(self, movie: Movie):
        raise NotImplementedError
    
    @abc.abstractmethod
    def add_actor(self, actor: Actor):
        raise NotImplementedError
    
    @abc.abstractmethod
    def add_director(self, director: Director):
        raise NotImplementedError
    
    @abc.abstractmethod
    def add_genre(self, genre: Genre):
        raise NotImplementedError
    
    @abc.abstractmethod
    def get_movies(self) -> Movie:
        raise NotImplementedError