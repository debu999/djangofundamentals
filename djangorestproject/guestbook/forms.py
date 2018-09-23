from django import forms
from .models import Todo


class CommentForm(forms.Form):
    name = forms.CharField(max_length=20,
                           widget=forms.TextInput(attrs={"class": "form-control",
                                                         "placeholder": "Name"}))
    comment = forms.CharField(widget=forms.Textarea(attrs={"class": "form-control",
                                                           "placeholder": "Comment"}))


class TodoForm(forms.Form):
    text = forms.CharField(max_length=40,
                           widget=forms.TextInput(attrs={"style": "font-style:italic",
                                                         "class": "form-control",
                                                         "placeholder": "Enter ToDo e.g. Workout today.",
                                                         "aria-label": "Todo",
                                                         "aria-describedby": "add-btn"
                                                         }))


class NewTodoForm(forms.ModelForm):
    # text = forms.CharField(max_length=40,
    #                        widget=forms.TextInput(attrs={"style" : "font-style:italic",
    #                                                      "class": "form-control",
    #                                                      "placeholder": "Enter ToDo e.g. Workout today.",
    #                                                      "aria-label": "Todo",
    #                                                      "aria-describedby": "add-btn"
    #                                                      }))4
    todoid = forms.HiddenInput()
    class Meta:
        model = Todo
        fields = ["text", ]
        widgets = {
            "text": forms.TextInput(attrs={"style": "font-style:italic",
                                           "class": "form-control",
                                           "placeholder": "Enter ToDo e.g. Workout today.",
                                           "aria-label": "Todo",
                                           "aria-describedby": "add-btn"
                                           }),
            "todoid": forms.HiddenInput()
        }
