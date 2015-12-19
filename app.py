# -*- coding: utf-8 -*-

"""
Directory listing script by Jakub Sycha

Published under the Do Whatever You Feel Like, "I Don't Fucking Care" license.
You should have received a copy of the license with this script. If you did not,
you can grab it at http://j.mp/DWYFLIDFC

Dotfiles are hidden by default. You can change this in the config.
You can edit the config down below...
"""

from flask import Flask, render_template, send_from_directory, send_file
import os
from pprint import pprint
import magic
import urllib
import sys

reload(sys)
sys.setdefaultencoding('utf8')

app = Flask(__name__)
mime = magic.Magic(mime=True)

"""
This is the configuration
"""
# To list the current directory of the script, use os.path.dirname(os.path.abspath(__file__))
base_directory = os.path.dirname(os.path.abspath(__file__))
# These directories will not be listed
ignored_dirs = ["venv"]
ignore_dotfiles = True
ignore_dollarfiles = True
omit_folders = True
omit_files = False

""" The base route with the file list """
@app.route("/")
def home():
    files = []
    dirs = []

    meta = {
        "current_directory": base_directory
    }

    for (dirpath, dirnames, filenames) in os.walk(base_directory):
        for name in filenames:
            if omit_files == True:
                break

            for ign in ignored_dirs:
                if ign in dirnames:
                    dirnames.remove(ign)

            nm = os.path.join(dirpath, name).replace(base_directory, "").strip("/").split("/")
            fullpath = os.path.join(dirpath, name)

            if os.path.isfile(fullpath) == False:
                continue

            size = os.stat(fullpath).st_size

            if len(nm) == 1:
                name_s = name.split(".")
                if ignore_dotfiles == True:
                    if name_s[0] == "" or name_s[0] == None:
                        continue

                files.append({
                    "name": name,
                    "size": str(size) + " B",
                    "mime": mime.from_file(fullpath),
                    "fullname": urllib.quote_plus(fullpath)
                })

        for dirname in dirnames:
            if omit_folders == True:
                break

            fullpath = os.path.join(dirpath, dirname)

            if ignore_dotfiles == True:
                name_split = dirname.split(".")
                if name_split[0] == "" or name_split[0] == None:
                    continue

            if ignore_dollarfiles == True:
                name_split = dirname.split("$")
                if name_split[0] == "" or name_split[0] == None:
                    continue

            dirs.append({
                "name": dirname,
                "size": "0b",
                "mime": mime.from_file(fullpath)
            })

    return render_template("index.html", files=sorted(files, key=lambda k: k["name"].lower()), folders=dirs, meta=meta)

@app.route("/download/<filename>")
def download(filename):
    filename = urllib.unquote(filename)
    if os.path.isfile(filename):
        if os.path.dirname(filename) == base_directory.rstrip("/"):
            return send_file(filename, as_attachment=True)
        else:
            return render_template("no_permission.html")
    else:
        return render_template("not_found.html")
    return None

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
