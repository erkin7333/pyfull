

def title(request):
    return {
        "title": getattr(request, "title", "PyFull")
    }
