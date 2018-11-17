from django.http import HttpResponseRedirect


REDIRECT_PATH = "https://vk.com"


def redirect(request, name):
    return HttpResponseRedirect(f'{REDIRECT_PATH}{request.path}')
