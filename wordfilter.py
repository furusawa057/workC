class WordFilter:
    def __init__(self, erased_word, replaced_word):
        self.word = erased_word
        self.eraser = replaced_word

    def detect(self, message):
        detect_result = []
        for word in self.word:
            detect_result.append(word in message)
        return detect_result
        # return self.word in message

    def censor(self, message):
        for word in self.word:
            message = message.replace(word, self.eraser)
        print(message)


def main():
    yn='y'
    while yn=='y':
        my_NGword = input('NGワード：').split()
        my_filter = WordFilter(erased_word=my_NGword, replaced_word="-----")

        # NGワードが含まれている場合
        my_filter.censor("昨日のアーセナルの試合アツかった！")

        # NGワードが含まれていない場合
        my_filter.censor("昨日のリバプールの試合アツかった！")

        yn = input('WordFilter?(y/n):')
    else:
        print('END')



if __name__ == '__main__':
    main()
