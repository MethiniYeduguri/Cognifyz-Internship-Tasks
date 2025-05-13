#function to validate the email
def email_validator(email):
    if(email.count('@')==1):#checking for '@'
        #checking for extra characters
        extra_chars="`~!#$%^&*()[]{}<>|\/,;:"
        for char in extra_chars:
            if(char in email):
                return False
        
        #splitting the email at @ into username and domain
        email_parts=email.split('@')
        username=email_parts[0]
        domain=email_parts[1]

        if('.' in domain):#checking for '.' in domain
            #splitting domain into parts
            domain_parts=domain.split('.')

            #checking no.of domain parts
            if(len(domain_parts)<2):
                return False
            
            #checking domain parts satisfies both alphabet and numeric characters
            for part in domain_parts:
                if(not part.isalnum()):
                    return False
            return True
        else:
            return False     
    return False

#input
email=input("Enter an email=")

#output
if(email_validator(email)):
    print("Email is valid")
else:
    print("Email is not valid")