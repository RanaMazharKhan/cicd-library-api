from django.http import HttpResponse, JsonResponse



def home(request):
    # Someone visited the homepage - say hello
    return HttpResponse("Welcome to my Library API!")


def health(request):
    # A special checkpoint - other tools (like our future pipeline)
    # can visit this to ask "are you alive and working?"
    return JsonResponse({"status": "ok"})
