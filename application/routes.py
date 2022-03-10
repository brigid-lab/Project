from flask import render_template, request, redirect, url_for
from application import app, db
from application.models import Recipes, Ingredients
from application.models import RecipeForm, BasicForm, IngredientForm



@app.route('/')
def home():

    all_recipes=Recipes.query.all()

    return render_template('read.html', all_recipes= all_recipes)

#registering for website
#@app.route('/', methods=['GET', 'POST'])
@app.route('/register', methods=['GET', 'POST'])
def register():
    message = "Register here for Cozy Kitchen"
    form = BasicForm()

    if request.method == 'POST':
        first_name = form.first_name.data
        last_name = form.last_name.data

        if len(first_name) == 0 or len(last_name) == 0:
            message = "Please supply both first and last name"
        else:
            message = f'Thank you, {first_name} {last_name}'

    return render_template('register.html', form=form, message=message)




@app.route('/add_recipe', methods = ['GET','POST'])
def add_recipe():
    # instantiate the RecipeForm object
    form = RecipeForm()
    
    if form.validate_on_submit():
            # adds the recipe to the database
        recipe = Recipes(
            recipe_name = form.recipe_name.data,
            description = form.description.data,
            instructions = form.instructions.data 
        )    
       
        db.session.add(recipe)
        db.session.commit()
        return redirect(url_for ('home'))
          
    return render_template('add_recipe.html', form=form)

@app.route('/add_ingredient/<int:recipe_id>', methods = ['GET','POST'])
def add_ingredient(recipe_id):
    # instantiate the RecipeForm object
    form = IngredientForm()
    if form.validate_on_submit():
            # adds the recipe to the database
        ingredient = Ingredients(
            ingredient_name = form.ingredient_name.data,
            recipe_id = form.recipe_id.data 
        )    

        db.session.add(ingredient)
        db.session.commit()
        return redirect(url_for ('home')) 
    return render_template('add_ingredient.html', form=form)

@app.route('/ingredients/<int:recipe_id>', methods =['GET'])

def ingredients(recipe_id):
    all_ingredients=Ingredients.query.all()
    return render_template('read_ingredients.html', all_ingredients= all_ingredients)


@app.route('/delete_recipe/<int:id>')
def delete_recipe(id):
    recipe= Recipes.query.get(id)
    db.session.delete(recipe)
    db.session.commit()
    return redirect(url_for('home'))

@app.route('/delete_ingredient/<int:id>')
def delete_ingredient(id):
    ingredient= Ingredients.query.get(id)
    db.session.delete(ingredient)
    db.session.commit()
    return redirect(url_for('home'))    






@app.route('/update/<int:id>', methods = ['GET','POST'])
def update(id):
    form = RecipeForm()
    recipe = Recipes.query.get(id)
    if form.validate_on_submit():
        recipe.recipe_name = form.recipe_name.data
        recipe.description = form.description.data
        recipe.instructions = form.instructions.data
        db.session.commit()
        return redirect(url_for ('home'))
    elif request.method == 'GET':
        form.recipe_name.data = recipe.recipe_name
        form.description.data = recipe.description
        form.instructions.data = recipe.instructions
    return render_template('update_recipe.html',form=form)

@app.route('/update_ingredients/<int:id>', methods = ['GET','POST'])
def update_ingredients(id):
    form = IngredientForm()
    ingredient = Ingredients.query.get(id)
    if form.validate_on_submit():
        ingredient.ingredient_name = form.ingredient_name.data
        ingredient.recipe_id = form.recipe_id.data
        db.session.commit()
        return redirect(url_for ('home'))
    elif request.method == 'GET':
        form.ingredient_name.data = ingredient.ingredient_name
        form.recipe_id.data = ingredient.recipe_id
        
    return render_template('update_ingredient.html',form=form)