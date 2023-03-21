import sys
from getparentdir import GetParentDir
from nametoscripts import NameToScripts
from executecommands import ExecuteAppleCommand

parentPath = GetParentDir()

args = sys.argv

if len(args) > 1:
    name = args[1]
    scripts = NameToScripts(name)
    ExecuteAppleCommand(scripts,parentPath)
