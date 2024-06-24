from config import app, db
import routes

if __name__ == "__main__":
    with app.app_context():
        db.create_all() # Create all the models we have to find in our database - if we don't have the database created already

    app.run(port=5000)
