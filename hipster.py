#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import time

from src import InstaBot
from src.check_status import check_status
from src.feed_scanner import feed_scanner
from src.follow_protocol import follow_protocol
from src.unfollow_protocol import unfollow_protocol

bot = InstaBot(
    # login="trend.sttler",  # Enter username (lowercase). Do not enter email!
    # password="karansoniji#1",
    login="alignthem.co",
    password="Karansoniji1",
    like_per_day=2000,
    comments_per_day=0,
    tag_list=[
" userinterface ","uxuidesign ","webdesign ","uiux ","uxinspiration ","interactiondesign ","designtips #designprocess #dailyinspiration ","uxtrends ","uiuxdesign ","freelancer ","uxchoice ","uidesign ","designstrategy ","designbusiness ","designadvice ","bizofdesign ","userexperiencedesign ","ux_meta ","fourmeta"],
    tag_blacklist=["rain", "thunderstorm", "followers",
                   "fc", "official", "desi", "japnies", "bhabhi"],
    user_blacklist={},
    max_like_for_one_tag=37,
    follow_per_day=300,
    follow_time=1 * 1 * 5,
    unfollow_per_day=75,
    unlike_per_day=20,
    # If True, the bot will also unfollow people who dont follow you using the recent feed. Default: True
    unfollow_recent_feed=True,
    time_till_unlike=3 * 24 * 60 * 60,  # 3 days
    unfollow_break_min=2,
    unfollow_break_max=5,
    user_max_follow=0,
    # session_file=False, # Set to False to disable persistent session, or specify custom session_file (ie ='myusername.session')
    user_min_follow=0,
    log_mod=0,
    proxy="",
    # List of list of words, each of which will be used to generate comment
    # For example: "This shot feels wow!"
    comment_list=[
        ["this", "the", "your"],
        ["thing", "move", "idea", "shot"],
        ["is", "looks", "is 👉", "is really"],
        [
            "great",
            "super",
            "good",
            "very good",
            "good",
            "wow",
            "WOW",
            "cool",
            "GREAT",
            "magnificent",
            "magical",
            "very cool",
            "so professional",
            # "lovely",
            # "so lovely",
            # "very lovely",
            # "glorious",
            # "so glorious",
            # "very glorious",
            "adorable",
            "excellent",
            "amazing",

        ],
        [".", "🙌", "... 👏", "!", "! 😍", "😎"],
    ],
    # Use unwanted_username_list to block usernames containing a string
    # Will do partial matches; i.e. 'mozart' will block 'legend_mozart'
    # 'free_followers' will be blocked because it contains 'free'
    unwanted_username_list=[
        "second",
        "stuff",
        "art",
        "project",
        "love",
        "life",
        "food",
        "blog",
        "free",
        "keren",
        "photo",
        "graphy",
        "indo",
        "travel",
        "art",
        "shop",
        "store",
        "sex",
        "toko",
        "jual",
        "online",
        "murah",
        "jam",
        "kaos",
        "case",
        "baju",
        "fashion",
        "corp",
        "tas",
        "butik",
        "grosir",
        "karpet",
        "sosis",
        "salon",
        "skin",
        "care",
        "cloth",
        "tech",
        "rental",
        "kamera",
        "beauty",
        "express",
        "kredit",
        "collection",
        "impor",
        "preloved",
        "fan",
        "group",
        "follow",
        "follower",
        "gain",
        ".id",
        "_id",
        "bags",
        "fc",
        "bhabhi",
    ],
    unfollow_whitelist=["sonalii.sharmaa", "saniya_khaton_13", "simran_thakur743", "___sachi.__", "anushka4nov", "fulwanideepa",
                        "simran6734", "worldwide_photography_hub", "mehakrajput132",
                        "mansi__cupcake", "deeksha_rajput_07", "ritika_2945",
                        "shizhukasingh0", "simar.5796", "shivanimohitsharma",
                        "pari_ji_bhardwaj", "cutegirlsonali", "garvita786",
                        "pinkssss08", "skywalker_flying_1", "sarjeeta",
                        "shruti_verma_", "panwarversha8", "saru_3565",
                        ],
    # Enable the following to schedule the bot. Uses 24H
    # end_at_h = 23, # Hour you want the bot to stop
    # end_at_m = 30, # Minute you want the bot stop, in this example 23:30
    # start_at_h = 9, # Hour you want the bot to start
    # start_at_m = 10, # Minute you want the bot to start, in this example 9:10 (am).
)

bot.mainloop()
