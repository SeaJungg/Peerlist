from django.db import models

class PeerIDs(models.Model):
    peername = models.CharField(max_length = 200)
    peercode = models.CharField(max_length = 200)
    attend = models.BooleanField(default=False)
    def __str__(self):
        return self.peername

class Meta:
   ordering = ['-id']