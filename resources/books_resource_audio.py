from flask_restful import Resource, reqparse
from logic.books_logic_audio import BooksLogicAudio


class BooksAudio(Resource):
    def __init__(self):
        self.city_put_args = self.createParser()
        self.logic = BooksLogicAudio()

    def createParser(self):
        args = reqparse.RequestParser()
        args.add_argument("nombre", type=str, help="nombre del libro")
        args.add_argument("parte", type=str, help="archivo del libro")
        args.add_argument("archivo", type=str, help="partes del libro")
        args.add_argument("idioma", type=str, help="idioma del libro")
        args.add_argument("precio", type=int, help="precio del libro")
        return args

    def get(self, nombre):
        result = self.logic.getBooksByName(nombre)
        return result, 200

    def post(self, name):
        result = self.logic.getBooksById(name)
        return result, 200
