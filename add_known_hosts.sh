for i in $(cat ansible_hosts)
do
ssh-keyscan $i >> ~/.ssh/known_hosts
done

