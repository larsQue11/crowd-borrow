class Account:
    def __init__(self, id, institutionUserId, institutionCustomerId, institutionId, description, nickName, hostAccountNumber, accountNumber, category,
                 ownershipType, interestRate, isAccountHyBrid, isVisible, isHiddenByFi, micrNumber, type, availableBalance, recipient_id):
        self.id = id
        self.institutionUserId = institutionUserId
        self.institutionCustomerId = institutionCustomerId
        self.institutionId = institutionId
        self.description = description
        self.nickName = nickName
        self.hostAccountNumber = hostAccountNumber
        self.accountNumber = accountNumber
        self.category = category
        self.ownershipType = ownershipType
        self.interestRate = interestRate
        self.isAccountHybrid = isAccountHyBrid
        self.isVisible = isVisible
        self.isHiddenByFi = isHiddenByFi
        self.micrNumber = micrNumber
        self.type = type
        self.availableBalance = availableBalance
        self.recipient_id = recipient_id

    def to_dict (self):
        data = {
            u' id': str(self.id)
        }

    def __str__(self):
        return "id = "+self.id+\
               "\ninstitutionUserId = "+self.institutionUserId+\
               "\ninstitutionCustomerId = "+self.institutionCustomerId+\
               "\ninstitutionId = "+ self.institutionId+\
               "\ndescription = "+self.description+\
               "\nnickName = "+self.nickName+\
               "\nhostAccountNumber = "+self.hostAccountNumber+\
               "\naccountNumber = "+self.accountNumber+\
               "\navailableBalance = "+str(self.availableBalance)+"\n\n"
