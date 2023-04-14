from threading import Thread

from cheroot.wsgi import PathInfoDispatcher
from cheroot.wsgi import Server as WSGIServer
from flask import Flask, request

from .db import Db


class Server:
    def __init__(
        self,
        host: str = "localhost",
        port: int = 8080,
        spa_path: str = "dist",
        index_file: str = "index.html",
    ):
        self.__server = None
        self.__host = host
        self.__port = port
        self.__app = Flask("main", static_folder=spa_path, static_url_path="/")
        self.__spa_path = spa_path
        self.__index_file = index_file
        self.__error_handlers = {}

    def start(self, threading: bool = False):
        if threading:
            Thread(target=self.start).start()
            return
        if not self.__server:
            self.__app.static_folder = self.__spa_path

            # catches all error codes
            @self.__app.errorhandler(Exception)
            def catch_all(e):
                if getattr(e, "code", None):
                    # sort in order of the number of / in the route prefix
                    sorted_route_prefixes = sorted(
                        self.__error_handlers.keys(),
                        key=lambda x: x.count("/"),
                        reverse=True,
                    )

                    for route_prefix in sorted_route_prefixes:
                        # if route prefix matches and the error code matches return the result of the stored function
                        if (
                            request.path.startswith(route_prefix)
                            and self.__error_handlers[route_prefix]["error_code"]
                            == e.code
                        ):
                            return self.__error_handlers[route_prefix]["func"](e)
                    # if no route prefixes match and error is 404, return the spa
                    if e.code == 404:
                        return self.__app.send_static_file(self.__index_file)

                # else just default behaviour (return the error)
                return e

            @self.__app.teardown_appcontext
            def shutdown_session(exception=None):
                Db.get_session().remove()

            d = PathInfoDispatcher({"/": self.__app})  # load in flask app
            self.__server = WSGIServer(
                (self.__host, self.__port), d
            )  # create webserver with dispatcher
            try:
                print("Server started at  ", self.__host, ":", self.__port)
                self.__server.start()
            except KeyboardInterrupt:
                self.stop()

    def stop(self):
        if self.__server:
            self.__server.stop()
            self.__server = None
            print("Server stopped")

    def restart(self):
        self.stop()
        self.start()

    # use as decorator e.g. @server.errorhandler('/api', 404)
    def errorhandler(self, route_prefix: str, error_code: int):
        if not route_prefix[0] == "/":
            route_prefix = "/" + route_prefix

        if route_prefix[-1] == "/":
            route_prefix = route_prefix[:-1]

        def inner(func):
            self.__error_handlers[route_prefix] = {
                "route_prefix": route_prefix,
                "error_code": error_code,
                "func": func,
            }

        return inner

    def get_spa_path(self) -> str:
        return self.__spa_path

    def set_spa_path(self, spa_folder: str):
        self.__spa_path = spa_folder
        self.__app.static_folder = spa_folder

    def set_index_file(self, index_file: str):
        self.__index_file = index_file

    def register_blueprint(self, blueprint, url_prefix: str = ""):
        self.__app.register_blueprint(blueprint, url_prefix=url_prefix)

    def get_host(self) -> str:
        return self.__host

    def get_port(self) -> int:
        return self.__port

    def set_host(self, host: str):
        self.__host = host
        if self.__server:
            self.restart()

    def set_port(self, port: int):
        self.__port = port
        if self.__server:
            self.restart()
