# quick-mailpy

**Quickly send mails via command line**

<sub>built with Python 3</sub>

### Parameters

Execution parameters are configured in the file `setttings.conf`

| parameter | description | default value |
|--|--|--|
| smtp_server | SMTP Server Host | -- |
| smtp_port | STMP Server Port | 587 |
| user | Username for SMTP server authentication | -- |
| password| Password for SMTP server authentication| -- |
| sender_mail| Sender mail address | -- |

### Usage

- Download this folder to your host machine
- Setup your server configurations in `settings.conf`
- Call the script with the desired command line parameters

```bash
# For detailed info, call the script with -h or --help
$> python mail.py -h

# -r, --receiver: Email address to receive the message
# -m, --message: Subject and body to the email message
# ps: Both parameters must be enclosed within quotation marks
$> python mail.py -r "target@example.com" -m "Subject: Test Mail \n Sending test mail.\nDo not reply."
```
