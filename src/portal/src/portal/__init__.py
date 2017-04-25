from pyramid.config import Configurator


def main(global_config, **settings):

    config = Configurator(settings=settings)
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.include(routes)
    config.scan()
    return config.make_wsgi_app()


def routes(config):
    config.add_route('home', '/')
