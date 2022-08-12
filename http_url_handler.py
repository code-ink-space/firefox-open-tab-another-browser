#! /usr/bin/env python3
import sys, os, re

arg_url = sys.argv[1]
# print(arg_url)

browsers = {
    'ffstable': '/usr/bin/firefox',
    'ffbeta': '/usr/bin/firefox-beta',
    'ffdev': '/usr/bin/firefox-developer-edition',
    'gchromium': '/usr/bin/chromium',
    'gchrome': '/usr/bin/google-chrome-stable',
    'msedgebeta': '/usr/bin/microsoft-edge-beta',
    'vivaldi': '/usr/bin/vivaldi-stable',
    'librewolf': '/usr/bin/librewolf',
}

pattern_protocol = 'urlbookmarklet-protocol://'
input_url = arg_url.replace(pattern_protocol, '')

pattern_ffstable = '_______ffstable'
pattern_ffbeta = '_______ffbeta'
pattern_ffdev = '_______ffdev'
pattern_chromium = '_______gchromium'
pattern_chrome = '_______gchrome'
pattern_msedgebeta = '_______msedgebeta'
pattern_vivaldi = '_______vivaldi'
pattern_librewolf = '_______librewolf'

if input_url.endswith(pattern_ffstable):
    browser = browsers['ffstable']
    url = input_url.replace(pattern_ffstable, '')
elif input_url.endswith(pattern_ffbeta):
    browser = browsers['ffbeta']
    url = input_url.replace(pattern_ffbeta, '')
elif input_url.endswith(pattern_ffdev):
    browser = browsers['ffdev']
    url = input_url.replace(pattern_ffdev, '')
elif input_url.endswith(pattern_chromium):
    browser = browsers['gchromium']
    url = input_url.replace(pattern_chromium, '')
elif input_url.endswith(pattern_chrome):
    browser = browsers['gchrome']
    url = input_url.replace(pattern_chrome, '')
elif input_url.endswith(pattern_msedgebeta):
    browser = browsers['msedgebeta']
    url = input_url.replace(pattern_msedgebeta, '')
elif input_url.endswith(pattern_vivaldi):
    browser = browsers['vivaldi']
    url = input_url.replace(pattern_vivaldi, '')
elif input_url.endswith(pattern_librewolf):
    browser = browsers['librewolf']
    url = input_url.replace(pattern_librewolf, '')
else:
    browser = browsers['ffstable']
    url = input_url

cmd = browser + ' ' + url

# print(cmd)
os.system(cmd)