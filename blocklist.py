"""
blocklist.py

This file just contains the blocklist of the JWT tokens.
It will be imported by app an the logout resource so that tokens can be added to the blocklist when the user logs out.
"""

#TODO move this to db or redis queue with ttl
BLOCKLIST = set()