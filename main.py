# This does NOT seem to work without forking first. You also need to go to the `repl.co` link in another tab.

# Fork (!) and run this REPL, then navigate to http://<SERVER>.repl.co/tree
# to get to standard notebook and  http://<SERVER>.repl.co/lab for the lab


import jupyterlab.labapp
jupyterlab.labapp.main(ip='0.0.0.0', port=8080, password_required=False, token='')