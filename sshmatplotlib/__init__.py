# When running any matplotlib-based code in a non-graphical environment (eg. SSH),
# after 'import matplotlib' you may encounter errors such as the following:
#
# ImportError: No module named '_tkinter', please install the python3-tk package
#
# Unable to access the X Display, is $DISPLAY set properly?
#
# The following code checks if your Python program is being run in a text-based
# environment (eg. an SSH console) and configures Matplotlib accordingly
import os
if not os.environ.get('DISPLAY'):
    import matplotlib
    matplotlib.use('Agg')
