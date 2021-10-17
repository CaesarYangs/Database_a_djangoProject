from django.db import models


class Flight(models.Model):
    flightid = models.CharField(db_column='FlightID', primary_key=True, max_length=30)  # Field name made lowercase.
    planeid = models.IntegerField(db_column='PlaneID', blank=True, null=True)  # Field name made lowercase.
    flightname = models.CharField(db_column='FlightName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    utime = models.CharField(db_column='UTime', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dtime = models.CharField(db_column='DTime', max_length=255, blank=True, null=True)  # Field name made lowercase.
    origin = models.CharField(db_column='Origin', max_length=255, blank=True, null=True)  # Field name made lowercase.
    destination = models.CharField(db_column='Destination', max_length=255, blank=True, null=True)  # Field name made lowercase.
    isdelay = models.CharField(db_column='IsDelay', max_length=255, blank=True, null=True)  # Field name made lowercase.
    seatleft = models.IntegerField(db_column='SeatLeft', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Flight'

class Ticket(models.Model):
    ticketid = models.AutoField(db_column='TicketID', primary_key=True)  # Field name made lowercase.
    userid = models.CharField(db_column='UserID', max_length=255, blank=True, null=True)  # Field name made lowercase.
    flightid = models.CharField(db_column='FlightID', max_length=11, blank=True, null=True)  # Field name made lowercase.
    airportid = models.CharField(db_column='AirportID', max_length=11, blank=True, null=True)   # Field name made lowercase.
    money = models.CharField(db_column='Money', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Ticket'