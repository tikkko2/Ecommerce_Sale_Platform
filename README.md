# Ecommerce_Sale_Platform
Completed

In the course SL, we had implement a website that would be company's sales platform. With this information we created what we could in a certain timeframe without much knowledge. So first we will talk about:
* How to start your own server
* How can you open our project and start it on your local:server so it can work for you.
* How to open admin panel and use it to add items/super-users/products for your desire.
### Enviroment setup
You will need:
* python installed
* django - `pip install Django==4.0.5`
* pillow - `pip install Pillow==9.1.1`
* open terminal in project folder

### How to start server
run the following commands in the terminal in project folder (if python command not working try python3)
* `python manage.py makemigrations`
* `python manage.py migrate`
* `python manage.py createsuperuser` (you can skip this step if you don't want admin powers)
* `python manage.py runserver`

