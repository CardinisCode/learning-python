class Solution:

    def run(self, p):
        #
        # Write your code below; return type and arguments should be according to the problem's requirements
        #
        p_split_list = p.split()
        reverse_list = p_split_list[::-1]
        reverse_string = " ".join(reverse_list)
        pv_str = ""

        vowel_count = 0
        consonant_count = 0
        for word in p_split_list:
            for letter in word:
                if letter.lower() in ['a','e','i','o','u']:
                    vowel_count += 1
                elif letter.isalpha():
                    consonant_count += 1

        for letter in p:
            if letter.lower() in ['a','e','i','o','u']:
                pv_str += "pv" + letter
            elif letter.isalpha():
                pv_str += letter
            else:
                pv_str += letter

        combined_queries = str(vowel_count) + " " + str(consonant_count) + "::"
        for i in reverse_string:
            if i.islower():
                combined_queries += i.capitalize()
            else:
                combined_queries += i.lower()
        
        combined_queries += "::" + "-".join(p.split()) + "::" + pv_str
        
        return combined_queries


solution = Solution()
print(solution.run("pA tA"))