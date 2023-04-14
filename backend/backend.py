from .api import api
from .db import Db
from .webserver import Server


class Backend:
    def __init__(
        self,
        host: str = "localhost",
        port: int = 8080,
        spa_path: str = "frontend/dist",
        index_file: str = "index.html",
        db_path: str = 'sqlite:///database.db',
        model_path: str = 'backend/models'
    ):
        self.__server = Server(host, port, spa_path, index_file)
        Db.set_file_path(db_path)
        Db.set_model_path(model_path)

    def start(self, threading: bool = False):
        self.__server.register_blueprint(api, "/api")

        # add a custom 404 method, fires when given route is request prefix
        @self.__server.errorhandler("/api", 404)
        def not_found(e):
            return e

        Db.start()

        self.__server.start(threading)

    def stop(self):
        self.__server.stop()
