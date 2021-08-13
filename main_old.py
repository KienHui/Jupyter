import jupyter, notebook, notebook.notebookapp
import jupyterlab.labapp

# This does NOT seem to work without forking first. You also need to go to the `repl.co` link in another tab.

# Fork (!) and run this REPL, then navigate to http://<SERVER>.repl.co/tree
# to get to standard notebook and  http://<SERVER>.repl.co/lab for the lab

# Both JupyterLab and standard notebook work
# with JUPYTERLAB=True. 
JUPYTERLAB=True

kwargs = dict(ip='0.0.0.0', port=8080, password_required=False, token='')

if JUPYTERLAB:
  jupyterlab.labapp.main(**kwargs)
else:
  notebook.notebookapp.launch_new_instance(**kwargs)