# -*-coding:utf-8-*-
'''
Created on 2013年9月5日

@author: wangzining
'''
import poplib, sys
import email
import base64,smtplib

def extract_body(payload):  
    if isinstance(payload,str):  
        return payload  
    else:  
        return '\n'.join([extract_body(part.get_payload()) for part in payload])

def accp_mail():
        try:
            p = poplib.POP3('pop.139.com')
            p.user('13260717602')
            p.pass_('19910213wzn')
            ret = p.stat()
        except poplib.error_proto, e:
            return 1
            print "Login failed:", e
            sys.exit(1)
            
        for item in p.list()[1]:
            number, octets = item.split(' ')
            lines = p.retr(number)[1]
            msg = email.message_from_string("\n".join(lines))
            body=extract_body(msg.get_payload())
            print base64.decodestring(body).decode("gbk").encode("utf-8")
            if msg.get_payload() == "start\n\n":
                return 0

def send_mail():
    try:
        handle = smtplib.SMTP('smtp.139.com', 25)
        handle.login('13260717602@139.com','19910213wzn')
        msg = "To: 1072207635@qq.com\r\nFrom: 13260717602@139.com\r\nSubject: startpc \r\n\r\nstart\r\n"
        handle.sendmail('13260717602@139.com','1072207635@qq.com', msg)
        handle.close()
        return 1
    except:
        return 0

if __name__ == "__main__":
    accp_mail()
