from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    # return HttpResponse("Home Page")

    # return render(request, "index.html") # Projede bulunan her uygulama
    # kendi templates dosyasına sahip olabilir. Bu yüzden burada
    # hangi uygulamanın templates dosyasındaki hangi html dosyasını
    # çağırmak istiyorsak onu belirtmeliyiz. Bu yüzden render fonksiyonu
    # içerisinde ilk parametre request, ikinci parametre ise çağırılacak
    # html dosyasının adıdır. Bu html dosyası projedeki herhangi bir uygulamanın 
    # templates dosyası içerisinde bulunmalıdır.
    # settings.py dosyasındaki 'APP_DIRS': True, ayarı sayesinde bu gerçekleşir.

    # Projenin ana dizininde bir uygulama içerisinde olmadan bir TEMPLATES klasörü
    # oluşturarak html dosyalarındaki aynı kısımları tek bir yerden yönetebiliriz yani
    # sürekli aynı şeyi farklı yerlerde yazmak zorunda kalmayız.
    # Bunu da setting.py dosyasında 'DIRS': [], kısmına BASE_DIR / "templates"
    # komutunu eklemeliyiz.

    # Uygulamayı belirtmek için aşağıdaki şekilde belirtilebilir:
    return render(request, "blog/index.html")

def blogs(request):
    # return HttpResponse("Blogs")
    return render(request, "blog/blogs.html")

def blog_details(request, id):
    # return HttpResponse("Blog Details: " + str(id))
    return render(request, "blog/blog-details.html", {
            "ID": id
        })
