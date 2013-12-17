error_url = ''.join(x.strip() for x in open('error_rate_url').readlines())

msg = '''
<h3>Explanation</h3>
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
The depth of the gate queue is also tracked. This allows two things: one, a
comparison of the patch pass chance to the depth of the queue (e.g. "Is the
patch pass chance high because the queue is empty?") and two, the ability to
calculate the probability that the current gate queue will clear. To calculate
the chance that the gate queue will clear, take the decimal representation of
the patch pass chance and raise it to the depth of the gate queue. For example,
a gate queue 10 deep, when combined with a patch pass chance of 85% has a
19.69% chance of passing (100 * .85**10).
</p>

<h3>Methodology</h3>
<p>
The last two weeks are graphed by summarizing each 6-hour window into the
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
<hr/>
<p style="font-size: 80%">Source for generating this page is at
<a href="https://github.com/notmyname/gate_status">
https://github.com/notmyname/gate_status</a>
</p>
'''

page = '''
<html><head><title>Gate Success Rate</title></head>
<body style="width: 80%%">
<center><img style="margin: 0 auto;" src="%s"></center>
<div style="margin: 0 10%%;">%s</div></body></html>
''' % (error_url, msg)

with open('gate_status.html', 'wb') as f:
    f.write(page)
