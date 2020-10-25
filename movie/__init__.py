#__init__.py

import os
from flask import Flask, render_template

import movie.adapters.repository as repo
from movie.adapters.memory_repository import MemoryRepository, populate

def create_app():
    app = Flask(__name__)
    
    data_path = os.path.join('movie', 'adapters', 'data', 'Data1000Movies.csv')
    
    print(data_path)
    repo.repo_instance = MemoryRepository()
    populate(data_path, repo.repo_instance)
    
    @app.route("/")
    def index():
        return "<h1>Welcome</h1> \n <h4><a href=/hello>Click me</a></h4>"
    
    @app.route("/hello/")
    def hello():
        html_page = render_template(
            'hello.html',
            test = repo.repo_instance.get_movies(),
            desc = repo.repo_instance.get_movies().description,
            direc = repo.repo_instance.get_movies().director,
            actor = repo.repo_instance.get_movies().actors,
            genre = repo.repo_instance.get_movies().genres
            )
        return html_page
    
    return app
