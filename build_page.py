error_url = ''.join(x.strip() for x in open('error_rate_url').readlines())
#pressure_url = ''.join(x.strip() for x in open('gate_pressure_url').readlines())

page = '<html><head><title>Gate Success Rate</title></head><body><img src="' \
       '%s"></body></html>' % error_url
#       '%s"><br><img src="%s"></body></html>' % (error_url, pressure_url)

with open('gate_status.html', 'wb') as f:
    f.write(page)
