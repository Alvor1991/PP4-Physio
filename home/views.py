from django.shortcuts import render

def home_view(request):
    """
    View to render the home page.
    Simply returns the rendered home.html template.
    """
    return render(request, 'home/home.html', {'banner_image': 'path/to/your/banner_image.jpg'})


