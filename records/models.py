#models.py
from django.db import models

class Species(models.Model):
    name = models.CharField(max_length=200, verbose_name="種")
    genus = models.CharField(max_length=100, blank=True, null=True, verbose_name="属")
    family = models.CharField(max_length=100, blank=True, null=True, verbose_name="科")
    scientific_name = models.CharField(max_length=200, blank=True, null=True, verbose_name="学名")
    note = models.TextField(blank=True, null=True, verbose_name="備考")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "種"
        verbose_name_plural = "種"

class Location(models.Model):
    name = models.CharField(max_length=200, verbose_name="場所名")
    latitude = models.FloatField(blank=True, null=True, verbose_name="緯度")
    longitude = models.FloatField(blank=True, null=True, verbose_name="経度")
    note = models.TextField(blank=True, null=True, verbose_name="備考")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "場所"
        verbose_name_plural = "場所"

class Survey(models.Model):  # 調査日をまとめるモデル
    date = models.DateField(verbose_name="調査日")
    note = models.TextField(blank=True, null=True, verbose_name="調査メモ")

    def __str__(self):
        return str(self.date)

    class Meta:
        verbose_name = "調査"
        verbose_name_plural = "調査"

class Record(models.Model):
    species = models.ForeignKey(Species, on_delete=models.CASCADE, verbose_name="種")
    location = models.ForeignKey(Location, on_delete=models.CASCADE, verbose_name="採取場所")
    survey = models.ForeignKey(Survey, on_delete=models.CASCADE, verbose_name="調査日")
    count = models.IntegerField(default=1, verbose_name="個体数")
    length = models.FloatField(blank=True, null=True, verbose_name="体長(mm)")
    weight = models.FloatField(blank=True, null=True, verbose_name="湿重量(g)")
    water_temperature = models.FloatField(blank=True, null=True, verbose_name="水温(℃)")
    flow_rate = models.FloatField(blank=True, null=True, verbose_name="流速(m/s)")
    water_depth = models.FloatField(blank=True, null=True, verbose_name="水深(m)")
    note = models.TextField(blank=True, null=True, verbose_name="備考")

    def __str__(self):
        return f"{self.species.name} - {self.location.name} - {self.date}"

    class Meta:
        verbose_name = "記録"
        verbose_name_plural = "記録"