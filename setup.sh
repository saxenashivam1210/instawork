#!/bin/bash
set -e
rm /etc/environment
echo '#!/bin/bash' >> env_setup.sh
 echo 'set -e' >> env_setup.sh
while read KEY; do 
  echo $KEY 
  echo 'echo "export '$KEY'=${'$KEY'}" >> /etc/environment' >> env_setup.sh 
done < env_key.conf
