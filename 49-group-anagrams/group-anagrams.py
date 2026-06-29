# class Solution:
#     def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
#         dict={}
#         seen=set()
#         output=[0]*len(strs)
#         idx1=0
#         for w1 in strs:
#             w2=''.join(sorted(w1))
#             if w2 not in seen:
#                 seen.add(w2)
#                 dict[w2]=idx1
#                 output[idx1]=[w1]
#                 idx1+=1
#             else:
#                 idx2=dict.get(w2)
#                 output[int(idx2)].append(w1)
#         out=[x for x in output if x!=0]
#         return out
                
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}

        for word in strs:
            key = ''.join(sorted(word))

            if key not in groups:
                groups[key] = []

            groups[key].append(word)

        return list(groups.values())