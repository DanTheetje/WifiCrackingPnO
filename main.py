from website import create_app  

app = create_app()

if __name__ == '__main__':
    app.run(debug=True) #This causes the server to be restarted everytime a change is made to the code
