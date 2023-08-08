class Stack:
    def __init__(self) -> None:
        self.__ls = []
        self.__size = 0

    def push(self, vl):
        self.__ls.append(vl)
        self.__size += 1

    def empty(self):
        return self.__size == 0

    def pop(self):
        if not self.empty():
            self.__size -= 1
            return self.__ls.pop()
        else:
            raise Exception("Xatolik")

    def top(self):
        return self.__ls[-1]
    
    def size(self):
        return self.__size
    

class Solution:
    def isValid(self, s: str) -> bool:
        st = Stack()
        for i in s:
            if i in "({[":
                st.push(i)
            else:
                if not st.empty() and i == ')' and st.top() == '(':
                    st.pop()
                elif not st.empty() and i == '}' and st.top() == '{':
                    st.pop()
                elif not st.empty() and i == ']' and st.top() == '[':
                    st.pop()
                else:
                    return False
        if st.empty():
            return True
        else:
            return False
        
