# LOGICAL OPERATOR AND / OR / NOT

hasHighIncome = True
hasGoodCredit = True
hasCriminalRecord = False


# if hasHighIncome and hasGoodCredit:
#     print("eligible for loan")

# if hasHighIncome or hasGoodCredit:
#     print("eligible for loan")

if hasGoodCredit and not hasCriminalRecord:
    print("eligible for loan")
