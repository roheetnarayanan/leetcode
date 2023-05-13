class Solution:
    def decodeString(self, s: str) -> str:
        stack = []

        for i in s:
            if i!="]":
                stack.append(i)
            else:
                ## Retreive all the chars inside the bracket
                curr_str = []
                while  stack[-1]!="[":
                    curr_str.append(stack.pop())
                stack.pop()
                curr_str.reverse()

                ## Retreive the repeat value ; break if the stack is empty
                curr_k = ""
                while stack and stack[-1].isdigit():
                    curr_k += stack.pop()
                curr_k = int("".join(curr_k[::-1]))

                curr_str = curr_str*curr_k
                stack.extend(curr_str)
        return "".join(stack)
