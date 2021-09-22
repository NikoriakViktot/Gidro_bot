from django.db import models
from django.db.models import ForeignKey


class River(models.Model):
    name_river = models.CharField(max_length=100)
    baseyn = models.TextField()

    def __str__(self):
        return self.name_river



class GidroPost(models.Model):
    name_river = models.ForeignKey(River, on_delete=models.CASCADE)
    post = models.CharField(max_length=100)
    slag_name = models.CharField(max_length=100, default="")
    index_posta = models.IntegerField(unique=True)
    # geografic_koord = models.CharField(max_length=200)
    # height_BS = models.IntegerField(unique=True)
    # istory_max_level = models.IntegerField()
    # reper = models.IntegerField(unique=True)
    # reyka_max_pruvodka = models.IntegerField()
    # pali_pruvodka = models.IntegerField()
    # sposterigach = models.CharField(max_length=500)
    # telefon = models.IntegerField()
    nebezpecni_yavusha = models.IntegerField()
    stuchiyni_yavusha = models.IntegerField()
    lavel_pidtoplenya = models.IntegerField()
    zonu_pidtoplenya = models.TextField()

    def __str__(self):
        return self.post

    @property
    def nebezpeca(self):
        rep = self.last_report
        if rep:
            if rep.water_level >= self.nebezpecni_yavusha:
                return True
        return False

    @property
    def stuxiya(self):
        rep = self.last_report
        if rep:
            if rep.water_level >= self.stuchiyni_yavusha:
                return True
        return False

    @property
    def message_pidtoplenya(self):
        rep = self.last_report
        if rep:
            if rep.water_level >= self.lavel_pidtoplenya:
                return self.zonu_pidtoplenya
        return False

    @property
    def last_report(self):
        return PostReport.objects.filter(post=self).order_by('-report_time').first()

class PostReport(models.Model):
    post = models.ForeignKey(GidroPost,on_delete=models.CASCADE)
    report_time = models.DateTimeField()
    class ReportType(models.IntegerChoices):
        MANUAL = 1
        MAWS = 2
        AIVS = 3
    report_type = models.IntegerField(choices=ReportType.choices, default=ReportType.MANUAL)
    # battery = models.DecimalField(max_digits=7, decimal_places=3)
    # qml_Voltage = models.DecimalField(max_digits=7, decimal_places=3)
    # qml_temp = models.DecimalField(max_digits=7, decimal_places=3)
    # temperature = models.DecimalField(max_digits=7, decimal_places=3)
    # air_pressure = models.DecimalField(max_digits=7, decimal_places=3)
    # soil_temperature = models.DecimalField(max_digits=7, decimal_places=3)
    water_level = models.DecimalField(max_digits=7, decimal_places=3)
    # pruvodka = models.DecimalField(max_digits=7, decimal_places=3)
    # water_level_BS = models.DecimalField(max_digits=7, decimal_places=3)
    # water_level_ymov = models.DecimalField(max_digits=7, decimal_places=3)
    # precipitation = models.DecimalField(max_digits=7, decimal_places=3)
    # precipitation_1h = models.DecimalField(max_digits=7, decimal_places=3)
    # precipitation_doba = models.DecimalField(max_digits=7, decimal_places=3)
    # precipitation_den = models.DecimalField(max_digits=7, decimal_places=3)
    class Meta:
        unique_together = [('post', 'report_time', 'report_type')]
# class StuchiyniYavusha(models.Model):
#     post = models.ForeignKey(GidroPost, on_delete=models.CASCADE)



class Pruladu(models.Model):
    name_prulad = models.CharField(max_length=100)
    nomer = models.CharField(max_length=50)
    avtomatic_post = models.CharField(max_length=100)
    stan = models.ForeignKey(GidroPost,on_delete=models.CASCADE)
    peredano = models.DateTimeField()
    povireno = models.DateTimeField()
    povirka_grafik = models.DateTimeField()
    termin_povirku = models.IntegerField(unique=True)

    def __str__(self):
        return self.name_prulad


class TelegramUser(models.Model):
    chat_id = models.IntegerField(unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    time_create = models.DateTimeField(auto_now_add=True)
    last_message = models.DateTimeField()


    def __str__(self):
        return f'{self.chat_id} {self.last_name} {self.first_name}'

