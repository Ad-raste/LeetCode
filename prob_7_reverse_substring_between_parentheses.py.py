"""Leetcode : 1190. Reverse Substrings Between Each Pair of Parentheses
10/07/24 -> 11/07/24"""

class Solution:
    def reverseParentheses(self, s: str) -> str:
        list_s = list(s)
        list_open, list_colse = [],[]
        
        #on recupere les emplacements de toutes les parentaises
        for item in enumerate(list_s):
            if item[1] == "(":
                list_open.append(list(item))
            elif item[1] == ")":
                list_colse.append(list(item))
        
        #on supprime les parentaises en les remplacant par du vide
        for item in range(len(list_s)):
            if list_s[item] == "(" or list_s[item] == ")":
                list_s[item] = ""
        
        #on inverse la liste des parentaises ouvrantes
        list_open.reverse()
        for item in range(len(list_colse)):
            #on regarde la correspondance des parentaises
            for item in range(len(list_colse)):
                if list_colse[item][0] >= list_open[0][0]:
                    closed = list_colse[item][0]
                    # on retire la parentaise que l'on vient de prendre
                    del list_colse[item]
                    break
            
            # on retire la parentaise que l'on vient de prendre
            opened = list_open[0][0]
            del list_open[0]
            
            al = list_s[opened:closed]
            al.reverse()
            list_s = list_s[:opened] + al + list_s[closed:]
        
        s = "".join(list_s)
        return s

if __name__ == "__main__":
    sol = Solution()
    print(sol.reverseParentheses("(abcd)")) # "dcba"
    print(sol.reverseParentheses("(u(love)i)")) # "iloveu"
    print(sol.reverseParentheses("(ed(et(oc))el)")) # "leetcode"
    print(sol.reverseParentheses("(e((((de))(t()o)c))el)")) # "lectoede"