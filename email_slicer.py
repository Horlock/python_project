def emailSlicer(email):    
    atSign = email.find('@')
    dotCom = email.find('.com')
    user = email[0:atSign].replace('.', ' ')
    domain = email[atSign+1:dotCom]
    print("Username: %s" %(user).title())
    print("Domain: %s" %(domain).capitalize())


email = input("Digite seu e-mail: ")


emailSlicer(email)
