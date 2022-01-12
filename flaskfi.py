from flask import Flask
app = Flask(__name__)
@app.route("/")
def hello_world():
    return "<h1>Hello World!</h1>"

@app.route("/home", methods=['POST','GET'])
def home_page():
    return "<h1>It is our home page!</h1>"

@app.route("/store")
def store():
    return "<h1>It is our Store!</h1>"

if __name__ == "__main__":
    app.run(debug=True)
# git bash here + git init დირექტორიაში შესაძლებელს ხდის გითის დაკვირვებას
# git status გვიჩვენებს რა დირექტორიები და ფაილებია მოცემულ დირექტორიაში (სამუშაო ადგილას)
# git add გადააქვს სასურველი ფაილი უბრალოდ სამუშაო ადგილიდან გითის თვალთვალის ქვეშ
# git commit -m "comment" სქრინშოთის გადაღება და კომენტირება,
# git config --global user.name"FIRST_NAME LAST_NAME" ... git config --global user.email"s.something@gmail.com"დაქომითებისთვის სახელის და ელფოსტის ჩაწერაა საჭირო, როდესაც ვწერთ გლობალს ერთჯერადად იწერება და ინახება კომპში
