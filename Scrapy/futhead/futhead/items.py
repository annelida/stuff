# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/topics/items.html

from scrapy.item import Item, Field


class FutheadItem(Item):
    # define the fields for your item here like:
    Name = Field()
    Club = Field()
    League = Field()
    Nation = Field()
    SkillMoves = Field()
    WeakFoot = Field()
    StrongFoot = Field()
    Age = Field()
    Height = Field()
    Workrates = Field()
    Pace = Field()
    Shooting = Field()
    Passing = Field()
    Dribbling = Field()
    Defending = Field()
    Physical = Field()
    AttackerRating = Field()
    CreatorRating = Field()
    DefenderRating = Field()
    BeastRating = Field()
    HeadingRating = Field()
    TotalStats = Field()
    TotalLigs = Field()
    Rating = Field()
    Position = Field()
    pass
