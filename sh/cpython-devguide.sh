hg clone https://hg.python.org/cpython
virtualenv .venv
.venv/bin/activate
pip install _bz2
pip install _dbm
pip install _gdbm
pip install _lzma
pip install _sqlite3
pip install _tkinter
pip install readline
./configure --with-pydebug && make -j2
./python -m test -j3
