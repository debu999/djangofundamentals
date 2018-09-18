from django.db import models


# Create your models here.
class Popularity(models.Model):
    previousrank = models.IntegerField(verbose_name="PreviousWeekRank", name="previousrank",
                                       blank=True, null=True, db_index=True)
    rank = models.IntegerField(verbose_name="Rank", name="rank",
                               blank=False, null=False, default=-999)

    def __str__(self):
        return "rnk: {}, prnk: {}".format(self.rank, self.previousrank)


class Language(models.Model):
    name = models.CharField(name="name", max_length=50)
    paradigm = models.CharField(name="paradigm", max_length=20)
    rank = models.IntegerField(name="rank", null=False)
    popularity = models.ForeignKey(Popularity, on_delete=models.CASCADE, default=-999)

    class Meta:
        db_table = u'Language'
        verbose_name = "Table: Language"
        ordering = ['-rank']

    def __unicode__(self):
        return self.name

    def __repr__(self):
        return "{}.{}".format(self.rank, self.name)

    def __str__(self):
        return "{}.{}".format(self.rank, self.name)


class Programmer(models.Model):
    name = models.CharField(max_length=50)
    languages = models.ManyToManyField(Language)

    def __str__(self):
        return "{} - {}".format(self.name, str(self.languages))
