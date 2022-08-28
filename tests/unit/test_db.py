from app import Zertifikate
  

def test_db():

    created_zertifikate= Zertifikate("999", "AWS")
    assert created_zertifikate.id=="999"
    assert created_zertifikate.content== "AWS"
