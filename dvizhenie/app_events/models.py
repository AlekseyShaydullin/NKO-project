from django.core.exceptions import ValidationError
from django.db import models
from django.utils.translation import gettext_lazy as _


class Address(models.Model):
    """
    Адрес (чего угодно).
    """
    address = models.CharField(_("address"), max_length=256)

    def __str__(self):
        return self.address

    class Meta:
        verbose_name = _("address")
        verbose_name_plural = _("addresses")
        ordering = ("address",)


class FundEvent(models.Model):
    """
    Мероприятие фонда. Если мероприятие прошло поставьте флажок в поле 'Закончено?'.
    """
    name = models.CharField(_("name"), max_length=128, db_index=True)
    description = models.TextField(_("description"), max_length=2048, blank=True)
    start_timestamp = models.DateTimeField(_("start timestamp"))
    end_timestamp = models.DateTimeField(_("end timestamp"))

    is_finished = models.BooleanField(
        _("is finished"), db_index=True, help_text=_("Is this event has finished?"), default=False
    )

    addresses = models.ManyToManyField(Address, verbose_name=_("addresses"), related_name="events", blank=True)

    is_online = models.BooleanField(
        _("online mode?"), db_index=True, help_text=_("Is this event will conduct in online mode?")
    )

    files = models.ManyToManyField('root.File', verbose_name=_("files"), related_name="events", blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("event")
        verbose_name_plural = _("events")
        ordering = ("start_timestamp",)

    def clean(self):
        if self.start_timestamp >= self.end_timestamp:
            raise ValidationError(_("Start of the project cannot be later than its end."))
