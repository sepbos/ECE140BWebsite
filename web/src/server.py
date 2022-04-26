from pyramid.config import Configurator
from pyramid.renderers import render_to_response
from pyramid.response import FileResponse
import mysql.connector as mysql
import os
from wsgiref.simple_server import make_server


db_user = os.environ['MYSQL_USER']
db_pass = os.environ['MYSQL_PASSWORD']
db_name = os.environ['MYSQL_DATABASE']
db_host = os.environ['MYSQL_HOST']


def kvp_page(req):
    return FileResponse("templates/kvp.html")


def product_page(req):
    return FileResponse("templates/product.html")


def empathyMapImg(req):
    return FileResponse("public/EmpathyMap.png")


def home_page(req):
    return FileResponse("templates/home.html")


if __name__ == '__main__':
    with Configurator() as config:
        config.add_route('home', '/')
        config.add_view(home_page, route_name='home')

        config.add_route('kvp', '/kvp')
        config.add_view(kvp_page, route_name='kvp', renderer='json')

        config.add_route('product', '/product')
        config.add_view(product_page, route_name='product', renderer='json')

        config.add_route('EmpathyMap', '/public/EmpathyMap.png')
        config.add_view(empathyMapImg, route_name='EmpathyMap')

        config.add_static_view(name='/', path='./public', cache_max_age=3600)
        app = config.make_wsgi_app()
    server = make_server('0.0.0.0', 6000, app)
    server.serve_forever()
