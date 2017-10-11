from Crypto.Cipher import AES

cipher = AES.new('6v3TyEgjUcQRnWuIhjdTBA=='.decode('base64'),AES.MODE_ECB)
decoded = cipher.decrypt('rW4q3swEuIOEy8RTIp/DCMdNPtdYopSRXKSLYnX9NQe8z+LMsZ6Mx/x8pwGwofdZ'.decode('base64'))

print decoded