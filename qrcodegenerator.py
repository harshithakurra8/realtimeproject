import qrcode 
myqr=qrcode.make("https://www.linkedin.com/posts/stevenouri_new-open-source-physics-ai-engine-is-out-ugcPost-7275445239434113024-CQQR?utm_source=share&utm_medium=member_desktop")
myqr.save("qrcode.png")