import urllib

format_dict = {
    'HOWLONGAGO': '6weeks',
    'TIMEBUCKET': '12hours',
    'MOVINGAVGPERIOD': '10days',
    'SUCCESS,FAILURE': '{SUCCESS,FAILURE}',
    'SIMPLETIMEBUCKET': '24hours',
    'SIMPLEHOWLONGAGO': '3weeks',
    'SIMPLEMOVINGAVGPERIOD': '5days',
}


error_url = ''.join(x.strip() for x in open('graph_template').readlines())
error_url = error_url.replace(' ', '%20')
error_url = error_url.format(**format_dict)
simple_graph_url = ''.join(x.strip() for x in open('simple_graph_template').readlines())
simple_graph_url = simple_graph_url.replace(' ', '%20')
simple_graph_url = simple_graph_url.format(**format_dict)
swift_error_url = ''.join(x.strip() for x in open('swift_graph_template').readlines())
swift_error_url = swift_error_url.replace(' ', '%20')
swift_error_url = swift_error_url.format(**format_dict)
recheck_graph_url = ''.join(x.strip() for x in open('recheck_count_template').readlines())
recheck_graph_url = recheck_graph_url.replace(' ', '%20')
recheck_graph_url = recheck_graph_url.format(**format_dict)
neutron_graph_url = ''.join(x.strip() for x in open('neutron_graph_template').readlines())
neutron_graph_url = neutron_graph_url.replace(' ', '%20')
neutron_graph_url = neutron_graph_url.format(**format_dict)
nova_graph_url = ''.join(x.strip() for x in open('nova_graph_template').readlines())
nova_graph_url = nova_graph_url.replace(' ', '%20')
nova_graph_url = nova_graph_url.format(**format_dict)
solum_graph_url = ''.join(x.strip() for x in open('solum_graph_template').readlines())
solum_graph_url = solum_graph_url.replace(' ', '%20')
solum_graph_url = solum_graph_url.format(**format_dict)
cinder_graph_url = ''.join(x.strip() for x in open('cinder_graph_template').readlines())
cinder_graph_url = cinder_graph_url.replace(' ', '%20')
cinder_graph_url = cinder_graph_url.format(**format_dict)
marconi_graph_url = ''.join(x.strip() for x in open('marconi_graph_template').readlines())
marconi_graph_url = marconi_graph_url.replace(' ', '%20')
marconi_graph_url = marconi_graph_url.format(**format_dict)
keystone_graph_url = ''.join(x.strip() for x in open('keystone_graph_template').readlines())
keystone_graph_url = keystone_graph_url.replace(' ', '%20')
keystone_graph_url = keystone_graph_url.format(**format_dict)

msg = '''
<h3>Explanation</h3>
<p>
The purpose of these graphs are to report what's been going on and to give
OpenStack contributors a narrow time window in which to look for errors.
Importantly, these graphs are not explaining why something is or isn't passing.
These graphs only report if something is or is not passing.
</p>
<p>
The "Patch Pass Chance" above (the bold red line) is the chance that
a newly submitted patch has of passing the six tracked gate jobs,
optimistically assuming that the patch is perfect and introduces no bugs. In
other words, if you submit a new patch to the Jenkins gate queue&mdash;whether
a major new feature or a trivial doc spelling error&mdash;the "Patch Pass
Chance" is the starting point for the likelihood of that patch being merged
into master.
</p>
<p>
The "Patch Pass Chance Avg" (the bold orange line) is the ten day moving
average of the patch pass chance.
</p>
<p>
The depth of the gate queue is also tracked. This allows two things: one, a
comparison of the patch pass chance to the depth of the queue (e.g. "Is the
patch pass chance shown as a high value because the queue isn't testing
much?") and two, the ability to calculate the probability that the current gate
queue will clear. To calculate the chance that the gate queue will clear, take
the decimal representation of the patch pass chance and raise it to the depth
of the gate queue. For example, a gate queue 10 deep, when combined with a
patch pass chance of 85% has a 19.69% chance of passing (100 * .85**10).
</p>
<p>
Note that the gate-*-{docs,pep8,python26,python27} jobs run in the zuul check
queue as well as the gate queue, so a failure reported in these may not
indicate a gate-blocking bug.
</p>
<p>
To be clear, the gate depth is the result of a low pass chance, not the cause.
A low pass chance will cause more jobs to be rechecked and therefore keep
patches in the gate longer, thus leading to a larger gate queue.
</p>
<p>
The "Gate Resets" graph is an attempt to track the efficiency of the zuul
pipeline scheduler. An ideal value is 1. Any number above that means that
jobs before it in the gate queue failed and caused zuul to rerun the jobs for
the patch set.
</p>

<h3>Methodology</h3>
<p>
The last six weeks are graphed by summarizing each 12-hour window into the
average (mean) value for that time slice. The gate job status success rate
is the percent of successful runs divided by the sum of the successful and 
unsuccessful runs in that time block. The "Patch Pass Chance" is the
multiplication of the gate job pass percentages. Because each gate job failure
is independent (i.e. a patch will fail if any of the gate jobs fails), this
calculation is an accurate representation of the chance a patch has of landing.
Missing data points in the data (i.e. nothing happening) is optimistically
counted as a 100% pass rate. Therefore the "Patch Pass Chance" calculated is
the absolute best-case scenario, based on the status of the six tracked jobs.
</p>
<p>
The gate resets count is calculated by taking the total number of runs of
pep8 jobs, divides that by 2 (since they run for check and gate) and then
dividing that number by the number of patches that have merged. This is an
experiment, and I don't think it's too accurate right now, but it is a guide.
</p>
<hr/>
<p style="font-size: 80%">Source for generating this page is at
<a href="https://github.com/notmyname/gate_status">
https://github.com/notmyname/gate_status</a>
</p>
'''

common_page = '''
<html><head><title>Gate Success Rate</title></head>
<body style="width: 80%%">
<center>
<img style="margin: 0 auto;" src="%s"><br />
<img style="margin: 0 auto;" src="%s"><br />
</center>
<div style="margin: 0 10%%;">%s</div></body></html>
''' % (error_url, recheck_graph_url, msg)

with open('gate_status.html', 'wb') as f:
    f.write(common_page)

with open('simple_graph_url', 'wb') as f:
    f.write(simple_graph_url)

all_page = '''
<html><head><title>Gate Success Rate</title></head>
<body style="width: 80%%">
<center>
<img style="margin: 0 auto;" src="%s"><br />
<img style="margin: 0 auto;" src="%s"><br />
<img style="margin: 0 auto;" src="%s"><br />
<img style="margin: 0 auto;" src="%s"><br />
<img style="margin: 0 auto;" src="%s"><br />
<img style="margin: 0 auto;" src="%s"><br />
<img style="margin: 0 auto;" src="%s"><br />
<img style="margin: 0 auto;" src="%s"><br />
<img style="margin: 0 auto;" src="%s"><br />
</center>
<div style="margin: 0 10%%;">%s</div></body></html>
''' % (error_url, swift_error_url, neutron_graph_url, nova_graph_url,
       cinder_graph_url, keystone_graph_url, marconi_graph_url,
       solum_graph_url, recheck_graph_url,
       msg)

with open('all_gate_status.html', 'wb') as f:
    f.write(all_page)

swift_page = '''
<html><head><title>Gate Success Rate</title></head>
<body style="width: 80%%">
<center>
<img style="margin: 0 auto;" src="%s"><br />
<img style="margin: 0 auto;" src="%s"><br />
<img style="margin: 0 auto;" src="%s"><br />
</center>
<div style="margin: 0 10%%;">%s</div></body></html>
''' % (error_url, swift_error_url, recheck_graph_url, msg)

with open('swift_gate_status.html', 'wb') as f:
    f.write(swift_page)

neutron = '''
<html><head><title>Gate Success Rate</title></head>
<body style="width: 80%%">
<center>
<img style="margin: 0 auto;" src="%s"><br />
<img style="margin: 0 auto;" src="%s"><br />
<img style="margin: 0 auto;" src="%s"><br />
</center>
<div style="margin: 0 10%%;">%s</div></body></html>
''' % (error_url, neutron_graph_url, recheck_graph_url, msg)

with open('neutron_gate_status.html', 'wb') as f:
    f.write(neutron)

nova = '''
<html><head><title>Gate Success Rate</title></head>
<body style="width: 80%%">
<center>
<img style="margin: 0 auto;" src="%s"><br />
<img style="margin: 0 auto;" src="%s"><br />
<img style="margin: 0 auto;" src="%s"><br />
</center>
<div style="margin: 0 10%%;">%s</div></body></html>
''' % (error_url, nova_graph_url, recheck_graph_url, msg)

with open('nova_gate_status.html', 'wb') as f:
    f.write(nova)

solum = '''
<html><head><title>Gate Success Rate</title></head>
<body style="width: 80%%">
<center>
<img style="margin: 0 auto;" src="%s"><br />
<img style="margin: 0 auto;" src="%s"><br />
</center>
<div style="margin: 0 10%%;">%s</div></body></html>
''' % (solum_graph_url, recheck_graph_url, msg)

with open('solum_gate_status.html', 'wb') as f:
    f.write(solum)


cinder = '''
<html><head><title>Gate Success Rate</title></head>
<body style="width: 80%%">
<center>
<img style="margin: 0 auto;" src="%s"><br />
<img style="margin: 0 auto;" src="%s"><br />
<img style="margin: 0 auto;" src="%s"><br />
</center>
<div style="margin: 0 10%%;">%s</div></body></html>
''' % (error_url, cinder_graph_url, recheck_graph_url, msg)

with open('cinder_gate_status.html', 'wb') as f:
    f.write(cinder)


marconi = '''
<html><head><title>Gate Success Rate</title></head>
<body style="width: 80%%">
<center>
<img style="margin: 0 auto;" src="%s"><br />
<img style="margin: 0 auto;" src="%s"><br />
</center>
<div style="margin: 0 10%%;">%s</div></body></html>
''' % (marconi_graph_url, recheck_graph_url, msg)

with open('marconi_gate_status.html', 'wb') as f:
    f.write(marconi)


keystone = '''
<html><head><title>Gate Success Rate</title></head>
<body style="width: 80%%">
<center>
<img style="margin: 0 auto;" src="%s"><br />
<img style="margin: 0 auto;" src="%s"><br />
</center>
<div style="margin: 0 10%%;">%s</div></body></html>
''' % (keystone_graph_url, recheck_graph_url, msg)

with open('keystone_gate_status.html', 'wb') as f:
    f.write(keystone)
