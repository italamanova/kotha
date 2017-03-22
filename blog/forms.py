import datetime

from django import forms
from django.utils.translation import ugettext_lazy as _
from PIL import Image

from blog.models import Post, Comment


class DateInput(forms.DateInput):
    input_type = 'date'


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['author', 'text']
        widgets = {
            'author': forms.TextInput(attrs={'placeholder': 'Name'}),
            'text':forms.TextInput(attrs={'placeholder': 'Write message'}),
        }


class PostForm(forms.ModelForm):
    # image = forms.ImageField(label=_('Image'), required=False,
    #                                 error_messages={
    #                                     'invalid': _("Image files only")},
    #                                 widget=forms.FileInput)
    class Meta:
        model = Post
        fields = ['author', 'title', 'text', 'published_date', 'category', ]#'image']
        widgets = {
            'created_date': DateInput(),
            'published_date': DateInput(),
        }

    # def clean(self):
    #     cleaned_data = super(PostForm, self).clean()
    #     start_date = cleaned_data.get('start_date')
    #     end_date = cleaned_data.get('end_date')
    #
    #     if end_date and start_date > end_date:
    #         self.add_error('end_date',
    #                        _('End date cant\'t be earlies than start date'))


