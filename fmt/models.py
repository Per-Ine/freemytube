from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User



# Create your models here.

class Main_Frame(models.Model):
    mdf = models.CharField(_('Main Frame'), max_length=50, blank=True)
    lon = models.FloatField(_('Longitude'), blank=True, null=True)
    lat = models.FloatField(_('Latitude'), blank=True, null=True)

    class Meta:
        verbose_name = _('Main frame')

    def __unicode__(self):
        return unicode(self.mdf)


class Location(models.Model):
    user = models.ForeignKey(User)
    main_frame = models.ForeignKey(Main_Frame)  
    ip_address = models.IPAddressField(_('IP Address'), unique=True)
    hostname = models.CharField('Resolved hostname', max_length=255, blank=True)
    zipcode = models.CharField(_('ZIP Code'), max_length=64, blank=True)

    class Meta:
        verbose_name = _('Location')
        verbose_name_plural = _('Locations')

    def __unicode__(self):
        return unicode(self.ip_address)


class Video(models.Model):
    location = models.ForeignKey(Location)
    video_title = models.CharField(max_length=255, verbose_name=_("YouTube Video Title"), null=True, blank=True)
    video_url = models.URLField(verbose_name=_("YouTube Video URL"), null=True, blank=True)
    #startDate = models.DateTimeField("Start date")
    #average = models.FloatField(null=True)

    class Meta:
        verbose_name = _('Video')
        verbose_name_plural = _('Videos')

    def __unicode__(self):
        return unicode(self.video_title)


class Load(models.Model):
    video = models.ForeignKey(Video)
    minimum = models.IntegerField(verbose_name=_("Minimum"))
    maximum = models.IntegerField(verbose_name=_("Maximum"))
    average = models.IntegerField(verbose_name=_("Average"))
    start_time = models.DateTimeField(verbose_name=_("Start Date"))
    end_time = models.DateTimeField(verbose_name=_("End Date"))
    file_size = models.IntegerField(verbose_name=_("File Size"), null=True, blank=True)
    #video_title = models.CharField(max_length=255, verbose_name=_("YouTube Video Title"), null=True, blank=True)
    #video_url = models.URLField(verssbose_name=_("YouTube Video URL"), null=True, blank=True)

    class Meta:
        verbose_name = _("Measurement")
        verbose_name_plural = _("Measurements")

    def __unicode__(self):
        return unicode(self.id)