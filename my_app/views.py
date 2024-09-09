from django.shortcuts import HttpResponse

def first_page(request):
    response = """
        <h1>My first website</h1>
        <p>This site is best one in my project</p>
        <a href="/kitob/1">
        <ul>
          <li>Madaminbek Qonli gullar vodiysi</li>
        </ul>
        </a>
        <a href="/kitob/2">
        <ul>
          <li>Turkiston qayg'usi</li>
        </ul>
        </a>
        <a href="/kitob/3">
        <ul>
          <li>Buyuk shaxmat doskasi</li>
        </ul>
        </a>
    """
    return HttpResponse(response)

def Madaminbek_page(request):
    response = """
        <h1>Madaminbek Qonli gullar vodiysi</h1>
        <h2>author: Baxtiyor Abdug’afur</h2>
        <p>Madaminbek haqida batafsil ma'lumot...</p>
        <a href="/">Back</a>
    """
    return HttpResponse(response)

def ikkinchi_page(request):
    response = """
        <h1>My first website</h1>
        <p>This site is best one in my project</p>
        <a href="/kitob/2">
        <ul>
          <li>Turkiston qayg'usi</li>
        </ul>
        </a>
    """
    return HttpResponse(response)

def qaygusi_page(request):
    response = """
        <h1>Turkiston qayg‘usi</h1>
        <h2>author: Shokirov Uvaysxonto'ra</h2>
        <p>Turkiston qaygʻusi haqida batafsil ma'lumot...</p>
        <a href="/">Back</a>
    """
    return HttpResponse(response)

def uchinchi_page(request):
    response = """
        <h1>My first website</h1>
        <p>This site is best one in my project</p>
        <a href="/kitob/3">
        <ul>
          <li>Buyuk shaxmat doskasi</li>
        </ul>
        </a>
    """
    return HttpResponse(response)

def buyuk_page(request):
    response = """
        <h1>Buyuk shaxmat taxtasi</h1>
        <h2>author: Jimmi Karterning</h2>
        <p>"Buyuk shaxmat taxtasi" kitobi haqida batafsil...</p>
        <a href="/">Back</a>
    """
    return HttpResponse(response)
