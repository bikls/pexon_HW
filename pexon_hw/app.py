from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

# DB Erstellung
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data/zertifikate.db'
db = SQLAlchemy(app)

class Zertifikate(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(300), nullable=False)

    def __repr__(self):
        return '<zertifikate %r>' % self.id



# App start

@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        certification_content = request.form['content']
        new_certification = Zertifikate(content=certification_content)

        try:
            db.session.add(new_certification)
            db.session.commit()
            return redirect('/')
        except:
            return 'DB ERROR'

    else:
        certificationHTML = Zertifikate.query.order_by(Zertifikate.id).all()
        return render_template('index.html', certification=certificationHTML)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
