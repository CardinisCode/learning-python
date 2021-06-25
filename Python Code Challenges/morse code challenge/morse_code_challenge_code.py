class Solution:

    def run(self, morseToEnglish, textToTranslate):
        # Write your code below; return type and arguments should be according to the problem's requirements

        if len(textToTranslate) == 0:
            return "Invalid Morse Code Or Spacing"

        output = ""

        morse_reference = {
          "a": ".-", "b": "-...", "c": "-.-.", "d":"-..", "e":".", "f":"..-.", "g":"--.", "h":"....", "i":"..", "j":".---", "k":"-.-", "l":".-..", "m":"--", "n":"-.", "o":"---", "p":".--.", "q":"--.-", "r":".-.", "s":"...", "t": "-", "u":"..-", "v":"...-", "w":".--", "x":"-..-", "y":"-.--", "z":"--..", " ":"  "
        } 

        # Convert from English to Morse Code
        if morseToEnglish == False:
            for i in textToTranslate:
                if i == " ":
                    output += morse_reference[i]
                else:
                    output += morse_reference[i] + " "

            return output.rstrip()

        # From Morse to English
        if morseToEnglish:
            textToTranslate_list = textToTranslate.split("   ")

            for morse_word in textToTranslate_list:
                morse_word_list = morse_word.split()
                
                for letter in morse_word_list:
                    for english, morse_code in morse_reference.items():
                        if letter == morse_code:
                            output += english

                output += " "
                    
        return output.rstrip()

solution = Solution()
print(solution.run(True, "- .... .   .-- .. --.. .- .-. -.."))

