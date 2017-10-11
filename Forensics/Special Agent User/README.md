# Special Agent User
Points: 50

## Category
Forensics

## Question
>We can get into the Administrator's computer with a browser exploit. But first, we need to figure out what browser they're using. Perhaps this information is located in a network packet capture we took: [data.pcap](files/data.pcap). Enter the browser and version as "BrowserName BrowserVersion". NOTE: We're just looking for up to 3 levels of subversions for the browser version (ie. Version 1.2.3 for Version 1.2.3.4) and ignore any 0th subversions (ie. 1.2 for 1.2.0)

### Hint
>Where can we find information on the browser in networking data? Maybe try reading up on [user-agent strings](http://www.useragentstring.com./).

## Solution
From the challenge name, we can assume that we are trying to find the user agent. By doing `strings data.pcap | grep User-Agent`, we get this,
```
User-Agent: Wget/1.16 (linux-gnu)
User-Agent: Wget/1.16 (linux-gnu)
User-Agent: Wget/1.16 (linux-gnu)
User-Agent: Wget/1.16 (linux-gnu)
User-Agent: Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.93 Safari/537.36
User-Agent: Wget/1.16 (linux-gnu)
User-Agent: Wget/1.16 (linux-gnu)
User-Agent: Wget/1.16 (linux-gnu)
User-Agent: Wget/1.16 (linux-gnu)
```

There is one that is not like the other...

Let's try to input that.

After trying one by one, it turns out that Chrome is the correct one.

### Flag
`Chrome 40.0.2214.93`
