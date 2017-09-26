# keyz
Points: 20

## Category
Cryptography

## Question
>While webshells are nice, it'd be nice to be able to login directly. To do so, please add your own public key to ~/.ssh/authorized_keys, using the webshell. Make sure to copy it correctly! The key is in the ssh banner, displayed when you login remotely with ssh, to shell2017.picoctf.com

### Hint
>There are plenty of tutorials out there. This one covers key generation: https://confluence.atlassian.com/bitbucketserver/creating-ssh-keys-776639788.html
>
>Then, use the web shell to copy/paste it, and use the appropriate tool to ssh to the server using your key

## Solution
Let's start by generating a ssh key by doing `ssh-keygen -t rsa -b 1024`

Copy the contents from `~/.ssh/id_rsa.pub` and paste it in the web shell in `~/.ssh/authorized_keys`

Now just ssh into the shell `ssh username@shell2017.picoctf.com` replacing `username` with your own

```
The authenticity of host 'shell2017.picoctf.com (34.206.4.227)' can't be established.
ECDSA key fingerprint is SHA256:ZIqVNC9hm15Z6mdDFCWC/H0+5MzSzXEhW3a+iHP1HM4.
Are you sure you want to continue connecting (yes/no)? yes
Warning: Permanently added 'shell2017.picoctf.com,34.206.4.227' (ECDSA) to the list of known hosts.
Congratulations on setting up SSH key authentication!
Here is your flag: who_needs_pwords_anyways
platy@shell-web:~$ 
```

### Flag
`who_needs_pwords_anyways`
