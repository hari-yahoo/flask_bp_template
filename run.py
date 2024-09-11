from app import create_app, db

# Create an instance of the Flask application
app = create_app()

if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Create the database tables
    # Run the Flask application
    app.run(debug=True)
