while IFS=$'\t' read -r -a tmp ; do
ssh-keyscan "${tmp[0]}" >> ~/.ssh/known_hosts
done < ansible_hosts
