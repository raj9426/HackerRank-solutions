def getPhone(s):
    digit_dict = {
        "one":1,
        "two":2,
        "three":3,
        "four":4,
        "five":5,
        "six":6,
        "seven":"7",
        "eight":8,
        "nine":9,
        "zero":0
    }
    
    res = ""
    nums = s.split(" ")
    for i in range(0,len(nums)):
        if nums[i] =="double":
            res+=str(digit_dict[nums[i+1]])
            
        elif nums[i] == "triple":
            res+=str(digit_dict[nums[i+1]])*2
            
        else:
            res +=str(digit_dict[nums[i]])
    return res
    
    
    
getPhone("five eight double two double two four eight five six")
