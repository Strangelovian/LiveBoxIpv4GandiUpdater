# LiveBoxIpv4GandiUpdater
Python 3 script to update a Gandi zone with the current Livebox ipv4 wan address

livebox file:
use http POST request to query the livebox WAN status, including the current WAN ipv4 address
it doesn't need the admin livebox password

gandi file:
use Gandi xmlrpc API to check if the configured DNS zone is up to date

settings:
loads Gandi api key and other things from a .rc file

