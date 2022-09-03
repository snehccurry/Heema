import webbrowser


urls=['https:\\www.google.com', 
'https:\\www.facebook.com',
 'https:\\www.facebook.com', 
 'https:\\www.facebook.com',
  'https:\\www.facebook.com', 
  'https:\\www.facebook.com', 
  'https:\\www.facebook.com', 
  'https:\\www.facebook.com', 
  'https:\\www.facebook.com', 
  'https:\\www.facebook.com',
  'https:\\www.facebook.com', 
  'https:\\www.facebook.com', 
  'https:\\www.facebook.com', 
  'https:\\www.facebook.com',
  'https:\\www.facebook.com', 
  'https:\\www.facebook.com', 
  'https:\\www.facebook.com', 
  'https:\\www.facebook.com', 
  'https:\\www.facebook.com',
  'https:\\www.facebook.com']




"""
for url in urls:
    webbrowser.open_new_tab(url)
"""

























"""

'mozilla'
	

Mozilla('mozilla')
	

'firefox'
	

Mozilla('mozilla')
	

'netscape'
	

Mozilla('netscape')
	

'galeon'
	

Galeon('galeon')
	

'epiphany'
	

Galeon('epiphany')
	

'skipstone'
	

BackgroundBrowser('skipstone')
	

'kfmclient'
	

Konqueror()
	

(1)

'konqueror'
	

Konqueror()
	

(1)

'kfm'
	

Konqueror()
	

(1)

'mosaic'
	

BackgroundBrowser('mosaic')
	

'opera'
	

Opera()
	

'grail'
	

Grail()
	

'links'
	

GenericBrowser('links')
	

'elinks'
	

Elinks('elinks')
	

'lynx'
	

GenericBrowser('lynx')
	

'w3m'
	

GenericBrowser('w3m')
	

'windows-default'
	

WindowsDefault
	

(2)

'macosx'
	

MacOSXOSAScript('default')
	

(3)

'safari'
	

MacOSXOSAScript('safari')
	

(3)

'google-chrome'
	

Chrome('google-chrome')
	

'chrome'
	

Chrome('chrome')
	

'chromium'
	

Chromium('chromium')
	

'chromium-browser'
	

Chromium('chromium-browser')
	

Notes:

    “Konqueror” is the file manager for the KDE desktop environment for Unix, and only makes sense to use if KDE is running. Some way of reliably detecting KDE would be nice; the KDEDIR variable is not sufficient. Note also that the name “kfm” is used even when using the konqueror command with KDE 2 — the implementation selects the best strategy for running Konqueror.

    Only on Windows platforms.

    Only on macOS platform.

New in version 3.3: Support for Chrome/Chromium has been added.

Here are some simple examples:

url = 'https://docs.python.org/'

# Open URL in a new tab, if a browser window is already open.
webbrowser.open_new_tab(url)

# Open URL in new window, raising the window if possible.
webbrowser.open_new(url)



"""