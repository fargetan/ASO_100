import tarfile

tar_ref =  tarfile.open('data/marx-geo.tar.gz', 'r:gz')
tar_ref.extractall()
tar_ref.close()
