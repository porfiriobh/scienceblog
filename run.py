from app import app
"""""
Even though flask is not in its very nature an MVC framework; code can be written in a particular order
to make it work as an MVC pattern. I expect to take the many advantages this desing has zfor our blog,
so from this point foward the file init will handle the different routes and paths.
"""""

if __name__ == '__main__':
    app.run(debug=True)