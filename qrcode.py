import qrcode
print("---QR code generator---")
data=input("enter text or URL: ")
img=qrcode.make(data)
file_name=input("enter filename(without png):")
img.save(file_name+".png")
print(f"\n qrcode generated successfully")
print(f" saved as:{file_name}.png")
