from django.views.generic import TemplateView

class home(TemplateView):
    template_name = "index.html"

class origen(TemplateView):
    template_name = "origen.html"
    
class cervezas(TemplateView):
    template_name = "cervezas.html"
    
class eventos(TemplateView):
    template_name = "eventos.html"
    
class noticias(TemplateView):
    template_name = "noticias.html"
    
class contacto(TemplateView):
    template_name = "contacto.html"
    
class chopp(TemplateView):
    template_name = "chopp.html"
    
class lager(TemplateView):
    template_name = "lager.html"
    
class malzbier(TemplateView):
    template_name = "malzbier.html"