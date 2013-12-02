#!/usr/bin/python
# Copyright 2013 Sumana Harihareswara
# GPL'd -- see COPYING
# How long till cultural artifacts get ruined/covered/mashed up?
# Songs, movies, hashtags, short stories
# For use in @RuinRobot

import random
import time
from tweet import api

class Artifact():
    # items with year; people; ruinations; delay
    pass

class Songs(Artifact):
    items = [(1994, "A Whole New World"), 
             (1995, "Streets of Philadelphia") ,
             (1996, "Kiss from a Rose"),
             (1997, "Change the World"),
             (1998, "Sunny Came Home"),
             (1999, "My Heart Will Go On"),
             (2000, "Smooth"),
             (2001, "Beautiful Day"),
             (2004, "Lose Yourself"),
             (2007, "You're Beautiful"),
             (2008, "Hey There Delilah"),
             (2010, "Single Ladies (Put a Ring on It)"),
             (2011, "F**k You"),
             (2012, "Rolling in the Deep"),
             (2013, "We Are Young")]

    parodists = ["the Muppets", "Glee: The Next Generation", "teenyboppers", "a teen heartthrob", "a tv ad", "morning drive DJs", "Muzak"]

    ruins = ["cover", "mashup", "sample", "co-opt", "ringtone-ify"]

    delay = 20

class Books(Artifact):
    items = [(1983, "The Color Purple"),
             (1985, "The Cider House Rules"),
             (1988, "Beloved"),
             (1989, "A Prayer for Owen Meany"),
             (1992, "A Thousand Acres"),
             (1994, "The Shipping News"),
             (1998, "Tipping the Velvet"),
             (1998, "The Poisonwood Bible"),
             (2000, "Interpreter of Maladies"),
             (2001, "The Amazing Adventures of Kavalier & Clay"),
             (2002, "The Corrections"),
             (2003, "Moneyball"),
             (2003, "The Da Vinci Code"),
             (2003, "The Devil Wears Prada"),
             (2004, "He's Just Not That Into You"),
             (2005, "Maximum City"),
             (2005, "Freakonomics"),
             (2005, "The Girl with the Dragon Tattoo"),
             (2007, "The Road"),
             (2008, "The Brief Wondrous Life of Oscar Wao"),
             (2010, "Eat Pray Love"),
             (2012, "The Pale King")]

    parodists = ["The Onion", "MAD Magazine", "The New Yorker"]

    ruins = ["adapt for film", "publish fanfic of", "comic book-ify"]

    delay = 40

class Shows(Artifact):
    items = [(1985, "Cheers"),
             (1986, "The Cosby Show"),
             (1987, "Night Court"),
             (1988, "Murphy Brown"),
             (1989, "The Wonder Years"),
             (1992, "Northern Exposure"),
             (1993, "Home Improvement"),
             (1994, "Frasier"),
             (1995, "NYPD Blue"),
             (1996, "3rd Rock From the Sun"),
             (1997, "Seinfeld"),
             (1998, "The Practice"),
             (1999, "Ally McBeal"),
             (2001, "Will & Grace"),
             (2002, "Everybody Loves Raymond"),
             (2003, "Six Feet Under"),
             (2004, "Arrested Development"),
             (2005, "Lost"),
             (2006, "24"),
             (2007, "The Sopranos"),
             (2009, "Big Love"),
             (2010, "The Big Bang Theory"),
             (2011, "American Horror Story"),
             (2012, "Boardwalk Empire")
             ]

    parodists = ["the Muppets", "Saturday Night Live", "MAD Magazine", "Saturday morning cartoons"]

    ruins = ["reboot", "film", "remake", "comic book-ify"]

    delay = 30


def horrorPredictionGenerator(categories):
    while True:
        genre = random.choice(categories)
        thing = random.choice(genre.items)
        person = random.choice(genre.parodists)
        delay = genre.delay
        ruintype = random.choice(genre.ruins)
        yield "In %s, %s will %s %s." % (delay+thing[0], person, ruintype, thing[1])

genres = [Songs, Books, Shows]

hpg = horrorPredictionGenerator(genres)

while True:
    api.PostUpdate(hpg.next())
    time.sleep(30*60)  # sleep 30 minutes
