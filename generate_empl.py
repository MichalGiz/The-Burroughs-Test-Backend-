import random
import json
from optparse import OptionParser
from datetime import datetime

parser = OptionParser()
parser.add_option("-o", "--output", dest="filename", help="File to save result")
parser.add_option("-d", "--debug", action="store_true", dest="debug", default=False,
                  help="Debug process")
parser.add_option("-n", "--amount", dest="amount", help="Amount of employees to be generated")

(options, args) = parser.parse_args()

FIRST_NAMES = [
"James",
"Robert",
"John",
"Michael",
"David",
"William",
"Richard",
"Joseph",
"Thomas",
"Charles",
"Christopher",
"Daniel",
"Matthew",
"Anthony",
"Mark",
"Donald",
"Steven",
"Paul",
"Andrew",
"Joshua",
"Kenneth",
"Kevin",
"Brian",
"George",
"Timothy", ]

LAST_NAMES = [
"Wilson",
"Burton",
"Harris",
"Stevens",
"Robinson",
"Lewis",
"Walker",
"Payne",
"Baker",
"Owen",
"Holmes",
"Chapman",
"Webb",
"Allen",
"Jones",
"Davidson/Davies",
"Foster",
"Matthews",
"White",
"Griffiths",
"Knight",
"Corbyn",
"Young",
"Evans",
"Smith",
"Wright",
"Jenkins",]

amount = options.amount

random.seed(datetime.now().microsecond)

if amount is None or not amount.isdigit() or int(amount) < 1:
    print("Please provide positive value to amount (-h for help)")
    exit(128)

if options.filename in [None, '']:
    print("Please provide output filename (with -o)")
    exit(128)

result = []
for n in range(int(amount)):
    result.append({'id': n + 1, 'first_name': random.choice(FIRST_NAMES), 'last_name': random.choice(LAST_NAMES), 'salary': random.randint(10000, 25000), 'perc_bonus': random.randint(5, 15)})
if options.debug:
    for l in result:
        print(l)

with open(options.filename, "w") as f:
    json.dump(result, f)

