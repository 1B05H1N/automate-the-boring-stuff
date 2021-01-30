import smtplib
conn = smtplib.SMTP('smtp.email.com', 587)
type(conn)
conn.ehlo()
conn.starttls()
conn.login('email@email.com', 'password')
conn.sendmail('email@email.com', 'email@email.com', 'Subject: So long...\n\nDear Person, \nSo long, and thanks for all the fish.\n\n-Person')
conn.quit()