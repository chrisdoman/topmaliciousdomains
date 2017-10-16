

popular_domains = {}
popular_alexa_domains = {}


with open("top-1m.csv") as file:
     lines = file.readlines()

     for line in lines:
        l = line.strip().split(',')[1]
        popular_domains[l] = True

with open("alexa-top-1m.csv") as file:
     lines = file.readlines()

     for line in lines:
        l = line.strip().split(',')[1]
        popular_alexa_domains[l] = True


print "<h1>About</h1>"
print "This is a quick experiment looking at the cross section of popular domains (via https://umbrella.cisco.com/blog/2016/12/14/cisco-umbrella-1-million/)"
print " and malicious domains (via otx.alienvault.com)"


print "<h1>Potentially Malicious Popular Domains</h1>"
print "This is a list of domains that have been marked as bad in OTX, are listed as popular in Umbrella, but not popular in Alexa<br>"

with open("otx-c2-iocs.txt") as file:

     seen = []    
     lines = file.readlines()

     for line in lines:
        domain = line.strip().split(';')[0]
        if domain not in seen:
            seen.append(domain)

            if domain in popular_domains:
                if domain not in popular_alexa_domains and domain.replace("www.","") not in popular_alexa_domains:
                    print "<li><a href='http://otx.alienvault.com/indicator/hostname/" + domain + "'>" + domain + "</a>"

print "<h1>Possible false positives in OTX</h1>"

with open("otx-c2-iocs.txt") as file:
     lines = file.readlines()

     for line in lines:
        domain = line.strip().split(';')[0]

        if domain in popular_domains:
            if domain in popular_alexa_domains or domain.replace("www.","") in popular_alexa_domains:
                print "<li><a href='http://otx.alienvault.com/indicator/hostname/" + domain + "'>" + domain + "</a>"

print "<h1>Domains that are popular with machines but not humans</h1>"
print "This is a list of domains that are in Umbrella, but not Alexa<br>"
for key,value in popular_domains.iteritems():
     if key not in popular_alexa_domains and key.replace('www.','') not in popular_alexa_domains:
        print "<li><a href='http://otx.alienvault.com/indicator/hostname/" + key + "'>" + key + "</a>"