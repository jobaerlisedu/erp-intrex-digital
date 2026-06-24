from django.conf import settings
from urllib.parse import urlparse

class DynamicCsrfMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # 1. Check HTTP_ORIGIN header (sent by modern browsers for POST requests)
        origin = request.META.get('HTTP_ORIGIN')
        if origin:
            self._add_to_csrf_trusted(origin)
        
        # 2. Check HTTP_REFERER header as a fallback
        referer = request.META.get('HTTP_REFERER')
        if referer:
            parsed = urlparse(referer)
            if parsed.scheme and parsed.netloc:
                origin_from_referer = f"{parsed.scheme}://{parsed.netloc}"
                self._add_to_csrf_trusted(origin_from_referer)

        # 3. Check Host header as another fallback
        try:
            host = request.get_host()
            if host:
                self._add_to_csrf_trusted(f"https://{host}")
                self._add_to_csrf_trusted(f"http://{host}")
        except Exception:
            pass

        return self.get_response(request)

    def _add_to_csrf_trusted(self, origin):
        if origin:
            origin = origin.strip().rstrip('/')
            if origin not in settings.CSRF_TRUSTED_ORIGINS:
                # Safely append to Django's CSRF_TRUSTED_ORIGINS setting list/tuple
                trusted = list(settings.CSRF_TRUSTED_ORIGINS)
                trusted.append(origin)
                settings.CSRF_TRUSTED_ORIGINS = trusted
