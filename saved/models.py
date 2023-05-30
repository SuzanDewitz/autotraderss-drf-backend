from django.db import models
from django.contrib.auth.models import User
from autotraders.models import Autotrader


class Save(models.Model):
    """
    Model to save a autotrader ad. 'owner' is a User instance
    and 'autotrader' is a Autotrader instance. 'unique_together' prevent
    a user from saving the same autotrader ad more than once.
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    autotrader = models.ForeignKey(
        Autotrader, on_delete=models.CASCADE, related_name='saved')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        unique_together = ['owner', 'autotrader']

    def __str__(self):
        return f'{self.owner} {self.autotrader}'
