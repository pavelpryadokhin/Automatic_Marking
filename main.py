from botclick import mark_etu
import time

login = 'mrpavel23ooo@mail.ru'
password = 'v234praw'

def main():
    flag = True
    if not mark_etu(login, password):
        time.sleep(10)
        flag = mark_etu(login, password)
    if flag == True:
        print('Выполнилось')
    else:
        print('Ошибка')


if __name__ == "__main__":
    main()
