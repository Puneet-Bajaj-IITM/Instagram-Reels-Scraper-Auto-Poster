import os

#--------------------------------------------------------------------------------------------------#
# Global Configurations                                                                            #
#--------------------------------------------------------------------------------------------------#

# Config Variables
CURRENT_DIR = os.getcwd() + os.sep

# SQLite DB path
DB_PATH = CURRENT_DIR + '..'+os.sep+'database' + os.sep + 'sqlite.db'

# Download Path
DOWNLOAD_DIR = CURRENT_DIR + '..'+os.sep+'downloads' + os.sep  # Path of folder where files will be stored

#IS REMOVE FILES
IS_REMOVE_FILES = 1

# Remove Posted Files Interval
REMOVE_FILE_AFTER_MINS = 120 #every two hours

#--------------------------------------------------------------------------------------------------#
# Instagram Configurations                                                                         #
#--------------------------------------------------------------------------------------------------#

# IS RUN AUTO POSTER
IS_ENABLED_AUTO_POSTER = 1

# Instagram Username & Password
USERNAME = "your_username"
PASSWORD = "your_password"

# Account List for scraping
ACCOUNTS = [
    "totalgaming_official",
    "carryminati",
    "techno_gamerz",
    "payalgamingg",
    "dynamo__gaming"
]

# like_and_view_counts_disabled
LIKE_AND_VIEW_COUNTS_DISABLED = 0

# disable_comments
DISABLE_COMMENTS = 0

# HASHTAGS to add while Posting
HASHTAGS = "#reels #shorts #likes #follow #Reels-AutoPilot"
