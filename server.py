from flask import Flask
from flask import render_template
from flask import Response, request, jsonify
import re
app = Flask(__name__)


searchData = {}
currentid = 10
data = {"1": {
        "id": "1",
        "name": "Golden Oolong Tea With Cheese Mousse",
        "image": "https://media-cdn.grubhub.com/image/upload/d_search:browse-images:default.jpg/w_150,q_auto:low,fl_lossy,dpr_2.0,c_fill,f_auto,h_130/d4tlchrehzscazmzlois ",
        "brand": "Sugar Tiger",
        "description": "Golden Oolong with Cheese Foam, known as Cheese Golden Phoenix Tea, is an exquisite fusion of traditional and modern flavors. The base of this beverage is a high-quality Golden Oolong tea, celebrated for its fragrant aroma and deep, mellow taste. Topped with a rich and creamy cheese foam, this tea offers a delightful contrast of savory and sweet, enhancing the overall sipping experience. The cheese foam's velvety texture complements the smoothness of the oolong, creating a unique and memorable flavor profile. Ideal for adventurous tea lovers, this drink merges the best of both worlds, offering a luxurious twist on classic tea enjoyment.",
        "price": [0, 5.9, 6.9],
        "rate": "8.1",
        "similar milk tea ids": ["2", "3", "4"],
        "publish time": "2020-10-11",
        "reviews": ["Absolutely amazing! The Golden Oolong tea was so fragrant and smooth, and the cheese foam added a rich, creamy texture that I've never experienced in a tea before. A must-try for any tea lover!", "Was a bit skeptical about the cheese foam at first, but it perfectly complements the Golden Oolong. The combination creates a surprisingly delightful balance of flavors. Definitely coming back for more!", "The Cheese Golden Phoenix Tea is a game-changer. The depth of the oolong with the light, salty sweetness of the cheese foam is beyond delicious. It's like nothing I've ever tasted, in the best way possible.", "I'm a huge fan of oolong tea, and the Golden Oolong with Cheese Foam did not disappoint! The cheese foam is creamy and not overly sweet, which perfectly balances the tea's natural bitterness. Highly recommend.", "Tried the Cheese Golden Phoenix Tea on a friend's recommendation and was pleasantly surprised. The oolong is of excellent quality, and the cheese foam adds a unique twist that elevates the entire drink. A refreshing and innovative blend that's both satisfying and indulgent."],
        "ingredients": ["Golden Oolong Tea", "Cream Cheese Foam", "Sea Salt"],
        },
        "2": {
        "id": "2",
        "name": "Jasmine Green Tea with Lychee Frost",
        "image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSly1tsMnL0HFIlPMwBAOBB81umpS5oKp-dfW1YNS2UMCSpH5dCeBareszAPRWStYwzc9s&usqp=CAU",
        "brand": "Fruity Teas",
        "description": "Jasmine Green Tea with Lychee Frost combines the fragrant, delicate aroma of Jasmine green tea with the sweet, refreshing taste of lychee fruit. Topped with a light and frosty lychee-infused topping, this drink is a perfect blend of floral and fruity flavors, providing a refreshing and aromatic experience. Ideal for those who enjoy a hint of sweetness and a touch of exotic flavors in their tea.",
        "price": [0, 4.5, 5.5],
        "rate": "9.0",
        "similar milk tea ids": ["1", "3", "6"],
        "publish time": "2021-06-15",
        "reviews": ["Refreshing and light, the Jasmine tea pairs perfectly with the sweet lychee. A great drink for summer days!", "The lychee frost adds a nice, cool twist to the traditional jasmine tea. Love the unique flavor combination!", "A must-try for jasmine tea enthusiasts looking for something new. The lychee frost is an excellent addition!"],
        "ingredients": ["Jasmine Green Tea", "Lychee Juice", "Frosty Lychee Topping"],
},
    "3": {
        "id": "3",
        "name": "Classic Milk Tea with Boba Pearls",
        "image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQBAVU_lHqTe41ldoptGw5WS_iHqW3nAVxosw&usqp=CAU",
        "brand": "Boba King",
        "description": "Our Classic Milk Tea with Boba Pearls is a timeless favorite. Made with premium black tea and smooth, creamy milk, this classic beverage is complemented by sweet, chewy boba pearls for the perfect texture contrast. It's a comforting, familiar treat that never goes out of style, offering a satisfyingly sweet and creamy experience with every sip.",
        "price": [0, 3.5, 4.5],
        "rate": "8.5",
        "similar milk tea ids": ["1", "2", "7"],
        "publish time": "2021-09-20",
        "reviews": ["The classic milk tea never disappoints, and the boba pearls are just the right level of sweetness and chewiness.", "A solid choice for any boba tea lover. It's the perfect balance of tea, milk, and sweetness.", "You can't go wrong with the classic. It's my go-to comfort drink."],
        "ingredients": ["Black Tea", "Fresh Milk", "Tapioca Pearls", "Honey"],
},
    "4": {
        "id": "4",
        "name": "Matcha Green Tea Latte",
        "image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTM_sfVF4mLVLFPTJXoLf9UdQCr-7S2F2XEDg&usqp=CAU",
        "brand": "Green Zen",
        "description": "Our Matcha Green Tea Latte is a smooth, creamy delight, blending the rich, earthy flavors of premium matcha with the soft, milky texture of a classic latte. Perfect for matcha lovers and newcomers alike, this drink offers a powerful antioxidant boost with a gentle caffeine lift, providing a wholesome, energizing start to your day or a refreshing mid-afternoon pick-me-up.",
        "price": [0, 5.0, 6.0],
        "rate": "9.2",
        "similar milk tea ids": ["1", "2", "3"],
        "publish time": "2022-01-08",
        "reviews": ["The matcha latte was creamy and had the perfect amount of sweetness. Definitely one of the best I've had.", "Rich in flavor and smooth in texture, this matcha latte is a real treat for green tea enthusiasts.", "Loved every sip of this matcha latte! It's energizing without being overpowering."],
        "ingredients": ["Matcha Green Tea", "Fresh Milk", "Sweetened Condensed Milk"]
}, "5": {
        "id": "5",
        "name": "Caramel Honey Black Tea",
        "image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTYbgu_HUJxMGjNIHWbJW0tz1_MZR6zcqWpkA&usqp=CAU",
        "brand": "Sweet Bee",
        "description": "Caramel Honey Black Tea is a sweet and aromatic drink combining the rich depth of black tea with the smooth sweetness of caramel and the natural essence of honey. This delightful beverage offers a perfect balance of flavors, making it an irresistible treat for anyone with a sweet tooth.",
        "price": [0, 4.0, 5.0],
        "rate": "8.7",
        "similar milk tea ids": ["1", "2", "4"],
        "publish time": "2022-04-10",
        "reviews": [
            "The caramel and honey blend seamlessly with the black tea for a truly comforting drink.",
            "Sweet, but not too sweet. The caramel honey black tea is my new afternoon pick-me-up!",
            "Loved the depth of flavor in this tea! The caramel isn't overpowering, and the honey adds just the right touch of sweetness.",
            "This tea is a perfect sweet treat without being too heavy. Great for a relaxing evening."
        ],
        "ingredients": ["Black Tea", "Caramel Syrup", "Honey", "Cream"]
},
    "6": {
        "id": "6",
        "name": "Peach Oolong Iced Tea",
        "image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT-blmJsAwA5JBjHo-hUbdTINoXXtfWFLb_nQ&usqp=CAU",
        "brand": "Fruity Teas",
        "description": "Peach Oolong Iced Tea is a refreshing and fruity beverage, perfect for cooling down on a hot day. Made with high-quality oolong tea and infused with natural peach flavors, this drink is both invigorating and delicious, offering a sweet yet slightly tart taste.",
        "price": [0, 4.2, 5.2],
        "rate": "9.1",
        "similar milk tea ids": ["2", "3", "5"],
        "publish time": "2022-06-30",
        "reviews": [
            "Absolutely refreshing! The peach flavor is natural and complements the oolong tea beautifully.",
            "This is the perfect summer drink - light, fruity, and incredibly refreshing!",
            "I'm typically not a huge fan of fruity teas, but this peach oolong changed my mind. Love it!",
            "The balance between the peach flavor and the tea is spot on. Not too sweet, just perfect."
        ],
        "ingredients": ["Oolong Tea", "Natural Peach Flavor", "Mint Leaves"]
},
    "7": {
        "id": "7",
        "name": "Spiced Chai Latte",
        "image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSkucAv3uS55jkn0mGy6q42jh7SrueIrtxuMg&usqp=CAU",
        "brand": "Chai Corner",
        "description": "Our Spiced Chai Latte is a warm and comforting drink, rich in flavor and perfect for chilly days. Made with a blend of black tea and aromatic spices like cinnamon, cardamom, and ginger, then frothed with creamy milk, this latte is both soothing and invigorating.",
        "price": [0, 4.5, 5.5],
        "rate": "8.9",
        "similar milk tea ids": ["1", "4", "6"],
        "publish time": "2022-09-15",
        "reviews": [
            "The perfect blend of spices makes this chai latte stand out. Warm and comforting!",
            "This spiced chai latte is the real deal. Love the authentic flavor and creamy texture.",
            "Just the right amount of spice and sweetness. It's become my go-to drink for cold mornings.",
            "I never knew I needed a spiced chai latte until I tried this one. Absolutely delicious!"
        ],
        "ingredients": ["Black Tea", "Cinnamon", "Cardamom", "Ginger", "Milk"],
},
    "8": {
    "id": "8",
    "name": "Vanilla Almond Milk Tea",
    "image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT4M8OyUjkENp-9vBjQeQ7PqAGNjLjRqQu09gX4268d4bXIMHrllJrTsr-Ri_CragqMADg&usqp=CAU",
    "brand": "Nutty Brews",
    "description": "Our Vanilla Almond Milk Tea combines the smooth, comforting flavor of vanilla with the nutty, rich taste of almond. This dairy-free delight is perfect for those who enjoy a lighter, plant-based alternative to traditional milk tea. The subtle sweetness and creamy texture make it a favorite among health-conscious tea lovers.",
    "price": [0, 4.5, 5.5],
    "rate": "8.6",
    "similar milk tea ids": ["2", "5", "7"],
    "publish time": "2023-01-05",
    "reviews": [
        "The vanilla flavor is just right – not too strong but noticeable, and I love the hint of almond.",
        "A great option for those who prefer plant-based milk. It’s creamy and delicious!",
        "I was pleasantly surprised by how well the almond and vanilla paired with the tea. Will definitely order again.",
        "Light, refreshing, and the flavors balance perfectly. A new favorite for sure!"
    ],
    "ingredients": ["Black Tea", "Vanilla Extract", "Almond Milk"]
},
    "9": {
    "id": "9",
    "name": "Berry Blast Black Tea",
    "image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQlzKZLdzA-lvSy9w_butDtJPfDiAWA9PAlbQ&usqp=CAU",
    "brand": "Fruity Teas",
    "description": "Berry Blast Black Tea is a vibrant, fruity beverage that combines the bold flavor of black tea with the natural sweetness of mixed berries. This refreshing drink is perfect for those who enjoy a fruity twist on their tea. Loaded with antioxidants and bursting with flavor, it’s a great pick-me-up at any time of day.",
    "price": [0, 4.7, 5.7],
    "rate": "9.0",
    "similar milk tea ids": ["1", "3", "8"],
    "publish time": "2023-02-12",
    "reviews": [
        "Absolutely refreshing! The mix of berries is perfect and not too overpowering.",
        "I love the natural sweetness of this tea. It’s become my afternoon staple.",
        "The berry flavors are vivid and refreshing, making it a perfect summer drink.",
        "This tea is both beautiful to look at and delicious to drink. Love the burst of berry flavors!"
    ],
    "ingredients": ["Black Tea", "Mixed Berries", "Lemon Zest"],
},
    "10": {
    "id": "10",
    "name": "Ginger Lemon Green Tea",
    "image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSiimkyE7gak9iXmJS9YeA9DP5HaJGZOwjAWA&usqp=CAU",
    "brand": "Zesty Blends",
    "description": "Our Ginger Lemon Green Tea is a zesty, invigorating drink that combines the soothing properties of green tea with the spicy kick of ginger and the refreshing zing of lemon. This detoxifying beverage is perfect for those looking for a healthy, flavorful way to stay hydrated and boost their immune system.",
    "price": [0, 4.0, 5.0],
    "rate": "8.8",
    "similar milk tea ids": ["2", "6", "9"],
    "publish time": "2023-03-20",
    "reviews": [
        "The perfect combination of flavors – it’s soothing, zesty, and packs a punch!",
        "I drink this for the health benefits, but the taste is a huge bonus. So refreshing!",
        "The ginger is not too overpowering, and the lemon adds just the right amount of tang.",
        "Love how refreshing this is! The ginger and lemon are a perfect pair."
    ],
    "ingredients": ["Green Tea", "Fresh Ginger", "Lemon Juice"],
}
}
# ROUTES
@app.route('/')
def homepage():
    global data
    return render_template('homepage.html', data=data)


@app.route('/view/<id>')
def item_detail(id):
    global data
    detail_data = data.get(id)
    return render_template('item_detail.html', detail_data=detail_data, data=data)


# AJAX FUNCTIONS
# ajax for search
@app.route('/search', methods=['GET'])
def search():
    global data
    query = request.args.get('query', '').lower().strip()
    search_ingredient = request.args.get('ingredient', '').lower().strip()
    search_brand = request.args.get('brand', '').lower().strip()
    search_results = {}
    search_case = query

    for item_id, item in data.items():
        match = False
        if search_ingredient:
            match = any(search_ingredient == ingredient.lower()
                        for ingredient in item['ingredients'])
            search_case = search_ingredient
            if match:
                highlighted_item = {
                    'name': item['name'],
                    'brand': item['brand'],
                    'ingredients': ', '.join([highlight(ingredient, search_case) for ingredient in item['ingredients']]),
                    'image': item['image']
                }
                search_results[item_id] = highlighted_item

        elif search_brand:
            match = search_brand == item['brand'].lower()
            search_case = search_brand
            if match:
                highlighted_item = {
                    'name': item['name'],
                    'brand': highlight(item['brand'], search_case),
                    'ingredients': item['ingredients'],
                    'image': item['image']
                }
                search_results[item_id] = highlighted_item

        elif query:
            match = query in item['name'].lower() or query in item['brand'].lower() or any(
                query in ingredient.lower() for ingredient in item['ingredients'])

            if match:
                highlighted_item = {
                    'name': highlight(item['name'], search_case),
                    'brand': highlight(item['brand'], search_case),
                    'ingredients': ', '.join([highlight(ingredient, search_case) for ingredient in item['ingredients']]),
                    'image': item['image']
                }
                search_results[item_id] = highlighted_item
    return render_template('search_results.html', query=search_case, items=search_results, total=len(search_results))


def highlight(text, query):
    """Highlights the query in text."""
    highlighted = re.sub(
        f'({query})', r'<mark>\1</mark>', text, flags=re.IGNORECASE)
    return highlighted


@app.route('/add', methods=['GET', 'POST'])
def add_milk_tea():
    global currentid
    global data
    print(data)
    if request.method == 'POST':
        new_entry = request.get_json()
        currentid += 1
        new_id = str(currentid)
        new_entry['id'] = new_id
        new_entry['price'] = [0, 5.9, 6.9]
        new_entry['similar milk tea ids'] = ["1", "3", "6"]
        new_entry['publish time'] = "2020-10-11"
        new_entry['reviews'] = ["Refreshing and light, the Jasmine tea pairs perfectly with the sweet lychee. A great drink for summer days!",
                                "The lychee frost adds a nice, cool twist to the traditional jasmine tea. Love the unique flavor combination!", "A must-try for jasmine tea enthusiasts looking for something new. The lychee frost is an excellent addition!"]
        data[new_id] = new_entry
        print(new_entry)
        print(data)
        return jsonify(new_entry), 201

    return render_template('add.html')


@app.route('/edit/<id>', methods=['GET', 'POST'])
def edit_milk_tea(id):
    global data
    print(data)
    print(id)
    if request.method == 'POST':
        form_data = request.get_json()
        id = str(id)
        data[id]['name'] = form_data['name']
        data[id]['brand'] = form_data['brand']
        data[id]['description'] = form_data['description']
        data[id]['image'] = form_data['image']
        data[id]['rate'] = form_data['rate']
        data[id]['ingredients'] = form_data['ingredients']
        return jsonify(data[id])
    else:
        detail_data = data.get(id)
        print(detail_data)
        return render_template('edit.html', detail_data=detail_data)


if __name__ == '__main__':
    app.run(debug=True)
