import pexpect
m_p=pexpect.spawn('python gmail.py')
m_p.timeout=600
m_p.expect('gamil')
m_pexpect.sendline('a.gopikrishna01@gmal.com')
m_p.expect('Password')
m_p.sendline('AGK@ece001')
m_p.expect('to')
m_p.sendline('a.gopikrshna01@gmail.com')
m_p.expect('subject')
m_p.sendline('hello')
m_p.close()
