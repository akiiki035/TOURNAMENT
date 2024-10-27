from django.db import models


class season (models.Model):
    
  
    season_name = models.CharField(max_length=20)
    start_date = models.CharField(max_length=20)
    end_date = models.CharField(max_length=20)
    stutus = models.CharField(max_length=30)

    def __str__(self):
        return self.season_name

class club(models.Model):
    club_name = models.CharField(max_length=30)
    club_stadium = models.CharField(max_length=30)
    stadium_capacity = models.BigIntegerField
    logo = models.CharField(max_length=30)
    club_sponsor = models.CharField(max_length=40)
    club_originality = models.CharField(max_length=50)

    def __str__(self):
        return self.club_name
    


class player  (models.Model):
    GENDER_OPTIONS = [
       ("M","MALE"),
       ("F","FEMALE"),
    ]
    player_name = models.CharField(max_length=30)
    birth_date = models.DateField(auto_now=True)
    position = models.CharField(max_length=30)
    gender = models.CharField( max_length=4,choices=GENDER_OPTIONS)
    contact  = models.CharField(max_length=40)
    club = models.ForeignKey(club,on_delete= models.CASCADE)


    def __str__(self):
        return self.player_name

class fixture (models.Model):
    fixture_time = models.TimeField(auto_now=True)
    fixture_date = models.DateField(auto_now=True)
    fixtture_status = models.CharField(max_length=10)    
    club = models.ForeignKey(club,on_delete= models.CASCADE) 
    season = models.ForeignKey(season,on_delete=models.CASCADE)
    referee = models.CharField(max_length=30)

    def __str__(self):
        return self.fixtture_status
                

class result (models.Model):  
    fixture = models.ForeignKey(fixture, on_delete= models.CASCADE)
    club = models.ForeignKey(club,on_delete= models.CASCADE)
    scores = models.IntegerField()
    yellow_card = models.IntegerField()
    red_cards = models.IntegerField()
    possession = models.IntegerField()


    def __str__(self):
        return self.possession
           


    






        
