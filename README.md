# R513ScanRes
TP R513 Scan Res, application flask, notebook



****************curl**************** 
curl https://nginx.org/download/nginx-1.18.0.tar.gz -o nginx.tar.gz
curl -O https://nginx.org/download/nginx-1.18.0.tar.gz (-O permete de garder le nom de fichier distant)

curl --limit-rate 5M https://cdn.kernel.org/pub/linux/kernel/v5.x/linux-5.17.7.tar.xz -o nginx.tar.gz
CTRL+C
curl --limit-rate 5M -C -  https://cdn.kernel.org/pub/linux/kernel/v5.x/linux-5.17.7.tar.xz -o nginx.tar.gz  
(Use "-C -" to instruct curl to automatically find out where/how to resume the transfer. It then uses the given output/input files to figure that out.)


xargs -n 1 curl -O < file.txt  (xargs -n 1 affiche les éléments du file.txt un par un, ligne par ligne (xargs < file.txt afiche tout ur une seule ligne))

curl http://mto38.free.fr --> dans wireshark, user agent = curl/8.5.0\r\n

****************wget****************

wget https://nginx.org/download/nginx-1.18.0.tar.gz    (ajoute un choffre à chaque fois que la meme dossier est download)
wget -o nginx.tar.gz https://nginx.org/download/nginx-1.18.0.tar.gz (renomme le fichier)

wget --limit-rate=5m https://cdn.kernel.org/pub/linux/kernel/v5.x/linux-5.17.7.tar.xz (on lance un téléchargement avec une rate de 5 mo/s)
CTRL + C  (stop du telechargement)
wget --limit-rate=5m https://cdn.kernel.org/pub/linux/kernel/v5.x/linux-5.17.7.tar.xz -c (on reprends le téléchargement la ou on en était.)

Créer un file.txt avec les URLs puis 
wget -i file.txt



/!\ pour l'app4, il faut créer un répertoire TP1_Web/uploads/web ou modifier la variable UPLOAD_FOLDER



Pour la partie certificats:
creer un dossir certs

ajouter des certificats en .pem
executer cette commande pour avoir des liens symboliques: for file in *.pem ; do ln -s $file $(openssl x509 -hash -noout -in $file).0 ; done

vérifier le fonctionnement: curl --capath ~/R513/certs/  https://self-signed.badssl.com/ 

si ok, on peut déclarer les variables:

pour wget : ca-directory = <the_cert_rep_path>
pour curl : capath = <the_cert_rep_path>

curl -k -X POST -F "file=@file.txt" https://127.0.0.1:5001/upload  (curl -k car mon self certificat est mal fait mais sinon tout fonctionne)