import codecs
import json
import re
import sys

reNormalize = re.compile("[\s]+")
def normalize(text):
    return reNormalize.sub(" ", text)

input = codecs.getreader("utf-8")(sys.stdin)
output = codecs.getwriter("utf8")(sys.stdout)

fields = sys.argv[1:]

for line in input:
    out = list()
    obj = json.loads(line.rstrip())
    for field in fields:
        subfields = field.split(":")
        value = obj[subfields[0]]
        for subfield in subfields[1:]:
            value = value[subfield]
        out.append(normalize(value))

    output.write(u"%s\n" % ("\t".join(out)))
