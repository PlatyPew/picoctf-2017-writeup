# Digital Camouflage
Points: 50

## Category
Forensics

## Question
>We need to gain access to some routers. Let's try and see if we can find the password in the captured network data: [data.pcap](data.pcap).

### Hint
>It looks like someone logged in with their password earlier. Where would log in data be located in a network capture?
>
>If you think you found the flag, but it doesn't work, consider that the data may be encrypted.

## Solution
We are supposed to find the password.

Let's see if we have any strings that contain password by doing `strings data.pcap | grep pass`

And we get this,
```html
<td><input type="password" name="pswrd"/></td>
<td><input type="password" name="pswrd"/></td>
```

We see that the form is sending a password using the name `paswrd`. Let's try to grep that by doing `strings data.pcap | grep pswrd`

We are presented with this,
```
<td><input type="password" name="pswrd"/></td>
document.login.pswrd.value = btoa(document.login.pswrd.value);
<td><input type="password" name="pswrd"/></td>
document.login.pswrd.value = btoa(document.login.pswrd.value);
&Ruserid=hardawayn&pswrd=UEFwZHNqUlRhZQ%3D%3Dv
```

We see that `pswrd=UEFwZHNqUlRhZQ%3D%3Dv`

Decoding the html elements and decoding it once more in base64, we get the flag.
```python
>>> '3D'.decode('hex')
'='
>>> 'UEFwZHNqUlRhZQ==v'.decode('base64')
'PApdsjRTae'
>>> 'UEFwZHNqUlRhZQ=='.decode('base64')
'PApdsjRTae'
```

### Flag
`PApdsjRTae`
