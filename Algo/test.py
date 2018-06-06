import pandas as pd
import matplotlib.pyplot as plt
import mpld3
import os

df = pd.read_excel('may.xlsx')
# plt.figure(figsize=(10, 8))
fig = df.groupby('CWL Name').count()['Employee Code'].plot.bar().get_figure()
fig.xlabel('CWL Name')
fig.ylabel('Employee counts')
# fig = df.groupby(x).count()[y].plot.bar().get_figure()
# outfile = APP_ROOT+r'\templates\output.html'
# mpld3.save_html(fig, open(outfile,'w'))
# mpld3.save_html(fig, 'sm.html')
mpld3.show()
