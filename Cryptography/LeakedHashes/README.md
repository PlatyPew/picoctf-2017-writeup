# LeakedHashes
Points: 90

## Category
Cryptography

## Question
>Someone got hacked! Check out some service's password hashes that were leaked at [hashdump.txt](files/hashdump.txt)! Do you think they chose strong passwords? We should check... The service is running at shell2017.picoctf.com:15846!

### Hint
>See if you can crack any of the login credentials and then connect to the service as one of the users. What's the chance these hashes have actually already been broken by someone else? Are there websites that host those cracked hashes? Connect from the shell with nc.

## Solution
You can use [CrackStation](https://crackstation.net/) to crack the hashes. The second line _christene:daae35de1f9c2cf09d95a99792dd7828_, is vulnerable.

We find out that the md5 hash is actually _1mp3d_.

Therefore, we can enter the service, key in the user _christene_ and the password _1mp3d_ to get the flag.

```
$ nc shell2017.picoctf.com 15846
enter username:
christene
christene's password:1mp3d
welcome to shady file server. would you like to access the cat ascii art database? y/n
y

     /\_/\ 
    ( o o )
  G-==_Y_==-M
      `-'
      
  /\ /\ 
  (O o)
=(: ^ :)=  
  '*v*'
  
 |\_/|     
 (. .)
  =w= (\   
 / ^ \//   
(|| ||)
,""_""_ .

     /\_/\ 
    ( o o )
   -==_Y_==- 
      `-'
    /\**/\ 
   ( o_o  )_)
   ,(u  u  ,),
  {}{}{}{}{}{}
  
  /\_/\ 
 ( o.o )
  > ^ <
  
       /\_/\ 
  /\  / o o \ 
 //\ \~(*)~/
 `  \/   ^ /
    | \|| ||  
    \ '|| ||  
     \)()-())
     
   A_A
  (-.-)
   |-|   
  /   \  
 |     |  __
 |  || | |  \___
 \_||_/_/
 
     /\__/\ 
    /`    '\ 
  === 0  0 ===
    \  --  /    - flag is 0d04e6db072cbd0f95854dfb3cb07118

   /        \ 
  /          \ 
 |            |
  \  ||  ||  /
   \_oo__oo_/#######o
   
  /\___/\ 
 ( o   o )
 (  =^=  ) 
 (        )
 (         )
 (          )))))))))))
 
 /\ /\ 
 (O o)
=(:^:)=  
   U
   
    _,,/|
    \o o' 
    =_~_=
    /   \ (\ 
   (////_)//
   ~~~
   
   /\     /\ 
  {  `---'  }
  {  O   O  }  
~~|~   V   ~|~~  
   \  \|/  /   
    `-----'__
    /     \  `^\_
   {       }\ |\_\_   W
   |  \_/  |/ /  \_\_( )
    \__/  /(_E     \__/
      (  /
       MM
       
              ("`-''-/").___..--''"`-._
               `6_ 6  )   `-.  (     ).`-.__.`)
               (_Y_.)'  ._   )  `._ `. ``-..-'
             _..`--'_..-_/  /--'_.' ,'
           (il),-''  (li),'  ((!.-'
           
from http://user.xmission.com/~emailbox/ascii_cats.htm
```

### Flag
`0d04e6db072cbd0f95854dfb3cb07118`
