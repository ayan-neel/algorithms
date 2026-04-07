class Permute:
    def find_all_permutations_of_a_distinct_array(self,nums):
        used = []
        self.answer = []
        self.helper(nums,used)
        return self.answer
    
    def helper (self,nums, used):
        if len(nums) == len(used):
            self.answer.append(used.copy()) # add a copy of the used
        for i in range(len(nums)):
            if nums[i] not in used:
                used.append(nums[i])
                self.helper(nums, used)
                used.pop()
    
    def find_unique_permutations_of_an_array(self,nums): #unoptimized
        arr2 = []
        answer = set()
        result = self.find_all_permutations_of_an_array(nums,arr2)
        for item in result:
              answer.add(tuple(item))
        return answer;
            
    def find_all_permutations_of_an_array(self,arr1,arr2):
        if not arr1:
                return [arr2]
        result = []
        for i in range (len(arr1)):
                sub1 = arr1[0:i] + arr1[i+1:]  # n! space complexity.
                result.extend(self.find_all_permutations_of_an_array(sub1,arr2 + [arr1[i]]))
        return result
    
    # optimized - need to keep a visited list for the elements to skip the duplicate 'branch'

    def find_unique_permutations_of_an_array_ii (self,nums):
         used = []
         self.answer = []
         visited = [False] * len(nums)
         nums.sort()
         self.unique_helper(nums,used,visited)
         return self.answer
    
    def unique_helper(self,nums,used,visited):
         if len(nums) == len(used):
              self.answer.append(used.copy())
         
         for i in range(0,len(nums)):
            
            if visited[i]:
                    continue
            if i>0 and nums[i-1] == nums[i] and not visited[i-1]:
                 continue
            used.append(nums[i])
            visited[i] = True
            self.unique_helper(nums,used,visited)
            used.pop()
            visited[i] = False   
        
    
if __name__ == '__main__':
    permute = Permute()
    print(permute.find_all_permutations_of_a_distinct_array([1,2,3]))
    print(permute.find_unique_permutations_of_an_array_ii([1,2,2]))
