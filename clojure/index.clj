guest-3Yg0XH@LW13390:~$ mkdir clojure
guest-3Yg0XH@LW13390:~$ cd clojure/
guest-3Yg0XH@LW13390:~/clojure$ vim arquivo.sh
guest-3Yg0XH@LW13390:~/clojure$ chmod a+x arquivo.sh 
guest-3Yg0XH@LW13390:~/clojure$ ./arquivo.sh 
Downloading Leiningen to /tmp/guest-3Yg0XH/.lein/self-installs/leiningen-2.7.0-standalone.jar now...
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100   605    0   605    0     0   1079      0 --:--:-- --:--:-- --:--:--  1078
100 14.6M  100 14.6M    0     0  1439k      0  0:00:10  0:00:10 --:--:-- 1926k
Leiningen is a tool for working with Clojure projects.

Several tasks are available:
change              Rewrite project.clj by applying a function.
check               Check syntax and warn on reflection.
classpath           Print the classpath of the current project.
clean               Remove all files from project's target-path.
compile             Compile Clojure source into .class files.
deploy              Build and deploy jar to remote repository.
deps                Download all dependencies.
do                  Higher-order task to perform other tasks in succession.
help                Display a list of tasks or help for a given task.
install             Install the current project to the local repository.
jar                 Package up all the project's files into a jar file.
javac               Compile Java source files.
new                 Generate project scaffolding based on a template.
plugin              DEPRECATED. Please use the :user profile instead.
pom                 Write a pom.xml file to disk for Maven interoperability.
release             Perform :release-tasks.
repl                Start a repl session either with the current project or standalone.
retest              Run only the test namespaces which failed last time around.
run                 Run a -main function with optional command-line arguments.
search              Search remote maven repositories for matching jars.
show-profiles       List all available profiles or display one if given an argument.
test                Run the project's tests.
trampoline          Run a task without nesting the project's JVM inside Leiningen's.
uberjar             Package up the project files and dependencies into a jar file.
update-in           Perform arbitrary transformations on your project map.
upgrade             Upgrade Leiningen to specified version or latest stable.
vcs                 Interact with the version control system.
version             Print version for Leiningen and the current JVM.
with-profile        Apply the given task with the profile(s) specified.

Run `lein help $TASK` for details.

Global Options:
  -o             Run a task offline.
  -U             Run a task after forcing update of snapshots.
  -h, --help     Print this help or help for a specific task.
  -v, --version  Print Leiningen's version.

These aliases are available:
downgrade, expands to upgrade

See also: readme, faq, tutorial, news, sample, profiles, deploying, gpg,
mixed-source, templates, and copying.


guest-3Yg0XH@LW13390:~/clojure$ ./lein
bash: ./lein: No such file or directory
guest-3Yg0XH@LW13390:~/clojure$ ./lein repl
bash: ./lein: No such file or directory
guest-3Yg0XH@LW13390:~/clojure$ ./lein repl
bash: ./lein: No such file or directory
guest-3Yg0XH@LW13390:~/clojure$ 
guest-3Yg0XH@LW13390:~/clojure$ ./arquivo.sh
Leiningen is a tool for working with Clojure projects.

user=> sample

CompilerException java.lang.RuntimeException: Unable to resolve symbol: sample in this context, compiling:(/tmp/form-init8923393782825834364.clj:1:1010) 
user=> 

user=> 

user=> (+ 1 2 3)
6
user=> 

user=> (+ 6 6 6)
18
user=> (* 6 6 6)
216
user=> (+ 1, 2, 3, )
6
user=> (doc + )
-------------------------
clojure.core/+
([] [x] [x y] [x y & more])
  Returns the sum of nums. (+) returns 0. Does not auto-promote
  longs, will throw on overflow. See also: +'
nil
user=> (def number 0)
#'user/number
user=> (doc inc)
-------------------------
clojure.core/inc
([x])
  Returns a number one greater than num. Does not auto-promote
  longs, will throw on overflow. See also: inc'
nil
user=> (inc number)
1
user=> number
0
user=> (number)

ClassCastException java.lang.Long cannot be cast to clojure.lang.IFn  user/eval1258 (form-init8923393782825834364.clj:1)
user=> 'number'
number'
user=> (type number)
java.lang.Long
user=> 


user=> (def person {:address {:street "test"}})
#'user/person
user=> 

user=> (:address person)
{:street "test"}
user=> 

user=> (person :address)
{:street "test"}
user=> 

user=> (:street (person :address))
"test"
user=> 

user=> (:street (:address person))
"test"


user=> (-> person :address :street)
"test"

user=> (def numero#{1 2 3 "teste"})
#'user/numero#
user=> (type numero)

CompilerException java.lang.RuntimeException: Unable to resolve symbol: numero in this context, compiling:(/tmp/form-init8923393782825834364.clj:1:1) 
user=> 

user=> (def numero #{1 2 3 "teste"})
#'user/numero
user=> 

user=> (type numero)
clojure.lang.PersistentHashSet
user=> 

user=> (first numero)
1
user=> 

user=> '(1 2 3 4)
(1 2 3 4)
user=> (1 2 3 4)

ClassCastException java.lang.Long cannot be cast to clojure.lang.IFn  user/eval1281 (form-init8923393782825834364.clj:1)
user=> 

user=> (def lista '(1 2 3 4))
#'user/lista
user=> 

user=> (first lista)
1
user=> (nth lista)

ArityException Wrong number of args (1) passed to: core/nth  clojure.lang.AFn.throwArity (AFn.java:429)
user=> (nth lista 1)
2
user=> 

user=> (type lista)
clojure.lang.PersistentList
user=> 

user=> (def vector [1 2 3 4])
WARNING: vector already refers to: #'clojure.core/vector in namespace: user, being replaced by: #'user/vector
#'user/vector
user=> 

user=> (def vectors [1 2 3 4])
#'user/vectors
user=> (type vectors)
clojure.lang.PersistentVector

user=> 

user=> (defn velocity [espaco tempo] (/espaco tempo  ))

RuntimeException Invalid token: /espaco  clojure.lang.Util.runtimeException (Util.java:221)
CompilerException java.lang.RuntimeException: Unable to resolve symbol: tempo in this context, compiling:(/tmp/form-init8923393782825834364.clj:1:1010) 
RuntimeException Unmatched delimiter: )  clojure.lang.Util.runtimeException (Util.java:221)
RuntimeException Unmatched delimiter: )  clojure.lang.Util.runtimeException (Util.java:221)
user=> 

user=> (defn velocity [espaco tempo] (/ espaco tempo  ))
#'user/velocity
user=> 

user=> (velocity 50 100)
1/2
user=> 

user=> (velocity 50 0.5)
100.0
user=> 

user=> (fn [espaco tempo] (/ espaco tempo))
#object[user$eval1298$fn__1299 0x1def8b6c "user$eval1298$fn__1299@1def8b6c"]
user=> 

user=> (3 5)

ClassCastException java.lang.Long cannot be cast to clojure.lang.IFn  user/eval1302 (form-init8923393782825834364.clj:1)
user=> 

user=> (fn [espaco tempo] (/ espaco tempo)) 50 0.5
#object[user$eval1304$fn__1305 0xd8d2db9 "user$eval1304$fn__1305@d8d2db9"]
50
0.5
user=> (def numeros [1 2 3 4])
#'user/numeros
user=> (map #(inc %) numeros)
(2 3 4 5)

user=> (let [number 10] (+ number 1))
11

user=> 

user=> 

user=> (def cruzeirao {:name "cruzerao" :brasileirao 4})
#'user/cruzeirao
user=> (= 10 10)
true
user=> (= 10 5)
false
user=> (if (= (:brasileirao cruzerao) 4)(println "tetra")(println "ta errado")
  #_=> 
  #_=> (if (= (:brasileirao cruzerao) 4)(println "tetra")(println "ta errado"))
  #_=> 
  #_=> (if (= (:brasileirao cruzerao) 4)(println "tetra")(println "ta errado")))

CompilerException java.lang.RuntimeException: Too many arguments to if, compiling:(/tmp/form-init8923393782825834364.clj:1:1) 
user=> (if (= (:brasileirao cruzerao) 4)(println "tetra")(println "ta errado"))

CompilerException java.lang.RuntimeException: Unable to resolve symbol: cruzerao in this context, compiling:(/tmp/form-init8923393782825834364.clj:1:8) 
user=> 

user=> 

user=> (if (= (:brasileirao cruzerao) 4)(println "tetra")(println "ta errado"))

CompilerException java.lang.RuntimeException: Unable to resolve symbol: cruzerao in this context, compiling:(/tmp/form-init8923393782825834364.clj:1:8) 
user=> (if (= (:brasileirao cruzeirao) 4)(println "tetra")(println "ta errado"))
tetra
nil
