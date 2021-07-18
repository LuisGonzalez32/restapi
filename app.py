from flask import Flask
from flask_restful import Api
from resources.books_resource_pdf import BooksPdf
from resources.books_resource_audio import BooksAudio

app = Flask(__name__)
api = Api(app)

api.add_resource(BooksPdf, "/pdf/<string:nombre>")

api.add_resource(BooksAudio, "/audio/<string:nombre>")


if __name__ == "__main__":
    app.run(debug=True, port=23512)