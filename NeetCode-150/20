
class Solution:
    def isValid(self, s: str) -> bool:
        opened_form = {}
        opened_form[')'] = '('
        opened_form['}'] = '{'
        opened_form[']'] = '['
        opened_brackets =[]
        for i in s :
            if i in "{[(" :
                opened_brackets.append(i)
            else :
                if opened_brackets :
                    last_opened_character = opened_brackets[-1]
                    opened_brackets.pop() 
                    if last_opened_character != opened_form[i] :
                        return False
                else : 
                    return False
        if opened_brackets: 
            return False
        return True 
        