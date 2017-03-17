from pyramid.config import Configurator
import blue_yellow_app.controllers.home_controller as home
import blue_yellow_app.controllers.albums_controller as album


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    config = Configurator(settings=settings)

    init_includes(config)
    init_routing(config)

    return config.make_wsgi_app()


def init_routing(config):
    config.add_static_view('static', 'static', cache_max_age=3600)

    # config.add_route('index', '/')
    # config.add_route('box', '/box-model')
    # config.add_route('selectors', '/selectors')
    # config.add_route('layout', '/layout')
    # config.add_route('float', '/float')

    config.add_handler('root', '/', handler=home.HomeController, action='index')
    config.add_handler('home_ctrl', '/home/{action}', handler=home.HomeController)
    config.add_handler('home_ctrl/', '/home/{action}/', handler=home.HomeController)
    config.add_handler('home_ctrl_id/', '/home/{action}/{id}', handler=home.HomeController)


    # TODO: FIX THIS?
    # config.add_handler('albums', '/home/albums', handler=album.AlbumController, action='albums')
    # config.add_handler('albums/', '/home/albums/', handler=album.AlbumController, action='albums')
    #
    # config.add_handler('album_ctrl', '/home/albums/{action}', handler=album.AlbumController)
    # config.add_handler('album_ctrl/', '/home/albums/{action}/', handler=album.AlbumController)
    # config.add_handler('album_ctrl_id/', '/home/albums/{action}/{id}', handler=album.AlbumController)

    config.scan()


def init_includes(config):
    config.include('pyramid_chameleon')
    config.include('pyramid_handlers')
