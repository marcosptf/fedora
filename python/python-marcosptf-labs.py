>>> 
>>> data = "http://rpmrolamentos.com.br/maps/sub"
>>> data2 = "-sitemap.xml"                       
>>> 
>>> i=1
>>> print data + "%d" %i  + data2          
http://rpmrolamentos.com.br/maps/sub1-sitemap.xml
>>> 
>>> 
>>> 
>>> while(i<=175):
...     print data + "%d" %i + data2
...     i+=1
... 
http://rpmrolamentos.com.br/maps/sub1-sitemap.xml
http://rpmrolamentos.com.br/maps/sub2-sitemap.xml
http://rpmrolamentos.com.br/maps/sub3-sitemap.xml
http://rpmrolamentos.com.br/maps/sub4-sitemap.xml
http://rpmrolamentos.com.br/maps/sub5-sitemap.xml
...

12166 >>> #evolucao das concatenacoes do python
12167 ... #no python2.7 era assim
12168 >>>
12169 >>> dreno1 = "java"
12170 >>> dreno2 = "c++"
12171 >>> print "eu gosto de %s e tambem " % dreno1 +  dreno2
12172 eu gosto de java e tambem c++
12173 >>>
12174 
12175 >>> #python3.6
12176 ...
12177 >>> print("eu gosto de {0} e tambem {1}".format(dreno1, dreno2));
12178 eu gosto de java e tambem c++
12179 >>>
12180 
12181 >>>outro modo de realizar concatenacao:
12182 >>> dreno1 = "java"
12183 >>> dreno2 = "c++"
12184 >>> f'eu gosto de {dreno1} e tambem {dreno2}'
12185 'eu gosto de java e tambem c++'
12186 
12187 
12188 
12189 
