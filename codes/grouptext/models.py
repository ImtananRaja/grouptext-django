from django.db import models


class TextGroup(models.Model):
    group_name = models.CharField(max_length=64)
    created_at = models.DateTimeField(auto_now_add=True)


class TextGroupMember(models.Model):
    text_group = models.ForeignKey(TextGroup, on_delete=models.CASCADE)
    member_name = models.CharField(max_length=64)
    member_phone = models.CharField(max_length=64)
    created_at = models.DateTimeField(auto_now_add=True)


class TextQuestion(models.Model):
    text_group = models.ForeignKey(TextGroup, on_delete=models.CASCADE)
    question = models.CharField(max_length=64)
    created_at = models.DateTimeField(auto_now_add=True)
    sent = models.BooleanField(default=False)
