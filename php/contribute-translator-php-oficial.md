# Referências

- https://wiki.php.net/doc/translations/pt_br
- http://doc.php.net/tutorial/local-setup.php

# Dependências

## PEAR
```
cd ~/contribs/php-manual
wget http://pear.php.net/go-pear.phar
php -d detect_unicode=0 go-pear.phar
```

## PHD
```
cd ~/contribs/php-manual
git clone http://git.php.net/repository/phd.git
cd phd
sudo pear install package.xml package_generic.xml package_php.xml
```

## EN - 1a. vez
```
cd ~/contribs/php-manual
svn checkout https://svn.php.net/repository/phpdoc/modules/doc-en
cd doc-en
php doc-base/configure.php --enable-xml-details
phd --docbook doc-base/.manual.xml --package PHP --format php --output mydocs
```

## EN - próximas vezes
```
cd ~/contribs/php-manual/doc-en
svn update
php doc-base/configure.php --enable-xml-details
phd --docbook doc-base/.manual.xml --package PHP --format php --output mydocs
```

## PT-BR - 1a. vez
```
cd ~/contribs/php-manual
svn checkout https://svn.php.net/repository/phpdoc/modules/doc-pt_BR
php doc-base/configure.php --enable-xml-details --with-lang=pt_BR
phd --docbook doc-base/.manual.xml --package PHP --format php --output mydocs
```

## PT-BR - próximas vezes
```
cd ~/contribs/php-manual/doc-pt_BR
svn update
php doc-base/configure.php --enable-xml-details --with-lang=pt_BR
phd --docbook doc-base/.manual.xml --package PHP --format php --output mydocs
```

## WEB - 1a. vez
```
cd ~/contribs/php-manual
git clone https://github.com/php/web-php.git
rm -r `pwd`/web-php/manual/en
ln -s `pwd`/doc-en/mydocs/php-web `pwd`/web-php/manual/en
ln -s `pwd`/doc-pt_BR/mydocs/php-web `pwd`/web-php/manual/pt_BR
cd web-php
php -S 0.0.0.0:4000
```

## WEB - próximas vezes
```
cd ~/contribs/php-manual/web-php
git clean -df
git checkout -- .
git pull
cd ~/contribs/php-manual
rm -r `pwd`/web-php/manual/en
ln -s `pwd`/doc-en/mydocs/php-web `pwd`/web-php/manual/en
ln -s `pwd`/doc-pt_BR/mydocs/php-web `pwd`/web-php/manual/pt_BR
cd web-php
php -S 0.0.0.0:4000
```

## Revcheck

```
php doc-base/scripts/revcheck.php pt_BR > revcheck.html
open revcheck.html
```

## SVN

```
svn revert --recursive .
svn status
svn commit
```
