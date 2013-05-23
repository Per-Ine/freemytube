from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User

from rest_framework.authtoken.models import Token

from django.dispatch import receiver
from django.db.models.signals import post_save


class MainFrame(models.Model):
    name = models.CharField(_("Main Frame"), unique=True, max_length=20,
                            blank=False)
    city = models.CharField(_("City Name"), max_length=100, blank=True)

    class Meta:
        verbose_name = _("Main frame")

    def __unicode__(self):
        return unicode(self.name)


class Video(models.Model):
    title = models.CharField(_("Video Title"), max_length=255, blank=True)
    url = models.URLField(_("Video URL"))

    class Meta:
        verbose_name = _('Video')
        verbose_name_plural = _('Videos')

    def __unicode__(self):
        return unicode(self.title)


class Measurement(models.Model):
    minimum = models.IntegerField(_("Minimum"))
    maximum = models.IntegerField(_("Maximum"))
    average = models.IntegerField(_("Average"))
    start_time = models.DateTimeField(_("Start Time"))
    end_time = models.DateTimeField(_("End Time"))
    file_size = models.IntegerField(_("File Size"), null=True, blank=True)
    ip_address = models.IPAddressField(_("IP Address"), max_length=50)
    lon = models.FloatField(_("Longitude"), blank=True, null=True)
    lat = models.FloatField(_("Latitude"), blank=True, null=True)

    video = models.ForeignKey(Video)
    user = models.ForeignKey(User)
    main_frame = models.ForeignKey(MainFrame, null=True, blank=True)

    class Meta:
        verbose_name = _("Measurement")
        verbose_name_plural = _("Measurements")

    def __unicode__(self):
        return u"%s - %s" % (self.user, self.end_time)


@receiver(post_save, sender=User)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
