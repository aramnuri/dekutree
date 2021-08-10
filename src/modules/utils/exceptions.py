import sys
import urllib.request


def exception_url(func):
    def inner_function(*args, **kwargs):
        try:
            func(*args, **kwargs)
        except ValueError as e:
            sys.stderr.write('ValueError: {0}\n'.format(e))
            return None
        except urllib.error.URLError as e:
            sys.stderr.write('urllib.error.UrlError: {0} ({1})\n'.format(e, args[0]))  # download_url = args[0]
            return None
        except urllib.error.HTTPError as e:
            sys.stderr.write('urllib.error.HTTPError: {0}\n'.format(e))
        except urllib.error.ContentTooShortError as e:
            sys.stderr.write('urllib.error.ContentTooShortError: {0}\n'.format(e))
    return inner_function
