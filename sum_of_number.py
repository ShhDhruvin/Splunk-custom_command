import splunk.Intersplunk
directory,unused1,unused2 = splunk.Intersplunk.getOrganizedResults()
sum=0
for i in directory:
	sum+=int(i["numbers"])
directory[0]["total"] = str(sum)
splunk.Intersplunk.outputResults([{i:directory[0][i] for i in directory[0] if i in ("total","_time")}])

