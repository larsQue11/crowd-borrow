class Recipient:
    def __init__(self, id, institutionID, memberNumber, institutionCustomerID, passCode, email, nickName):
        self.id = id
        self.institutionID  = institutionID
        self.memberNumber = memberNumber
        self.institutionCustomerID = institutionCustomerID
        self.passCode = passCode
        self.email = email
        self.nickName = nickName

    def __str__(self):
        return "id = "+self.id+\
               "\ninstitutionId = "+self.institutionID+\
               "\nmemberNumber = "+self.memberNumber+\
               "\ninstitutionCustomerID = "+self.institutionCustomerID+\
               "\npassCode = "+self.passCode+\
               "\nemail = "+self.email+\
               "\nnickName = "+self.nickName+"\n\n"


