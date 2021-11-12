#! python3
# mcb.pyw - Saves and loads pieces of text to the clipboard.
# Usage: py.exe mcb.pyw save <keyword> - Saves clipboard to keyword.
#        py.exe mcb.pyw <keyword> - Loads keyword to the clipboard.

import shelve, pyperclip, sys

mcbShelf = shelve.open('mcb')

# Save clipboard content.
if len(sys.argv) == 3:
	if sys.argv[1].lower() == 'save':
		mcbShelf[sys.argv[2]] = pyperclip.paste()
	# Delete specific keyword
	elif sys.argv[1].lower() == 'delete' and sys.argv[2] in mcbShelf:
		del(mcbShelf[sys.argv[2]])
elif len(sys.argv) == 2:

    # Delete all keywords
	if sys.argv[1] == 'delAll':
		del(mcbShelf.keys())
    # List keywords and load content.
	elif sys.argv[1].lower() == 'list':
		pyperclip.copy(str(list(mcbShelf.keys())))
	# Copies the desired response associated with key
	elif sys.argv[1] in mcbShelf:
		pyperclip.copy(mcbShelf[sys.argv[1]])
	

mcbShelf.close()