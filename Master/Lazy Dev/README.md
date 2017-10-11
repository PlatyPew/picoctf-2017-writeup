# Lazy Dev
Points: 50

## Category
Master

## Question
>I really need to login to this [website](http://shell2017.picoctf.com:43393/), but the developer hasn't implemented login yet. Can you help?

### Hint
>Where does the password check actually occur?
>
>Can you interact with the javascript directly?

## Solution
Looking at Google Chrome's Developer Tool's Sources, we cat see that there is `index` and `client.js`

The website is using only client-side validation.

Looking at the javascript, we can see that no matter what input is used, the password is always wrong

```javascript
//Validate the password. TBD!
function validate(pword){
  //TODO: Implement me
  return false;
}
```

Changing `return false` to `return true`, we enter any password and get the flag

### Flag
`client_side_is_the_dark_sidea99c64effed2c2f1c9347eff536e949c`
