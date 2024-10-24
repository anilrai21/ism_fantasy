from django.db import models


class ElementTypeName(models.TextChoices):
    GOALKEEPER = "GKP", "Goalkeeper"
    DEFENDER = "DEF", "Sub Defender"
    MIDFIELDER = "MID", "Midfielder"
    FORWARD = "FWD", "Forward"


class Team(models.Model):
    code = models.IntegerField()
    name = models.CharField(max_length=255)
    short_name = models.CharField(max_length=10)

    def __str__(self) -> str:
        return self.name


class ElementType(models.Model):
    singular_name = models.CharField(max_length=255)
    singular_name_short = models.CharField(
        max_length=3, choices=ElementTypeName.choices
    )

    def __str__(self) -> str:
        return self.singular_name


class Element(models.Model):
    chance_of_playing_next_round = models.IntegerField(null=True)
    chance_of_playing_this_round = models.IntegerField(null=True)
    element_type = models.ForeignKey(ElementType, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=255)
    second_name = models.CharField(max_length=255)
    web_name = models.CharField(max_length=255)
    total_points = models.IntegerField()
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    goals_scored = models.IntegerField()
    assists = models.IntegerField()
    goals_conceded = models.IntegerField()
    penalties_saved = models.IntegerField()
    penalties_missed = models.IntegerField()
    saves = models.IntegerField()

    def __str__(self) -> str:
        return f"{self.first_name} {self.second_name}"
