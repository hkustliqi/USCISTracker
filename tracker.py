#!/usr/bin/env python

import re 
from mechanize import Browser
br = Browser()

# Ignore robots.txt
br.set_handle_robots( False )
# Google demands a user-agent that isn't a robot
br.addheaders = [('User-agent', 'Firefox')]

# Retrieve the Google home page, saving the response
br.open( "http://egov.uscis.gov/casestatus/landing.do" )

# Select the search box and search for 'foo'
br.select_form( 'caseStatusForm' )
print br.form
br.form[ 'case' ] = 'foo'

# Get the search results
br.submit()

# Find the link to foofighters.com; why did we run a search?
resp = None
for link in br.links():
    siteMatch = re.compile( 'www.foofighters.com' ).search( link.url )
    if siteMatch:
        resp = br.follow_link( link )
        break

# Print the site
content = resp.get_data()
print content
