#필요한 모듈 호출
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes

#키 생성
key = get_random_bytes(16)

#암호화 데이터 인코딩
data = "Hello, World!".encode('utf-8')

#암호화 객체 생성 및 암호화
cipher = AES.new(key, AES.MODE_CBC)
ct_bytes = cipher.encrypt(pad(data, AES.block_size))

#초기화 벡터 iv, 암호문 ct
iv = cipher.iv
ct = ct_bytes

#복호화 객체 생성 및 복호화
cipher2 = AES.new(key, AES.MODE_CBC, iv=iv)
pt = unpad(cipher2.decrypt(ct), AES.block_size)

#복호문 디코딩후 출력
print(f"decrypted message is:{pt.decode('utf-8')}")
