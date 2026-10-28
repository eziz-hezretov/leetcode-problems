class Solution:
    def mostWordsFound(self, sentences: list[str]) -> int:
        
        longest_sentence = 0
        split_sentences = []

        for sentence in sentences:

            split_sent = []
            split_sent += sentence.split()
            split_sentences.append(split_sent)


        print(split_sentences)

        for sentence in split_sentences:
            if len(sentence) >= longest_sentence:
                longest_sentence = len(sentence)
        
        return longest_sentence