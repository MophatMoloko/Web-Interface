from django.db import models

# Create your models here.
class Tutor_Marking(models.Model): #name of the table  
    

    Student= models.CharField(max_length = 5, blank= True, null = True)

   # tutors= (
    #    ('BNDJAM007','BNDJAM007'), ('TRMDON002','TRMDON002'), ('JHNBOR002','JHNBOR002'),
    #    ('MNDNEL001','MNDNEL001'),('ZMXJAC003','ZMXJAC003'), ('RMPCYR004','RMPCYR004'), ('NHXTRE001','NHXTRE001'),
    #    ('RBNNIC005','RBNNIC005'), ('LTTMAR002','LTTMAR002'),
    #    ('PWRAUS003','PWRAUS003'), ('MBKTHA002','MBKTHA002'), ('CRRJIM004','CRRJIM004'), ('JHNBOR002','JHNBOR002'),
    #)
    
    A1_Marker = models.CharField(max_length=15, blank= True, null = True)
    A2_Marker = models.CharField(max_length=15, blank= True, null = True)
    A3_Marker = models.CharField(max_length=15, blank= True, null = True)
    A4_Marker = models.CharField(max_length=15, blank= True, null = True)
    A5_Marker = models.CharField(max_length=15, blank= True, null = True)
    A6_Marker = models.CharField(max_length=15, blank= True, null = True)
    
    def __str__(self) -> str:
        return str(self.id) 
    