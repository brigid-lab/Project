from application import db 
from application.models import Recipes, Ingredients 

db.drop_all()
db.create_all()

#victoria_sandwich = Recipes(id = 1,recipe_name = 'Victoria Sandwich', description= 'a popular tea-time treat', instructions= 'Preheat oven to 160 Fan, grease and flour two 20cm sandwich tins, cream butter and sugar, beat eggs and add a ittle at a time to mixture, fold in flour, place in tins, bake for 25 minutesor until golden brown and firm to touch')
#db.session.add(victoria_sandwich)
#db.session.commit()#

#butter_250g = Ingredients(id = 1, ingredient_name = 'butter_250g',recipe_id =1, add_to_shoppinglist = False)
#castor_sugar_250g = Ingredients(id =2, ingredient_name = 'castor_sugar_250g',recipe_id =1, add_to_shoppinglist = True)
#large_eggs_4 = Ingredients(id = 3, ingredient_name = 'large_eggs_4',recipe_id = 1, add_to_shoppinglist=True)
#sr_flour_250g = Ingredients(id =4, ingredient_name = 'Self_raising_flour_250g', recipe_id =1,add_to_shoppinglist =False)

#db.session.add(butter_250g)
#db.session.add (castor_sugar_250g)
#db.session.add(large_eggs_4)
#db.session.add(sr_flour_250g)
###b.session.commit()



#print(f'Ingredients for a Victoria Sandwich Cake are: {victoria_sandwich.ingredients[0].ingredient_name},{victoria_sandwich.ingredients[1].ingredient_name},{victoria_sandwich.ingredients[2].ingredient_name},{victoria_sandwich.ingredients[3].ingredient_name}')
#print(f'Recipe for a victoria sandwich is: {victoria_sandwich.recipe_name},{victoria_sandwich.description},{victoria_sandwich.instructions}')