#dependencias
#sudo dnf install xgettext msgfmt

#criar diretorios para internationalization
"""
mkdir locale/
mkdir locale/en_US/
mkdir locale/en_US/LC_MESSAGES/
mkdir locale/pt_BR/
mkdir locale/pt_BR/LC_MESSAGES/
"""

#comando para extrair string de traducao
#xgettext -o example.pot gettext_example.py

#comando para gerar a traducao
#msgfmt -o example.mo example.po 



import gettext

# Set up message catalog access
t = gettext.translation(
    domain='example', 
    localedir='locale',
    #languages='en_US',
    languages=['pt_BR'],
    fallback=False,
)
_ = t.gettext

print(_('This message is in the script.'))


