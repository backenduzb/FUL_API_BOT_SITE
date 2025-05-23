from django.db import models


class TeacherTopic(models.Model):

    topic_name = models.CharField(max_length=255)

    def __str__(self):
        return self.topic_name
    class Meta:
        verbose_name = "Kafedra"
        verbose_name_plural = "Kafedralar"
        
class TeacherUsersStats(models.Model):
    full_name = models.CharField(max_length=100)

    updated_at = models.DateTimeField(auto_now=True)
    topics = models.ManyToManyField(TeacherTopic, blank=True) 
    telegram_id = models.CharField(max_length=20, default="0")


    full_name = models.CharField(max_length=100)
    telegram_id = models.CharField(max_length=20, default="0")
    updated_at = models.DateTimeField(auto_now=True)
    topics = models.ManyToManyField(TeacherTopic, blank=True)

    m1_juda_yaxshi = models.IntegerField(default=0)
    m1_yaxshi = models.IntegerField(default=0)
    m1_ortacha = models.IntegerField(default=0)
    m1_past = models.IntegerField(default=0)
    m1_yomon = models.IntegerField(default=0)

    m2_juda_yaxshi = models.IntegerField(default=0)
    m2_yaxshi = models.IntegerField(default=0)
    m2_ortacha = models.IntegerField(default=0)
    m2_past = models.IntegerField(default=0)
    m2_yomon = models.IntegerField(default=0)

    m3_juda_yaxshi = models.IntegerField(default=0)
    m3_yaxshi = models.IntegerField(default=0)
    m3_ortacha = models.IntegerField(default=0)
    m3_past = models.IntegerField(default=0)
    m3_yomon = models.IntegerField(default=0)

    m4_juda_yaxshi = models.IntegerField(default=0)
    m4_yaxshi = models.IntegerField(default=0)
    m4_ortacha = models.IntegerField(default=0)
    m4_past = models.IntegerField(default=0)
    m4_yomon = models.IntegerField(default=0)

    m5_juda_yaxshi = models.IntegerField(default=0)
    m5_yaxshi = models.IntegerField(default=0)
    m5_ortacha = models.IntegerField(default=0)
    m5_past = models.IntegerField(default=0)
    m5_yomon = models.IntegerField(default=0)

    m6_juda_yaxshi = models.IntegerField(default=0)
    m6_yaxshi = models.IntegerField(default=0)
    m6_ortacha = models.IntegerField(default=0)
    m6_past = models.IntegerField(default=0)
    m6_yomon = models.IntegerField(default=0)

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = "O'qituvchining statistikasi"
        verbose_name_plural = "O'qituvchilarning statistikasi"
        ordering = ['-updated_at']

