# Flas(k) Cards - Web application! :books:
* This is a web application for storing a collection of
online flash cards for studying.
* Use as you wish! You're the hacker :thumbsup:
* **The app is currently geared towards my pursuit for a fulfilling Software Engineer position, but can certainly be modified for other areas of study** 

## Features
* Python syntax highlighting using [Pygments](http://pygments.org/)
* Random Card upon refreshing the app on index.html 
* Querying based on pre defined category. (General vs Code)

## Usage
* `git clone https://github.com/RafaelBroseghini/Flask-Cards.git`
* `cd Flask-Cards`
* `pip install -r requirements.txt`
* `flask db init`
* `flask db migrate -m "users table"`
* `flask db migrate -m "cards table"`
* `flask db upgrade`
* `flask run`

## Future Add-ons
* Ability to divide into multiple study sessions.
* Ajax calls.
* ~~AuthO~~ -> _Done!_

## Contributing

1. :spaghetti: Fork this repo!
2. Create your feature branch: `git checkout -b my-new-feature`
3. Commit your changes: `git commit -m 'Add some feature'`
4. Push to the branch: `git push origin my-new-feature`
5. Submit a pull request :+1:
