from django.views.generic import TemplateView, FormView
from django.shortcuts import redirect
from .forms import UserInputForm

class MainPageView(TemplateView):
    template_name = "main.html"


class PageView(TemplateView):
    def get_template_names(self):
        template_name = "generated/results_{}.html".format(self.kwargs["page_name"])
        return [template_name]


class UserInputView(FormView):
    form_class = UserInputForm
    template_name = "input.html"

    def form_valid(self, form):
        #create your file here, but you need to put it into generated folder
        new_file_name = "20200101"

        return redirect("generated-files", new_file_name)


