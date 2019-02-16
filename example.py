from flask import Flask, render_template
app = Flask(__name__)

posts = [
    {
        'author': 'Charlie Sievers',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'dates_posted': 'April 5 1993'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'dates_posted': 'April 6 1993'
    }
]


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)


@app.route("/about")
def about():
    return render_template('about.html', title='About')


if __name__ == '__main__':
    app.run()
