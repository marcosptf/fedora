import gettext

lang = gettext.translation('translate', localedir='locale', languages=['pt'])
_ = lang.gettext

lang.install()

print (_("Hello World!!!"))

