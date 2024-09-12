from django.shortcuts import render

# Create your views here.


def timer_view(request):
    """
    A function used to render the timer page
    Args:
        request (HttpRequest): The request object
    Returns:
        HttpResponse: The response object
    """
    # Render the timer page
    return render(request, 'focus_timer/timer.html')
