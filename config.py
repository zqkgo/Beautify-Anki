# -*- coding: utf-8 -*-
"""
Beautify Anki
an Addon for Anki
Github (https://github.com/my-Anki/Beautify-Anki)
Copyright (c) 2020 Shorouk Abdelaziz (https://shorouk.dev)
"""
#################################################################################
# Beautify Anki n is released under GNU AGPL, version 3 or later                #
# This Addon uses the following CSS and Javascript libraries                    #
#                                                                               #
# Acknowledgments                                                               #
# This Addon uses the following CSS and Javascript libraries                    #
#   - Materialize                                                               #
#   - Animate.css                                                               #
#   - plotly                                                                    #
# The Statistics part in the Deck Browser is based on Carlos Duarte             #
#  addon "More Decks Stats and Time Left" which is based on                     #
#  Dmitry Mikheev code, in add-on "More decks overview stats"                   #
#  and calumks code, in add-on "Deck Stats"                                     #
#                                                                               #
# The Statistics part in The Deck Overview pages is based on                    #
#  Kazuwuqt addon "More Overview Stats 2.1 " which is based on                  #
#  the More Overview Stats 2 add-on by Martin Zuther which is in turn based on  #
#  "More Overview Stats" by Calumks                                             #
#                                                                               #
#################################################################################

from aqt import mw
import os , sys


CONFIG = mw.addonManager.getConfig(__name__)
STATS = CONFIG["DECK-BROWSER"]["STATS"]
MAIN = CONFIG["MAIN"]
DECKSTATS = CONFIG["DECK-OVERVIEW"]["DECK-STATS"]