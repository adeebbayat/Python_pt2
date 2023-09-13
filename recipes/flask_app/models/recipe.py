from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash


class Recipe:
    def __init__(self,data):
        self.id = data['id']
        self.name = data['name']
        self.description = data['description']
        self.under = data['under']
        self.posted_by = data['posted_by']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def save(cls,data):
        query = """INSERT INTO recipes (name,description,under,posted_by,created_at,updated_at) 
        VALUES (%(name)s,%(description)s,%(under)s,%(posted_by)s,NOW(),NOW());"""
        return connectToMySQL("recipes_schema").query_db(query, data)
    
    @classmethod
    def get_info(cls,data):
        query = """SELECT * FROM recipes"""
        return connectToMySQL("recipes_schema").query_db(query, data)
    
    @classmethod
    def update_info(cls,data):
        query = """UPDATE recipes
        SET name = %(name)s,description = %(description)s,under = %(under)s,posted_by=%(posted_by)s
        WHERE id = %(id)s"""
        return connectToMySQL("recipes_schema").query_db(query, data)
