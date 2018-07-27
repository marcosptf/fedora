#comando para gerar a traducao
#msgfmt -o example.mo example.po 


import gettext

# Set up message catalog access
t = gettext.translation(
    domain='example', 
    localedir='locale',
    #languages='en_US',
    languages='pt_BR',
    fallback=False,
)
_ = t.gettext

print(_('This message is in the script.'))


