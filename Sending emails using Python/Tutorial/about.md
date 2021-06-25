Objective / Challenge:
    Send an email using Python
    Src: https://www.linkedin.com/learning/python-code-challenges/send-an-email

I sourced the solution to this problem on this site:
    https://www.freecodecamp.org/news/send-emails-using-code-4fcea9df63f/

Things I learnt (through bumping my head on these obstacles):
1)  Google do not allow untrusted apps to access your gmail details, thankfully. So to allow my "untrusted" app to log into, and send an email, from one of my gmail accounts, I'd have to give explicit permission to do this. 
    From within your account, you choose to 'Allow less secure apps'. You can do this by searching for this on Google itself. 

2) Make sure :
    -   I'm logged into the test gmail account, from which the application will be sending the email
    -   This account is set as the active account. Simply being logged into the account & having the gmail open doesn't make it the active account. 

    It does help if we're actually exposing the correct account, so that it's open to be accessed when we run this application. Its both note worthy & relieving to know that Google automatically switches off this feature once it hasn't been used for 10 mins!

3)  Keep the 'contacts.txt' file down to 1 contact (which actually exists), when testing this application for the first time. You'll want to keep the message short & simple for the same reason. 