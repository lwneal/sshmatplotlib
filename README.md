# SSH Matplotlib

Do you SSH from your laptop to run Python code on a server?
Do you run into errors about `tkinter` and `$DISPLAY` caused by
matplotlib?
Do you just want your code to output a `.png` graph or figure?

This extremely simple library will enable matplotlib's SSH-compatible
nongraphical mode. Just add:

```python
import sshmatplotlib
```

to the very beginning of your Python code.
