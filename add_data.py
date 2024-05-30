from models import db, Flashcard
from app import app

def add_drinks():
    drinks = [
        {
            "dish": "Drink",
            "beverage": "The Original Mango Bango",
            "ingredients": "Made with Rum. Add a floater of Rum for more bango!",
            "category": "Bar Beverages"
        },
        {
            "dish": "Drink",
            "beverage": "Maui Mango Bango",
            "ingredients": "Mango Bango with Captain Morgan, Coconut Rum, Strawberry Puree, Coconut Water",
            "category": "Bar Beverages"
        },
        {
            "dish": "Drink",
            "beverage": "Pain Killer",
            "ingredients": "Captain Morgan Coconut Rum, Fresh Cream of Coconut, Pineapple Juice and a Toasted Coconut Rim",
            "category": "Bar Beverages"
        },
        {
            "dish": "Drink",
            "beverage": "Freak Tiki",
            "ingredients": "Captain Morgan Coconut Rum, Simple Syrup, Lemon, Orange Juice, Cranberry and Club Soda",
            "category": "Bar Beverages"
        },
        {
            "dish": "Drink",
            "beverage": "Alligator Juice",
            "ingredients": "A Special Concoction... Captain Morgan Coconut Rum, Pineapple Juice, Melon and Blue Curacao",
            "category": "Bar Beverages"
        },
        {
            "dish": "Drink",
            "beverage": "Coronarita",
            "ingredients": "Our Famous Margarita Topped with a Corona, Frozen or on the Rocks",
            "category": "Bar Beverages"
        },
        {
            "dish": "Drink",
            "beverage": "Tres Amigos",
            "ingredients": "Our Frozen Sangria Swirled Together with our Frozen Margarita Topped with a Corona",
            "category": "Bar Beverages"
        },
        {
            "dish": "Drink",
            "beverage": "Pain in De Ass",
            "ingredients": "Strawberry Daiquiri combined with a Piña Colada",
            "category": "Bar Beverages"
        },
        {
            "dish": "Drink",
            "beverage": "Strawberry Daiquiri",
            "ingredients": "Our House Made Strawberry Mixture with Rum",
            "category": "Bar Beverages"
        },
        {
            "dish": "Drink",
            "beverage": "Piña Colada",
            "ingredients": "Best in the USA",
            "category": "Bar Beverages"
        },
        {
            "dish": "Drink",
            "beverage": "Sangria",
            "ingredients": "Our fresh berries and wine blended together for your enjoyment",
            "category": "Bar Beverages"
        },
        {
            "dish": "Drink",
            "beverage": "Electric Lemonade",
            "ingredients": "Lemon Citrus Vodka, Fresh Lemon and Blue Curacao",
            "category": "Bar Beverages"
        },
        {
            "dish": "Drink",
            "beverage": "Sangrita",
            "ingredients": "Our fresh sangria and our fresh award winning margarita swirled together",
            "category": "Bar Beverages"
        },
        {
            "dish": "Drink",
            "beverage": "Energy Crush",
            "ingredients": "Smirnoff Orange Vodka, Triple Sec, Orange Juice, Lemon-Lime Soda and Orange Energy Drink",
            "category": "Bar Beverages"
        },
        {
            "dish": "Drink",
            "beverage": "Blueberry Lemonade Energy Crush",
            "ingredients": "Blueberry Energy Drink, Fresh Blueberries with Deep Eddy Lemon Vodka and a dash of Pink Lemonade",
            "category": "Bar Beverages"
        },
        {
            "dish": "Drink",
            "beverage": "Mango Crush",
            "ingredients": "Smirnoff Vodka, Mango Puree, Triple Sec and Lemon-Lime Soda",
            "category": "Bar Beverages"
        },
        {
            "dish": "Drink",
            "beverage": "Orange Crush",
            "ingredients": "Smirnoff Orange Vodka, Fresh Squeeze Orange Juice, Triple Sec and Lemon-Lime Soda",
            "category": "Bar Beverages"
        },
        {
            "dish": "Drink",
            "beverage": "Julio's Crush",
            "ingredients": "Don Julio, Fresh Squeezed Orange Juice, Cranberry Juice, Pineapple Juice and Starry",
            "category": "Bar Beverages"
        },
        {
            "dish": "Drink",
            "beverage": "Piña Crush",
            "ingredients": "Captain Morgan Coconut Rum, Fresh Cream of Coconut, Pineapple Juice, Coconut Water and a Splash of Club Soda",
            "category": "Bar Beverages"
        },
        {
            "dish": "Drink",
            "beverage": "Grapefruit Crush",
            "ingredients": "Grapefruit Juice, Deep Eddy Ruby Red Vodka and Fresh Squeezed OJ",
            "category": "Bar Beverages"
        },
        {
            "dish": "Drink",
            "beverage": "Raspberry Mint Margarita",
            "ingredients": "Raspberries, mint and fresh lime juice",
            "category": "Bar Beverages"
        },
        {
            "dish": "Drink",
            "beverage": "Peach Fizz",
            "ingredients": "Peach puree and limes topped with our fresh squeezed lemonade",
            "category": "Bar Beverages"
        },
        {
            "dish": "Drink",
            "beverage": "Mango Bango",
            "ingredients": "Our famous Mango Bango short on the Bang",
            "category": "Bar Beverages"
        },
        {
            "dish": "Drink",
            "beverage": "Blackberry Mint Tea",
            "ingredients": "Blackberries, mint, and passion fruit Iced Tea",
            "category": "Bar Beverages"
        },
        {
            "dish": "Drink",
            "beverage": "Piña Colada",
            "ingredients": "Best in the USA made for all ages",
            "category": "Bar Beverages"
        },
        {
            "dish": "Drink",
            "beverage": "Blueberry Basil Limeade",
            "ingredients": "Our fresh squeezed lemonade with basil, blueberries and lime",
            "category": "Bar Beverages"
        },
        {
            "dish": "Drink",
            "beverage": "Watermelon Mojito",
            "ingredients": "Fresh watermelon puree, mint, lime and starry",
            "category": "Bar Beverages"
        }
    ]
    
    drinks.extend([
        {
            "dish": "Drink",
            "beverage": "Blackberry Moscow Mule",
            "ingredients": "Bulleit Bourbon, Blackberries, Lime Juice, Simple Syrup and Ginger Beer",
            "category": "Bar Beverages"
        },
        {
            "dish": "Drink",
            "beverage": "Deep Eddy Lemon Mule",
            "ingredients": "Deep Eddy Lemon Vodka, Ginger Beer and Mint",
            "category": "Bar Beverages"
        },
        {
            "dish": "Drink",
            "beverage": "Strawberry Moscow Mule",
            "ingredients": "Smirnoff Strawberry Vodka, Strawberries, Lime and Ginger Beer",
            "category": "Bar Beverages"
        },
        {
            "dish": "Drink",
            "beverage": "Peach Agave Moscow Mule",
            "ingredients": "Smirnoff Peach Vodka, Fresh Lime, Peach Puree and Ginger Beer",
            "category": "Bar Beverages"
        },
        {
            "dish": "Drink",
            "beverage": "Raspberry Mule",
            "ingredients": "Smirnoff Raspberry Vodka, Fresh Raspberry, Mint, Raspberry Puree, Lime and Ginger Beer",
            "category": "Bar Beverages"
        },
        {
            "dish": "Drink",
            "beverage": "Havana Mule",
            "ingredients": "Captain Morgan Pineapple Rum, Fresh Lime, Angostura Bitters, Orange Juice and Ginger Beer",
            "category": "Bar Beverages"
        },
        {
            "dish": "Drink",
            "beverage": "Mezcal Mule",
            "ingredients": "Ilegal Mezcal, Passion Fruit, Fresh Lime Juice and Ginger Beer",
            "category": "Bar Beverages"
        },
        {
            "dish": "Drink",
            "beverage": "Jalapeno Watermelon Mule",
            "ingredients": "Fresh Watermelon Juice, Jalapenos, Blanco Tequila and Ginger Beer",
            "category": "Bar Beverages"
        },
        {
            "dish": "Drink",
            "beverage": "Cosmo Martini",
            "ingredients": "Belvedere Vodka, Fresh Lime Juice, Cranberry Juice, Cane Syrup and a Lemon Twist",
            "category": "Bar Beverages"
        },
        {
            "dish": "Drink",
            "beverage": "Jalisco Martini",
            "ingredients": "Blanco Tequila, Fresh Lime Juice and Raspberry Puree",
            "category": "Bar Beverages"
        },
        {
            "dish": "Drink",
            "beverage": "Sour Apple Martini",
            "ingredients": "Smirnoff Vodka and Sour Apple Schnapps",
            "category": "Bar Beverages"
        },
        {
            "dish": "Drink",
            "beverage": "Tropical Martini",
            "ingredients": "Ketel One Vodka, Captain Morgan Coconut Rum, Blue Curacao and Pineapple Juice with Fresh Pineapple and Rimmed with Toasted Coconut",
            "category": "Bar Beverages"
        },
        {
            "dish": "Drink",
            "beverage": "Pomegranate Martini",
            "ingredients": "Smirnoff Pomegranate Vodka, Pomegranate Schnapps, Cranberry Juice and Lime",
            "category": "Bar Beverages"
        },
        {
            "dish": "Drink",
            "beverage": "Chocolate Martini",
            "ingredients": "Belvedere Vodka, Godiva Dark Chocolate Liqueur and Cream",
            "category": "Bar Beverages"
        },
        {
            "dish": "Drink",
            "beverage": "Smoke and Fire Martini",
            "ingredients": "Ilegal Mezcal, Pineapple Juice, Fresh Jalapenos with a Tajin Rim",
            "category": "Bar Beverages"
        },
        {
            "dish": "Drink",
            "beverage": "Blueberry Lemon Mojito",
            "ingredients": "Captain Morgan White Rum, with Blueberries, Mint, Club Soda and Lemon",
            "category": "Bar Beverages"
        },
        {
            "dish": "Drink",
            "beverage": "Hawaiian Pineapple Mojito",
            "ingredients": "Captain Morgan Pineapple Rum, Pineapple Juice, Agave Nectar, Fresh Lime and Fresh Mint",
            "category": "Bar Beverages"
        },
        {
            "dish": "Drink",
            "beverage": "Lemonade Mojito",
            "ingredients": "Limoncello, Captain Morgan Coconut Rum, Fresh Mint and Fresh Lemon",
            "category": "Bar Beverages"
        },
        {
            "dish": "Drink",
            "beverage": "Fresh Orange Mojito",
            "ingredients": "Smirnoff Orange Vodka, Fresh Oranges, Fresh Mint, Cane Sugar, Lime Wedges and Club Soda",
            "category": "Bar Beverages"
        },
        {
            "dish": "Drink",
            "beverage": "Coconut Mojito",
            "ingredients": "Captain Morgan Coconut Rum, Fresh Cream of Coconut, Mint, Lime and Club Soda",
            "category": "Bar Beverages"
        },
        {
            "dish": "Drink",
            "beverage": "Mango Mojito",
            "ingredients": "Rum, Mango Puree, Club Soda and Mint",
            "category": "Bar Beverages"
        },
        {
            "dish": "Drink",
            "beverage": "Berry Pickin Mojito",
            "ingredients": "Smirnoff Raspberry Vodka, Fresh Blackberries, Fresh Strawberries, Club Soda and Mint Leaves",
            "category": "Bar Beverages"
        },
        {
            "dish": "Drink",
            "beverage": "Strawberry Coconut Mojito",
            "ingredients": "Captain Morgan Coconut Rum, Muddled Strawberries, Club Soda and Lime",
            "category": "Bar Beverages"
        },
        {
            "dish": "Drink",
            "beverage": "Single Lady Sangria",
            "ingredients": "Ketel One Vodka, Rose, Raspberry Liqueur, Pineapple Syrup, Club Soda, Strawberries and Raspberries",
            "category": "Bar Beverages"
        },
        {
            "dish": "Drink",
            "beverage": "Pina Colada Sangria",
            "ingredients": "Moscato, Pineapple Juice, Fresh Cream of Coconut, Captain Morgan Coconut Rum, with Rimmed Coconut",
            "category": "Bar Beverages"
        },
        {
            "dish": "Drink",
            "beverage": "Blueberry Sangria",
            "ingredients": "Moscato, Pineapple Juice, Tequila, Blueberries, Lemonade and Club Soda",
            "category": "Bar Beverages"
        },
        {
            "dish": "Drink",
            "beverage": "Siesta Key Sangria",
            "ingredients": "Tropical Rum, Fresh Orange Juice, Pineapple, Raspberries, Moscato Wine and Rimmed Coconut",
            "category": "Bar Beverages"
        },
        {
            "dish": "Drink",
            "beverage": "Strawberry Sangria",
            "ingredients": "Fresh Strawberries, Lambrusco, Pineapple Juice, Lemonade, Strawberry Puree, Strawberry Vodka and Ginger Ale",
            "category": "Bar Beverages"
        },
        {
            "dish": "Drink",
            "beverage": "Watermelon Sangria",
            "ingredients": "Blanco Tequila, Watermelon Puree, Fresh Lime Juice and Rose",
            "category": "Bar Beverages"
        }
    ])
    
    for drink in drinks:
        new_drink = Flashcard(dish=drink["dish"], beverage=drink["beverage"], ingredients=drink["ingredients"], category=drink["category"])
        db.session.add(new_drink)
    
    db.session.commit()
    print("Drinks added successfully!")


if __name__=="__main__":
    with app.app_context(): 
        add_drinks()