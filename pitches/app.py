from app import create_app

# Creating app instance
app = create_app('development')

manager = Manager(app)


if __name__ == '__main__':
    app.run(debug=True)
