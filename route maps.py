# import simplejson, urllib.request

# orig_lat = 39569521 / (10)**6
# orig_lng = 2650434 / (10)**6

# dest_lat = 39569521 / (10)**6
# dest_lng = 2650534 / (10)**6

# orig_coord = orig_lat, orig_lng
# dest_coord = dest_lat, dest_lng
# url = "http://maps.googleapis.com/maps/api/distancematrix/json?origins={0}&destinations={1}&mode=driving&language=en-EN&sensor=false".format(str(orig_coord),str(dest_coord))
# print (url)
# result= simplejson.load(urllib.request.urlopen(url))
# driving_time = result['rows'][0]['elements'][0]['duration']['value']


import simplejson, urllib.request
orig_coord = '39.569521,2650434'
dest_coord = '39.569521,2650534'
url = "http://maps.googleapis.com/maps/api/distancematrix/json?origins={0}&destinations={1}&mode=walking&language=en-EN&sensor=false".format(str(orig_coord),str(dest_coord))
print (url)
result= simplejson.load(urllib.request.urlopen(url))
walking_time = result['rows'][0]['elements'][0]['duration']['value']/60
print (walking_time)