url = ''.join(x.strip() for x in open('graph_url').readlines())

page = '<html><head><title>Gate Success Rate</title></head><body><img src="' \
       '%s"></body></html>' % url

with open('gate_status.html', 'wb') as f:
    f.write(page)
