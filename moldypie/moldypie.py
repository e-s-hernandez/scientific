import csv

# make an individual pie chart given a list of lists whose first entry is the
# title and the following entries represent label/value pairs, this function
# requires matplotlib
def make_pie(chart):
    import matplotlib.pyplot as plt

    # parse the chart into a title string and a list of labels and values
    labels = []
    values = []
    title = chart[0][0]
    del chart[0]
    for entry in chart:
        labels.append(entry[0])
        values.append(entry[1])

    # set up the figure, plot and save to png file
    fig = plt.figure()
    fig.suptitle(title)

    plt.pie(values, labels=labels)
    plt.legend(loc="lower left")
    fig.savefig(title+".png")

# set filename of the data file, this could be passed as an arg to the script
filename = "edata.csv"

# open the file and parse based on comma-delimited data
with open(filename, 'rb') as efile:
    edata = csv.reader(efile, delimiter=',')
    data = list(edata)

# logical loop, blank lines will make_pie(chart), and then reset the chart list
newtable = True
chart = []
blank_line = ['', '']
for entry in data:
    if entry == blank_line:
        make_pie(chart)
        chart = []
        newtable = True
    else:
        chart.append(entry)
        newtable=False
