import pyramid_handlers
import blue_yellow_app.infrastructure.static_cache as static_cache


class HomeController:
    def __init__(self, request):
        self.request = request

    @pyramid_handlers.action(renderer='templates/home/index.pt')
    def index(self):
        return {
            'value': 'HOME',
            'build_cache_id': static_cache.build_cache_id
        }

    @pyramid_handlers.action(renderer='templates/home/albums.pt')
    def about(self):
        return {
            'value': 'ALBUMS',
            'build_cache_id': static_cache.build_cache_id
        }

    @pyramid_handlers.action(renderer='templates/home/about.pt')
    def about(self):
        return {
            'value': 'ABOUT',
            'build_cache_id': static_cache.build_cache_id
        }

    @pyramid_handlers.action(renderer='templates/home/contact.pt')
    def contact(self):
        return {
            'value': 'CONTACT',
            'build_cache_id': static_cache.build_cache_id
        }