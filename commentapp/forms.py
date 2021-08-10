from django.forms import ModelForm

from commentapp.models import Comment


class CommentCreationForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
    #
    # def form_valid(self, form):
    #     form.instance.article = self.request.article
    #     form.instance.writer = self.request.writer
    #     return super().form_valid(form)