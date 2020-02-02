class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        
        #print(trips)
        
        #print(capacity)
        
        farest = 0
        
        for num,start,end in trips:
            farest = max(farest, end)
            
        
        val = [0] * (farest+1)
        
        for num,start,end in trips:
            for i in range(start,end):
                val[i] += num
                
                if val[i] > capacity:
                    return False
                
        return True