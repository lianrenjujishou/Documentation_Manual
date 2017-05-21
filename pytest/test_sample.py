#! encoding=utf-8
#content of test_sample.py
import pytest
import smtplib

@pytest.fixture()
def smtp(request):
    server = getattr(request.function, "smtpserver", "aaa.qq.com")
    smtp = smtplib.SMTP(server)
    yield smtp
    print("finalizing %s (%s)" % (smtp, server))
    smtp.close()

def test_showhelo(smtp):
    smtpserver = "smtp.qq.com" # will be ready by smtp fixture
    assert 0, smtp.helo()

