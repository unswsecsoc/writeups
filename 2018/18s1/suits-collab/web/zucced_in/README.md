# Zucced In

## Flavortext
With everyone looking for a new social network, I decided to build my own,  
it's so secure I can't even log back into the admin account!  

https://zucced.hashbangctf.com

## Hint
Perhaps I should try and reset my password  

## Solution

The main goal was to log in as admin, but wrong passwords would give a small hint:  
"Perhaps I should try and reset my password" 

Playing around with your own account and the password reset system you might have realised that the password reset link generated is always the same, which is insecure because it should be re-generated for each request. 

Furthermore, the "token" is simply the MD5 hash of the username, so if you wanted to reset the admin's password you simply gave 
`21232f297a57a5a743894a0e4a801fc3` as the token and you are able to reset the admin's login to anything you want and then log in.

Password link was generated like this, so...
```
def forgot_password():
    if request.method == 'POST':
        username = request.form.get('username', '')
        recovery = hashlib.md5(username.encode("utf")).hexdigest()
        recovery_addr = request.url_root+"recover/"+username+"/"+recovery
        print (recovery_addr)
        if get_email(username) != None:
            email_reset(recovery_addr, get_email(username))
            return render_template('forgot_password.html', message="Email Sent!")
```

So to get the flag, go to <url>/admin/md5(admin)

## Answer
FLAG{Safebook_might_be_a_misnomer}


