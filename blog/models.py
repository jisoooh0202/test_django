from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from django_ckeditor_5.fields import CKEditor5Field
from simple_history.models import HistoricalRecords


# Create your models here.
class Blog(models.Model):
    id: int
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    title = models.CharField(_("Title"), max_length=200)
    content = CKEditor5Field(_("Content"), config_name="extends", blank=True)
    author = models.CharField(
        get_user_model(),
        max_length=100,
    )
    history = HistoricalRecords(history_change_reason_field=models.TextField(null=True))

    def __str__(self):
        return self.title
