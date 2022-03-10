from application import db
from flask_wtf import FlaskForm
from wtforms import SelectField, StringField, SubmitField, IntegerField

class BasicForm(FlaskForm):
    first_name = StringField('First Name')
    last_name = StringField('Last Name')
    submit = SubmitField('Add Name')


class RecipeForm(FlaskForm):
    recipe_name =StringField("Recipe_Name")
    description = StringField("description")
    instructions = StringField("instructions")
    submit = SubmitField()

class IngredientForm(FlaskForm):
    ingredient_name= StringField("ingredient_name")
    recipe_id = IntegerField("recipe_id")
    submit = SubmitField()


class Recipes(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    recipe_name = db.Column(db.String(30),nullable= False)
    description = db.Column(db.String(300), nullable= False)
    instructions = db.Column(db.String(1000), nullable =False)
    

class Ingredients(db.Model):
    id = db.Column(db.Integer, primary_key =True)
    ingredient_name = db.Column(db.String(50), nullable =False)
    recipe_id = db.Column(db.Integer, db.ForeignKey('recipes.id'), nullable= False)
    add_to_recipes = db.relationship('Recipes', backref= 'ingredient')


    