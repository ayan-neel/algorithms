
def print_all_permutations_of_string(s1, s2):
        if s1 is None or s1 =="":
            print(s2)
           
        for i in range(len(s1)) : #n
            sub1 = s1[0:i]
            sub2 = s1[i+1:]   #for the last character, s1[i+1:] safely returns "" instead of causing an IndexError #n
            print_all_permutations_of_string("".join([sub1,sub2]), s2+s1[i]) #n!


#time complexity of this code - O(n X n X n!)

def print_all_permutations_of_an_array(arr1, arr2):
    if not arr1:
          print(arr2)
    for i in range(len(arr1)):
        sub1 = arr1[0:i] + arr1[i+1:]
        print_all_permutations_of_an_array(sub1, arr2 + [arr1[i]])  #pass a new list in each recursion. mutating the list in place will cause issues in the subsequent recursion call.

def find_all_permutations_of_an_array(arr1,arr2):
    if not arr1:
            return [arr2]
    result = []
    for i in range (len(arr1)):
            sub1 = arr1[0:i] + arr1[i+1:]
            result.extend(find_all_permutations_of_an_array(sub1,arr2 + [arr1[i]]))
    return result

def print_all_permutations_of_an_array(nums,tmp):
    if not nums:
          print(tmp)
    for i in range(len(nums)):
         sub = nums[0:i] + nums[i+1:]
         print_all_permutations_of_an_array(sub, tmp + [nums[i]])

if __name__ == '__main__':
#    print_all_permutations_of_string("ergon","")
#    print_all_permutations_of_an_array([3,4,5,6],[])
   print(find_all_permutations_of_an_array([1,3,4,5],[]))