
#This is generating a Public and Private RSA Key Pair named "Test"
New-RsaKeyPair -Subject 'CN=Test' -PublicKeyFile 'Test.cer' -PrivateKeyFile 'test.pfx' -Password $null