def minimumWindow (self, s: str,t: str) -> Str:
    if t == "": return ""
    countT, window = {}, {} # create two hashmaps countT and window
    for c in t:
      countT[c]= 1 + countT.get(c, 0) # adding the 0 as a second parameter to get(c,0) returns 0 as a default value if the value does not exist
    
    have, need = 0, len(countT)
    res, resLen = [-1, -1], float ("infinity")
    l = 0 # left pointer
    for r in range(len(s)):
        c = s[r]
        window [c]=1 + window.get(c, 0)
    
    if c in countT and window[c] == countT[c]:
       have += 1

    while have == need:
       # update our result
       if (r - l +1 ) < resLen:
          res = [l ,r]
          resLen = (r - l + 1)
    # pop from the left of our window
       window[s[l]] -= 1
       if s[l] in countT and window[s[l]] < countT[s[l]]:
          have -= 1
       l += 1
    l, r = res
    return s[l: r+1] if resLen!= float("infinity") else ""
       