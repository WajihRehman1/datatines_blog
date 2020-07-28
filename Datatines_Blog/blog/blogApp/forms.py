from django import forms
from tinymce.widgets import TinyMCE
from .models import post, comment


class TinyMCEWidget(TinyMCE):
    def use_required_attribute(self, *args):
        return False


class PostForm(forms.ModelForm):
    content = forms.CharField(
        widget=TinyMCEWidget(
            attrs={'required': False, 'cols': 30, 'rows': 10}
        )
    )

    class Meta:
        model = post
        fields = '__all__'


class commentForm(forms.ModelForm):
    class Meta:
        model = comment
        fields = ('user', 'content','Post')
