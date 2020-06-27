from django.views.generic import TemplateView



class MainPageView(TemplateView):
    template_name = "main.html"


class PageView(TemplateView):
    def get_template_names(self):
        template_name = "generated/results_{}.html".format(self.kwargs["page_name"])
        return [template_name]
