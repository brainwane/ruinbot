#!/usr/bin/python
# How long till cultural artifacts get ruined/covered/mashed up?
# Songs, movies, hashtags, short stories

import random

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

    parodists = ["the Muppets", "Glee: The Next Generation", "teenyboppers", "a teen heartthrob", "a tv ad", "morning drive DJs", "Muzak", "a stand-up comedian"]

    ruins = ["cover", "mashup", "sample", "co-opt", "ringtone-ify"]

    delay = 20

class Books(Artifact):
    items = [(2000, "Interpreter of Maladies"),
             (2005, "Maximum City: Bombay Lost and Found"),
             (2007, "The Road"),
             (2008, "Anathem"),
             (2012, "The Pale King")]

    parodists = ["The Onion", "MAD Magazine", "The New Yorker"]

    ruins = ["adapt for film", "publish fanfic of", "comic book-ify"]

    delay = 40

class Shows(Artifact):
    items = [(1992, "Northern Exposure"),
             (1994, "Frasier"),
             (1995, "NYPD Blue"),
             (1996, "3rd Rock From the Sun"),
             (1998, "The Practice"),
             (1999, "Ally McBeal"),
             (2001, "Will & Grace"),
             (2002, "Everybody Loves Raymond"),
             (2004, "Arrested Development"),
             (2005, "Lost"),
             (2006, "24"),
             (2007, "The Sopranos"),
             (2009, "Big Love"),
             (2010, "The Big Bang Theory")
             ]

    parodists = ["the Muppets", "Saturday Night Live", "MAD Magazine", "Saturday morning cartoons"]

    ruins = ["reboot", "film", "comic book-ify", "merchandise (with breakfast cereal and toys)"]

    delay = 30


def horrorPredictionGenerator(categories):
    while True:
        genre = random.choice(categories)
        thing = random.choice(genre.items)
        person = random.choice(genre.parodists)
        delay = genre.delay
        ruintype = random.choice(genre.ruins)
        yield "In the year %s, %s will %s %s." % (delay+thing[0], person, ruintype, thing[1])

genres = [Songs, Books, Shows]
