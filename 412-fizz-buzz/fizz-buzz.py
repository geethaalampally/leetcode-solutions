# class Solution:
#     def fizzBuzz(self, n: int) -> List[str]:
#         res=[]
#         for i in range(1,n+1):
#             val=""
#             if i%15==0:
#                 val="FizzBuzz"
#             elif i%3==0:
#                 val="Fizz"
#             elif i%5==0:
#                 val="Buzz"
#             else:
#                 val=str(i)
#             res.append(val)
#         return res
        
class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        result=[]
        for i in range(1,n+1) :

            if i%3==0 and i%5==0:
                result.append("FizzBuzz")
            elif i%3==0:
                result.append("Fizz")
            elif i%5==0:
                result.append("Buzz")
            else:
                result.append(str(i))
        return result 
        