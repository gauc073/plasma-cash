sudo apt-get install libsnappy-dev
export VER="1.20"
wget https://github.com/google/leveldb/archive/v${VER}.tar.gz
tar xvf v${VER}.tar.gz
rm -f v${VER}.tar.gz
cd leveldb-1.20/
make
sudo scp -r out-static/lib* out-shared/lib* "/usr/local/lib"
cd include
sudo scp -r leveldb /usr/local/include
sudo ldconfig

