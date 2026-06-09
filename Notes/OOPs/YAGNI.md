## YAGNI 

YAGNI stand for - You Aren't Gonna Need It

---

Do't build the feratures until they're actually needed.

#### BAD

	class NotificationService:
		def send_email(self):
			pass

		def send_sms(self):
			pass

		def send_whatsapp(self):
			pass

		def send_slack(self):
			pass

When the application only sends emails.

#### Better 
	class NotificationService:
		def send_email(self):
			pass
	
Add new channels only when required.


## KISS

- Stand for - Keep It Simple, Stupid
- In another phrases - Keep It Simple and Straightforward

- Bad (Overcomplicated)
```
def is_even(num):
    return True if ((num % 2) == 0) else False
```

- Good (KISS)

```
def is_even(num):
    return num % 2 == 0
```

