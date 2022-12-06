
def survive(daily_limit, survival_days, daily_req):

    totalReq = survival_days * daily_req

    daysNeeded = totalReq // daily_limit 

    if totalReq % daily_limit != 0:
        daysNeeded += 1
    
    sundays = survival_days // 7 
    validDays  = survival_days - sundays

    if daysNeeded <= validDays:
        return True, daysNeeded
    else:
        return False

print(survive(20,10,30))
print(survive(16,10,2))
