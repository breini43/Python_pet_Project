class CommentFromWebSite():
    '''
    "Комментарии с сайта
    '''
    def __init__(self, data, text, likes):
        self.data = data
        self.text = text
        self.likes = int(likes)

    def showComment(self):
            '''

            '''
            print(f'\nКомментарий с сайте, \n дата: {self.data},'
                  f'\n текст: {self.text}, лайков: {self.likes}')

    def changeLikes(self):
            '''

            '''
            self.likes = self.likes + 1

    def changeComment(self, new_text):
            self.text = new_text

new_comment = CommentFromWebSite('11/02/20', 'Первый!', '11')
new_comment2 = CommentFromWebSite('22/03/19', 'Второй', '5')

new_comment.showComment()
new_comment2.data